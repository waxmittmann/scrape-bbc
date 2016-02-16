# I'm sure that this is not good practice; I've come across using setuptools / setup.py to do a local dev install
# (e.g. http://stackoverflow.com/questions/1893598/pythonpath-vs-sys-path), but I just don't have the time to figure
# out the intricacies of that mechanism, so proper deployment will have to fall to the wayside for now.
import sys
import os
import unittest
from mock import MagicMock
from mock import patch

sys.path.insert(1, os.getcwd())
# patch('scrapymasters.pipelines.MongoWriterPipeline.MongoWriterPipeline')
from scrapymasters.pipelines.MongoWriterPipeline import MongoWriterPipeline


class MongoWriterPipelineTest(unittest.TestCase):

    # @patch('scrapymasters.pipelines.MongoWriterPipeline')
    # @patch('scrapymasters.pipelines.MongoWriterPipeline.MongoWriterPipeline')
    def test_process_item_should_add_item_to_bulk_transaction(self):
        # Given
        mongo_writer_pipeline = MongoWriterPipeline()
        # print(type(mongo_writer_pipeline))
        # with patch('scrapymasters.pipelines.MongoWriterPipeline') as self_mock:
        # mock_self = MagicMock[MongoWriterPipeline]()
        # mock_self = MagicMock()
        # mock_self.__getitem__ = MagicMock()
        # mock_self.bulk = MagicMock()
        # mongo_writer_pipeline.bulk.insert = MagicMock()



        title = "Title"
        url = "url"
        tags = "tags"
        summary = "summary"
        header = "header"
        body = "body"

        stripped_article = {
            title: "Title",
            url: "url",
            tags: "tags",
            summary: "summary",
            header: "header",
            body: "body"
        }

        article = {
            title: "Title",
            url: "url",
            tags: "tags",
            summary: "summary",
            header: "header",
            body: "body",
            "something": "else"
        }

        # def process_item(self, article, spider):
        # result = MongoWriterPipeline.process_item(mock_self, article, None)
        result = mongo_writer_pipeline.process_item(article, None)

        # Then
        self.assertEqual(result, article)
        result.
        mongo_writer_pipeline.bulk.insert.assert_called_with(stripped_article)

    if __name__ == '__main__':
        unittest.main()
