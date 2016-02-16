# I'm sure that this is not good practice; I've come across using setuptools / setup.py to do a local dev install
# (e.g. http://stackoverflow.com/questions/1893598/pythonpath-vs-sys-path), but I just don't have the time to figure
# out the intricacies of that mechanism, so proper deployment will have to fall to the wayside for now.
import sys
import os
import unittest
from mock import MagicMock

sys.path.insert(1, os.getcwd())
from scrapymasters.common.MongoUtils import MongoUtils


class XpathUtilTest(unittest.TestCase):
    def test_find_article_by_url_should_return_list_of_results_from_cursor(self):
        # Given
        mock_cursor = ["someitem"]
        mock_db = MagicMock()
        mock_db.articles = MagicMock()
        mock_db.articles.find = MagicMock(return_value=mock_cursor)
        some_url = "http://www.someurl.com"

        # When
        result = MongoUtils.find_article_by_url(mock_db, some_url)

        # Then
        self.assertEqual(result, ["someitem"])
        mock_db.articles.find.assert_called_with({"url": some_url})

    if __name__ == '__main__':
        unittest.main()
