import datetime # will use to split dates out into the correct format
from collections import defaultdict # will use to group lines by author
import csv #will need to write processed file to csv

#reading in the the file
def read_file(changes_file):
    #using strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-' #defining seperator for each commit as 72 hyphens
    commits = [] #creating an empty list of commits
    current_commit = None
    index = 0
    while index < len(data): #loop as long as the index is less that the no. of lines in the file
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|') #split all data from line 1 on pipe, save to a variable called details
            year = int((details[2][0:5]).strip()) #identifying year from the date line in details so i can split further in the dictionary
            month = int((details[2][6:8]).strip())#identifying month from the date line in details so i can split further in the dictionary
            day = int((details[2][9:11]).strip())#identifying day from the date line in details so i can split further in the dictionary
            number_of_lines = int(details[3].strip().split(' ')[0])#defining number_of_lines outside the dictionary so I can use to find comments
            # creating a dictionary called commit with each element of details included
            commit = {'revision': details[0].strip().strip('r'),	#stripping spaces, and 'r' in the revision element 
                'author': details[1].strip(),
                # 'full-date': details[2].strip(),
                'date': datetime.date(year, month, day).strftime("%Y-%m-%d"),
                'week': datetime.date(year, month, day).strftime("%W"),
                'number_of_lines': int(details[3].strip().split(' ')[0]),
                'changes': data[index+2:data.index('',index+1)], #creating these as list so the will print in a single row when in output even though they are multiple lines long
                'comments': data[index-number_of_lines:index]
            }
            # add details to the list of commits
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits
    
#count commits per author
def get_authors(commits):
    authors = {}
    for commit in commits: #loop through all the commits in the commits list
        author = commit['author'] #create new variable called author from the dictionary element author
        if author not in authors: #if the author occurs once, assign 1
            authors[author] = 1
        else:
            authors[author] = authors[author] + 1 #if the author occurs multiple times, increment the count by 1
    return authors
    
#counting commits per week
def get_weekly_commits(commits):
    weekly_commits = {}
    for commit in commits: #loop through all the commits in the commits list
        weekly_commit = commit['week'] #create new variable called author from the dictionary element author
        if weekly_commit not in weekly_commits: #if the author occurs once, assign 1
            weekly_commits[weekly_commit] = 1
        else:
            weekly_commits[weekly_commit] = weekly_commits[weekly_commit] + 1 #if the author occurs multiple times, increment the count by 1
    return weekly_commits
    
#counting commits per day           
def get_daily_commits(commits):
    daily_commits = {}
    for commit in commits: #loop through all the commits in the commits list
        daily_commit = commit['date'] #create new variable called author from the dictionary element author
        if daily_commit not in daily_commits: #if the author occurs once, assign 1
            daily_commits[daily_commit] = 1
        else:
            daily_commits[daily_commit] = daily_commits[daily_commit] + 1 #if the author occurs multiple times, increment the count by 1
    return daily_commits
    
#using defaultdict to group number of lines by author by looping through the commits dict with author as the key
#using the iadd method to append the number of lines each time
def get_lines(commits):
    lines = defaultdict(int)
    for x in commits:
        lines[x['author']] += x['number_of_lines']
    return lines
    
#function to print my summary tuples into columns for readability in cmdpromt
#using the lenth of each item in the tuple to define the width and adding a cushion of 3 for readability    
def tuple_to_column(my_tuple_list):    
    width = max(len(e) for t in my_tuple_list for e in t[:-1]) + 3 
    format=('%%-%ds' % width) * len(my_tuple_list[0])
    return '\n'.join(format % tuple(t) for t in my_tuple_list)

if __name__ == '__main__':
    changes_file = 'changes_python.log' #open the file
    data = read_file(changes_file) #read all the lines
    commits = get_commits(data) #creating list of dictionaries, one commit is one element of the dictionary
    authors = get_authors(commits) #creating a list of commits by author
    lines = get_lines(commits)
    daily_commits = get_daily_commits(commits)
    weekly_commits = get_weekly_commits(commits)
    sorted_dates = sorted([x['date'] for x in commits]) # i know this list is the same length as my list of commits, so i can use the index for 1st and last dates
    
#using string formatting to print and summarise the file in the terminal
# print '\nThere are {} number of lines of data in this log file, all of which contain data relating to {} github commits.'.format(len(data), len(commits))
# print 'These commits were made by {} different authors between {} and {}.\n'.format(len(authors), sorted_dates[0], sorted_dates[421])
# print '***************************************************************************************************************'
# print 'The top 5 authors, ranked by the number of commits are: \n'
# print tuple_to_column(sorted(authors.items(), key=lambda x:x[1], reverse=True)[:5])# using lambda to return key-value pairs from mydict, from highest to lowest
# print '\nThomas and Jimmy are by far the most productive developers on this project in terms of commits.'
# print '***************************************************************************************************************'
# print 'The top 5 authors, ranked by the number of comments are: \n'
# print tuple_to_column(sorted(lines.items(), key=lambda x:x[1], reverse=True)[:5])
# print '\nThomas and Jimmy also made the most comments on this project.'
# print '***************************************************************************************************************'
# print 'The most productive 5 weeks of the year (2015) ranked by the number of commits are: \n'
# print tuple_to_column(sorted(weekly_commits.items(), key=lambda x:x[1], reverse=True)[:5])
# print '\nThe most commits were made in week 28 of 2015.'
# print '***************************************************************************************************************'
# print 'The most productive 5 days of the year ranked by the number of commits are: \n'
# print tuple_to_column(sorted(daily_commits.items(), key=lambda x:x[1], reverse=True)[:5])
# print '\nThe most commits were made on August 4th, 2015.'
# print '***************************************************************************************************************'

#writing the file to .csv for further processing
#each key in the dict will print to a column
#each dict in the list of dicts will print to a row
# keys = commits[0].keys()
# with open('log_changes.csv', 'wb') as output_file:
    # dict_writer = csv.DictWriter(output_file, keys)
    # dict_writer.writeheader()
    # dict_writer.writerows(commits)


