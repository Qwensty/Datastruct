import unittest
from utils.node import Node

class Test_Stack(unittest.TestCase):
    def test_stack__init__(self, node_10):
        self.assertEqual(Node(10), node_10)
