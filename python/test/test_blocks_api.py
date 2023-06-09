# -*- coding: utf-8 -*-

"""
    Notion API

    Hello and welcome!  To make use of this API collection collection as it's written, please duplicate [this database template](https://www.notion.so/8e2c2b769e1d47d287b9ed3035d607ae?v=dc1b92875fb94f10834ba8d36549bd2a).  [Create an integration](https://www.notion.so/my-integrations) to retrieve an API token, add your database and page ID's as variables in the collection, and start making your requests!  For our full documentation, including sample integrations and guides, visit [developers.notion.com](developers.notion.com)  Need more help? Join our [developer community on Slack](https://join.slack.com/t/notiondevs/shared_invite/zt-lkrnk74h-YmPRroySRFGiqgjI193AqA/)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import notion_client
from notion_client.api.blocks_api import BlocksApi  # noqa: E501
from notion_client.rest import ApiException


class TestBlocksApi(unittest.TestCase):
    """BlocksApi unit test stubs"""

    def setUp(self):
        self.api = notion_client.api.blocks_api.BlocksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_blocks_id_children_get(self):
        """Test case for v1_blocks_id_children_get

        Retrieve block children  # noqa: E501
        """
        pass

    def test_v1_blocks_id_children_patch(self):
        """Test case for v1_blocks_id_children_patch

        Append block children  # noqa: E501
        """
        pass

    def test_v1_blocks_id_delete(self):
        """Test case for v1_blocks_id_delete

        Delete a block  # noqa: E501
        """
        pass

    def test_v1_blocks_id_get(self):
        """Test case for v1_blocks_id_get

        Retrieve a block  # noqa: E501
        """
        pass

    def test_v1_blocks_id_patch(self):
        """Test case for v1_blocks_id_patch

        Update a block  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
