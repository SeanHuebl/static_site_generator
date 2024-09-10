import unittest

from enums import TextType
from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode

class TestSplitNode(unittest.TestCase):

    def test_split_nodes_delimiter_bold(self):
        """Test splitting a text node by bold (`**`) delimiter."""
        text_node = TextNode('This is a text with a **bold word**', TextType.TEXT)
        result = split_nodes_delimiter([text_node], '**')
        expected = [
            TextNode('This is a text with a ', TextType.TEXT),
            TextNode('bold word', TextType.BOLD)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_italic(self):
        """Test splitting a text node by italic (`*`) delimiter."""
        text_node = TextNode('This is a text node with an *italic* word in the middle', TextType.TEXT)
        result = split_nodes_delimiter([text_node], "*")
        expected = [
            TextNode('This is a text node with an ', TextType.TEXT),
            TextNode('italic', TextType.ITALIC),
            TextNode(' word in the middle', TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_code(self):
        """Test splitting a text node by code (` ` `) delimiter."""
        text_node = TextNode('This is a text node with a `code block` in the middle', TextType.TEXT)
        result = split_nodes_delimiter([text_node], "`")
        expected = [
            TextNode('This is a text node with a ', TextType.TEXT),
            TextNode('code block', TextType.CODE),
            TextNode(' in the middle', TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_non_text(self):
        """Test that non-text nodes are not split by delimiters."""
        non_text_node = TextNode('This whole node is bold', TextType.BOLD)
        result = split_nodes_delimiter([non_text_node], '`')
        self.assertEqual(result, [non_text_node])

    def test_split_links(self):
        """Test splitting text nodes with Markdown links."""
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_links_multiple(self):
        """Test splitting text nodes with multiple Markdown links."""
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(result, expected)

    def test_split_images(self):
        """Test splitting text nodes with Markdown images."""
        node = TextNode('This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)', TextType.TEXT)
        result = split_nodes_image([node])
        expected = [
            TextNode('This is text with a ', TextType.TEXT),
            TextNode(None, TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif", "rick roll"),
            TextNode(' and ', TextType.TEXT),
            TextNode(None, TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg", "obi wan")
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
