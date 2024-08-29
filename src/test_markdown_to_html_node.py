import unittest

from enums import BlockType
from markdown_to_html_node import markdown_to_html_node

class TestMDtoHTMLNode(unittest.TestCase):
    def test_parent(self):
        text = '''# This is the heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n```here is a block of code```'''
    
        return markdown_to_html_node(text)
if __name__ == "__main__":
    unittest.main()