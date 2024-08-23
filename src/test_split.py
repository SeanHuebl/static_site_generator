import unittest
from textnode import TextNode
from split_node import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_snd(self):
        text_node = TextNode('This is a text with a **bold word**', 'text')

        print(split_nodes_delimiter([text_node], '**', 'text'))
        text_node2 = TextNode('This is a text node with an *itallic* word in the middle', 'text')
        print(split_nodes_delimiter([text_node2],"*", 'text'))
        text_node3 = TextNode('This is a text node with a `code block` in the middle', 'text')
        print(split_nodes_delimiter([text_node3], "`", 'text'))
        non_text_node = TextNode('This whole node is bold', 'bold')
        print(split_nodes_delimiter([non_text_node], '`', 'text'))
if __name__ == "__main__":
    unittest.main()