import unittest

from query_collections import exceptions
from query_collections import query_dict
from query_collections import filters

contents = query_dict({
    "status": "FAILURE",
    "errors": [
        {
            "code": 100,
            "message": "Failed to contact backend"
        },
        {
            "code": 101,
            "message": "Failed to start backend service"
        },
        {
            "message": "test"
        }
    ],
    "user_stats": {
        "count": 200,
        "active": 10,
        "most_recent_login_ids": [
            100,
            200,
            300
        ]
    }
})


class TestQueryDict(unittest.TestCase):
    """
    Tests to verify functionality of Query Collections.
    Tests must ensure 100% code coverage!
    """
    def testQueryTopLevelMember(self):
        result = contents.query("status")
        self.assertEqual('FAILURE', result)

    def testQueryMemberChild(self):
        result = contents.query("user_stats:count")
        self.assertEqual(200, result)

    def testQueryMemberChildList(self):
        result = contents.query("user_stats:most_recent_login_ids")
        self.assertEqual([100, 200, 300], result)

    def testQueryMemberChildDict(self):
        result = contents.query("user_stats")
        self.assertEqual(contents.user_stats, result)

    def testQueryExist(self):
        self.assertTrue(contents.query("user_stats!"))

    def testQueryNonExist(self):
        self.assertFalse(contents.query("invalid!"))

    def testQueryListWithExistingItem(self):
        # ensures we can retrieve a list of members from a list
        # where the member exists
        result = contents.query("errors:*:code!:code")
        self.assertEqual([100, 101], result)

    def testInitialWildcard(self):
        result = contents.query("*")
        self.assertEqual(contents, result)

    def testQueryForExistingItems(self):
        result = contents.query("errors:*:code!:*")
        for item in result:
            self.assertIn(item, [contents.errors[0], contents.errors[1]])

    def testWildcard(self):
        result = contents.query("errors:*")
        self.assertEqual(contents.errors, result)

    def testEmptyQuery(self):
        with self.assertRaises(exceptions.InvalidQueryException) as ex:
            contents.query("")

    def testIndexQueryOperator(self):
        result = contents['?errors:*']
        self.assertEqual(contents.errors, result)

        norm = contents['errors']
        self.assertEqual(contents.errors, norm)

    def testIndexQueryList(self):
        list_instance = contents.errors
        result = list_instance['?*']
        self.assertEqual(contents.errors, result)

        norm = contents.errors[0]
        self.assertEqual(list.__getitem__(contents.errors, 0), norm)

    def testFilterOperatorList(self):
        matched_error = contents.errors[0]
        result = contents.query("errors:*:code$", filters=filters.eq(100))[0]
        self.assertEqual(result, matched_error)

    def testFilterOperatorNoComparator(self):
        with self.assertRaises(exceptions.InvalidFilterException) as ex:
            matched_error = contents.errors[0]
            result = contents.query("errors:code$")

    def testInvalidFilterIndex(self):
        with self.assertRaises(exceptions.InvalidFilterException) as ex:
            matched_error = contents.errors[0]
            result = contents.query("errors:0:code$2")

