import unittest
from unittest.mock import Mock
from htmlnode import *
from textnode import TextNode
from enums import TextType


class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        
    def test_print(self):
        node = HTMLNode("h1", None, None, {"href": "https://www.google.com", "target": "_blank",})
        #return print(node)    
    
    def test_props_to_html(self):
        node = HTMLNode("h1", None, None, {"href": "https://www.google.com", "target": "_blank",})
        #print(node.props_to_html())        

    def test_to_html(self):
        node = LeafNode("p", "hello world")
        #print(node.to_html())
        node2 = LeafNode("a", "click me!", {"href": "https://www.google.com", "target": "_blank",})
        #print(node2.to_html())

    def test_parent_node_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        #node.to_html()
    def test_nested_parents(self):
        node = ParentNode(
            "p",
            [
                ParentNode("h1", [LeafNode("b", "Bold text"),]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),

            ],
        )
        #node.to_html()

    def test_nested_parents_two(self):
        node2 = ParentNode(
            "p",
            [
                ParentNode("h1", [LeafNode("b", "Bold text"),]),
                ParentNode("h2", [ParentNode("h3", [LeafNode(None, "Normal text"),]), 
                                  ParentNode("h4", [LeafNode(None, "Normal text"), LeafNode("i", "italic text"),])
                                  ]),
                LeafNode("i", "italic text"),

            ],
        )
        #node2.to_html()
        
    def test_text_node_text(self):
        text_node = TextNode("I am a plain text node", TextType.TEXT)        
        node = text_node_to_html_node(text_node)
        #print(node.to_html())

    def test_text_node_bold(self):
        text_node = TextNode("I am a bold text node", TextType.BOLD)
        node = text_node_to_html_node(text_node)
        #print(node.to_html())

    def test_text_node_itallic(self):
        text_node = TextNode("I am an itallic text node", TextType.ITALIC)
        node = text_node_to_html_node(text_node)
        #print(node.to_html())
    
    def test_text_node_code(self):
        text_node = TextNode("I am a code text node", TextType.CODE)
        node = text_node_to_html_node(text_node)
        #print(node.to_html())
    
    def test_text_node_link(self):
        text_node = TextNode("I am a link text node", TextType.LINK, "www.google.com")
        node = text_node_to_html_node(text_node)
        #print(node.to_html())

    def test_text_node_img(self):
        text_node = TextNode("", TextType.IMAGE, "/static/img.1", "this is an image text node")
        node = text_node_to_html_node(text_node)
        #print(node.to_html())
        
if __name__ == "__main__":
    unittest.main()