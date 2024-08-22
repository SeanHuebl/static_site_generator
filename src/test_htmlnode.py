import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_to_html(self):
        node = LeafNode("p", "hello world")
        print(node.to_html())
        node2 = LeafNode("a", "click me!", {"href": "https://www.google.com", "target": "_blank",})
        print(node2.to_html())

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

        node.to_html()
    def test_nested_parents(self):
        node = ParentNode(
            "p",
            [
                ParentNode("h1", [LeafNode("b", "Bold text"),]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),

            ],
        )
        node.to_html()

    def test_nested_parents_two(self):
        node2 = ParentNode(
            "p",
            [
                ParentNode("h1", [LeafNode("b", "Bold text"),]),
                ParentNode("h2", [ParentNode("h3", [LeafNode(None, "Normal text"),]), 
                                  ParentNode("h4", [LeafNode(None, "Normal text"), LeafNode("i", "italic text"),])]),
                LeafNode("i", "italic text"),

            ],
        )
        node2.to_html()
        
if __name__ == "__main__":
    unittest.main()