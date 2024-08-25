import unittest
from textnode import TextNode
from split_node import split_nodes_delimiter, split_nodes_link, split_nodes_image

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

    def test_split_links(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and", 'text')
        print(split_nodes_link([node]))
        node2 = TextNode('[to boot dev](https://www.bootdev.com)', 'text')
        print(split_nodes_link([node2]))
        node3 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", 'text')
        print(split_nodes_link([node3]))       
        
        print(split_nodes_link([node, node2, node3,]))

    def test_split_images(self):
        node = TextNode('This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)', 'text')
        print(split_nodes_image([node]))
if __name__ == "__main__":
    unittest.main()