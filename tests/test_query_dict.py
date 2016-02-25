import unittest
from query_collections import query_dict
from query_collections import exceptions

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
    def testQueryTopLevelMember(self):
        result = contents.query("status")
        self.assertEqual('FAILURE', result)

    def testQueryMemberChild(self):
        result = contents.query("user_stats:count")
        self.assertEqual(200, result)

    def testQueryMemberChildList(self):
        result = contents.query("user_stats:most_recent_login_ids")
        self.assertEqual([100,200,300], result)

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
        self.assertEqual([100,101], result)

    def testWildcard(self):
        result = contents.query("errors:*")
        self.assertEqual(contents.errors, result)

    def testEmptyQuery(self):
        try:
            contents.query("")
            self.fail()
        except exceptions.InvalidQueryException:
            pass

