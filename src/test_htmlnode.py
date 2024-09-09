import unittest

from enums import TextType
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode



class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertTrue(
            node.children == None or
            node.children == []
        )
        self.assertTrue(
            node.props == None or
            node.props == {}
        )
        
    def test_props_to_html(self):
        """Test conversion of properties to HTML format."""
        node = HTMLNode("h1", None, None, {"href": "https://www.google.com", "target": "_blank"})
        expected_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_leaf_node_to_html(self):
        """Test HTML generation for LeafNode with different tags."""
        node = LeafNode("p", "hello world")
        self.assertEqual(node.to_html(), "<p>hello world</p>")

        node2 = LeafNode("a", "click me!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com" target="_blank">click me!</a>')

    def test_parent_node_to_html(self):
        """Test HTML generation for ParentNode with child LeafNodes."""
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_output)

    def test_nested_parents(self):
        """Test HTML generation for nested ParentNode and LeafNode structure."""
        node = ParentNode(
            "p",
            [
                ParentNode("h1", [LeafNode("b", "Bold text")]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
            ],
        )
        expected_output = "<p><h1><b>Bold text</b></h1>Normal text<i>italic text</i></p>"
        self.assertEqual(node.to_html(), expected_output)

    def test_nested_parents_two(self):
        """Test HTML generation for deeply nested ParentNode structures."""
        node2 = ParentNode(
            "p",
            [
                ParentNode("h1", [LeafNode("b", "Bold text")]),
                ParentNode("h2", [
                    ParentNode("h3", [LeafNode(None, "Normal text")]),
                    ParentNode("h4", [LeafNode(None, "Normal text"), LeafNode("i", "italic text")])
                ]),
                LeafNode("i", "italic text"),
            ],
        )
        expected_output = "<p><h1><b>Bold text</b></h1><h2><h3>Normal text</h3><h4>Normal text<i>italic text</i></h4></h2><i>italic text</i></p>"
        self.assertEqual(node2.to_html(), expected_output)
        
    def test_text_node_text(self):
        """Test conversion of TextNode to LeafNode HTML for plain text."""
        text_node = TextNode("I am a plain text node", TextType.TEXT)        
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.to_html(), "I am a plain text node")

    def test_text_node_bold(self):
        """Test conversion of TextNode to LeafNode HTML for bold text."""
        text_node = TextNode("I am a bold text node", TextType.BOLD)
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.to_html(), "<b>I am a bold text node</b>")

    def test_text_node_italic(self):
        """Test conversion of TextNode to LeafNode HTML for italic text."""
        text_node = TextNode("I am an italic text node", TextType.ITALIC)
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.to_html(), "<i>I am an italic text node</i>")
    
    def test_text_node_code(self):
        """Test conversion of TextNode to LeafNode HTML for code text."""
        text_node = TextNode("I am a code text node", TextType.CODE)
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.to_html(), "<code>I am a code text node</code>")
    
    def test_text_node_link(self):
        """Test conversion of TextNode to LeafNode HTML for link text."""
        text_node = TextNode("I am a link text node", TextType.LINK, "www.google.com")
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.to_html(), '<a href="www.google.com">I am a link text node</a>')

    def test_text_node_img(self):
        """Test conversion of TextNode to LeafNode HTML for image text."""
        text_node = TextNode("", TextType.IMAGE, "/static/img.1", "this is an image text node")
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.to_html(), '<img src="/static/img.1" alt="this is an image text node"></img>')
        
if __name__ == "__main__":
    unittest.main()