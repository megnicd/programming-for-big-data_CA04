import unittest
from collections import defaultdict
from process_log_changes import get_commits, read_file #,get_lines, get_weekly_commits

#IN ORDER FOR THESE TO WORK, ENSURE THAT LINES 99-127 IN PROCESS_LOG_CHANGES ARE COMMENTED OUT
class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('1551925', commits[0]['revision'])
        self.assertEqual('2015-11-27',commits[0]['date'])
        
### COULD NOT GET THESE TESTS TO WORK - ERROR SAYING THAT MY NAMED FUNCTIONS WERE NOT DEFINED
        
    # def test_get_lines(self):
        # lines = get_lines(self.data)
        # self.assertEqual([10], len(commits))
        
    # def test_get_lines(self):
        # weekly_commits = get_weekly_commits(self.data)
        # self.assertEqual([20], len(weekly_commits.data))

if __name__ == '__main__':
    unittest.main()
