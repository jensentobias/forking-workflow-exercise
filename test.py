"""
This will loop through all the files with group*.py and assert that their
tweet()-function returns a string that is less than 280 characters long.
"""

import os
import unittest

class TestTweets(unittest.TestCase):

    def test_smaller_than_280(self):

        for filename in os.listdir("."):
            if filename.startswith("group") and filename.endswith(".py"):
                module_name = filename[:-3]  # ignore .py at the end
                module = __import__(module_name)
                tweet_content = module.tweet().encode('utf-8')
                self.assertTrue(len(tweet_content) <= 280)

    def test_larger_than_280(self):
        module = __import__("inerror")
        tweet_content = module.tweet().encode('utf-8')
        self.assertFalse(len(tweet_content) <= 280)

    def test_forced_error(self):
        module = __import__("inerror")
        tweet_content = module.tweet().encode('utf-8')
        self.assertFalse(len(tweet_content) > 280)

if __name__ == '__main__':
    unittest.main()
