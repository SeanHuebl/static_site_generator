import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode
from enums import TextType

class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_textnodes(self):
        """Test conversion of Markdown text to TextNodes with various elements."""
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) with a [superlink](https://github.com)[link2](https://link2.com)[link4](https://extra.com) end text"

        # Convert text to TextNodes
        result = text_to_textnodes(text)

        # Expected result list of TextNodes
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(None, TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg", "obi wan image"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" with a ", TextType.TEXT),
            TextNode("superlink", TextType.LINK, "https://github.com"),
            TextNode("link2", TextType.LINK, "https://link2.com"),
            TextNode("link4", TextType.LINK, "https://extra.com"),
            TextNode(" end text", TextType.TEXT)
        ]

        # Assert that the result matches the expected list of TextNodes
        self.assertEqual(result, expected)

    def test_text_without_markdown(self):
        """Test text without any Markdown syntax."""
        text = "This is plain text with no markdown."
        result = text_to_textnodes(text)
        expected = [TextNode("This is plain text with no markdown.", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_mixed_content(self):
        """Test text with mixed Markdown elements."""
        text = "**Bold** and `code` and [link](https://example.com)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("Bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com")
        ]
        self.assertEqual(result, expected)

    def test_incorrect_markdown(self):
        """Test that text with incorrect or unmatched Markdown syntax throws a ValueError."""
        text = "This is **not closed bold and `not closed code."
        
        with self.assertRaises(ValueError):
            text_to_textnodes(text)
      

if __name__ == "__main__":
    unittest.main()
