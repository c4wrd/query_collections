import unittest

from query_collections import Stream


class testStream(unittest.TestCase):

    def testNext(self):
        stream = Stream.of(1,2,3,4)

        for i in range(1,5):
            self.assertEqual(i, stream.next().getAsInt())

        self.assertFalse(stream.next().isPresent())

    def getAsInt(self):
        stream = Stream.of(1)

        self.assertEqual(stream.next().getAsInt(), 1)

    def testSkip(self):
        stream = Stream.of(1,2,3,4,5,6)

        self.assertNotIn(1, stream.skip(1))