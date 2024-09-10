import unittest

from enums import TextType
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        """Test equality of two TextNode objects with the same attributes."""
        node = TextNode("This is a text node", TextType.BOLD, "boot.dev", None)
        node2 = TextNode("This is a text node", TextType.BOLD, "boot.dev", None)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        """Test inequality when TextNode objects have different text."""
        node = TextNode("I am different", TextType.BOLD, "boot.dev", None)
        node2 = TextNode("Am I different?", TextType.BOLD, "boot.dev", None)
        self.assertNotEqual(node, node2)

    def test_not_equal_url(self):
        """Test inequality when TextNode objects have different URLs."""
        node = TextNode("Same text", TextType.BOLD, "boot.dev", None)
        node2 = TextNode("Same text", TextType.BOLD, "different.dev", None)
        self.assertNotEqual(node, node2)

    def test_not_equal_type(self):
        """Test inequality when TextNode objects have different TextTypes."""
        node = TextNode("Same text", TextType.BOLD, "boot.dev", None)
        node2 = TextNode("Same text", TextType.ITALIC, "boot.dev", None)
        self.assertNotEqual(node, node2)

    def test_none(self):
        """Test that TextNode attributes are not None after initialization."""
        node = TextNode("This is a text node", TextType.BOLD, "boot.dev", None)
        self.assertIsNotNone(node.text)
        self.assertIsNotNone(node.text_type)
        self.assertIsNotNone(node.url)

    def test_empty_text(self):
        """Test TextNode initialization with an empty text string."""
        node = TextNode("", TextType.BOLD, "boot.dev", None)
        self.assertEqual(node.text, "")
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertEqual(node.url, "boot.dev")
        self.assertIsNone(node.alt_text)

    def test_repr(self):
        """Test the __repr__ method of TextNode for accurate string representation."""
        node = TextNode("Text", TextType.LINK, "https://boot.dev", None)
        expected_repr = "TextNode(text=Text, text_type=TextType.LINK, url=https://boot.dev, alt_text=None)"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()
