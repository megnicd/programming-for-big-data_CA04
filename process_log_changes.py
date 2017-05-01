def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
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
            # creating a dictionary called commit with each element of details included
            commit = {'revision': details[0].strip().strip('r'),	#stripping spaces, and 'r' in the revision element 
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[1]
            }
            # add details to the list of commits
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits
    
def get_authors(commits):
    authors = {}
    for commit in commits: #loop through all the commits in the commits list
        author = commit['author'] #create new variable called author from the dictionary element author
        if author not in authors: #if the author occurs once, assign 1
            authors[author] = 1
        else:
            authors[author] = authors[author] + 1 #if the author occurs multiple times, increment the count by 1
    return authors

if __name__ == '__main__':
    changes_file = 'changes_python.log' #open the file
    data = read_file(changes_file) #read all the lines
    commits = get_commits(data) #creating list of dictionaries
    authors = get_authors(commits) #creating a list of commits by author
	
	#printing random data just to see if things are working correctly	
    print(len(data)) # no of lines read
    print(commits[0:2]) # print the first 3 commits
    print(commits[1]['author']) #print the author of the the 2nd commit
    print(len(commits)) #print the number of commits
    print authors


	



