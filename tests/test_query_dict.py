import unittest

from query_collections import query_dict


class ClassDummy(query_dict):

    MyVariable = "Hi!"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__setitem__('MyVariable', 'valid')

class QueryDictTest(unittest.TestCase):

    def testAccessClassMember(self):
        d = ClassDummy()
        print(d.MyVariable)
        self.assertEqual(d.MyVariable, 'valid')
        self.assertEqual(d['MyVariable'], 'valid')
        self.assertEqual(d.get('MyVariable'), 'valid')
        self.assertEqual(d.query("MyVariable"), "valid")