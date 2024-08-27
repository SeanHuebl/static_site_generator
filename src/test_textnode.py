import unittest

from enums import TextType
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "boot.dev", None)
        node2 = TextNode("This is a text node", TextType.BOLD, "boot.dev", None)
        self.assertEqual(node, node2)

    def test_different(self):
        node = TextNode("I am different", TextType.BOLD, "boot.dev", None)
        node2 = TextNode("Am I different?", TextType.BOLD, "boot.dev", None)
        self.assertNotEqual(node, node2)
        
    def test_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "boot.dev", None)
        self.assertIsNotNone(node.text)
        self.assertIsNotNone(node.text_type)
        self.assertIsNotNone(node.url)
            
        
         

if __name__ == "__main__":
    unittest.main()