import unittest
from textnode import TextNode
from split_node import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_snd(self):
        text_node = TextNode('This is a text with a **bold word**', 'text')

        print(split_nodes_delimiter([text_node], '**', 'text'))
        text_node2 = TextNode('This is a text node with a **bold** word in the middle')

if __name__ == "__main__":
    unittest.main()