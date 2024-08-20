import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        
    def test_print(self):
        node = HTMLNode("h1", None, None, {"href": "https://www.google.com", "target": "_blank",})
        return print(node)    
    
    def test_props_to_html(self):
        node = HTMLNode("h1", None, None, {"href": "https://www.google.com", "target": "_blank",})
        print(node.props_to_html())        
        
         

if __name__ == "__main__":
    unittest.main()