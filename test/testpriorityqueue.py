import unittest
from ds2.priorityqueue import (
                                SimpleListPQ,
                                SortedListPQ,
                                UnsortedListPQ,
                                HeapPQ,
                                PriorityQueue,
                                )

class PQTests:
    def testinit(self):
        P = self.PQ()

    def testinsert(self):
        P = self.PQ()
        P.insert('a', 2)
        P.insert('b', 3)
        P.insert('c', 1)

    def testfindmin(self):
        P = self.PQ()
        P.insert('a', 2)
        self.assertEqual(P.findmin(), 'a')
        P.insert('b', 3)
        self.assertEqual(P.findmin(), 'a')
        P.insert('c', 1)
        self.assertEqual(P.findmin(), 'c')

    def testremovemin(self):
        P = self.PQ()
        for item, priority in [('two', 2), ('three', 3), ('one', 1)]:
            P.insert(item, priority)
        self.assertEqual(P.removemin(), 'one')
        self.assertEqual(P.removemin(), 'two')
        self.assertEqual(P.removemin(), 'three')

    def testlargerexample(self):
        P = self.PQ()
        for i in range(1000):
            P.insert(i,i)
        for j in range(1000):
            self.assertEqual(P.removemin(), j)

def _test(implementation):
    class MyPQTestCase(unittest.TestCase, PQTests):
        PQ = implementation
    return MyPQTestCase

TestSimpleListPQ = _test(SimpleListPQ)
TestHeapPQ = _test(HeapPQ)
TestSortedListPQ = _test(SortedListPQ)
TestUnsortedListPQ = _test(UnsortedListPQ)

class TestPriorityQueue(unittest.TestCase, PQTests):
    PQ = PriorityQueue

    def testinitwihtentries(self):
        P = self.PQ([('a', 3), ('b', 6), ('c', 4)])
        P = self.PQ((i,i) for i in reversed(range(100)))

    def testlen(self):
        P = self.PQ()
        self.assertEqual(len(P), 0)
        for i in range(10):
            P.insert(i, i + 10)
        self.assertEqual(len(P), 10)
        P.removemin()
        self.assertEqual(len(P), 9)

    def testreducepriority(self):
        P = self.PQ()
        for i in range(10):
            P.insert(i, i + 10)
        self.assertEqual(P.findmin(), 0)
        P.reducepriority(4, 6)
        self.assertEqual(P.findmin(), 4)
        P.reducepriority(7, 8)
        self.assertEqual(P.removemin(), 4)
        self.assertEqual(P.removemin(), 7)


if __name__ == '__main__':
    unittest.main()
