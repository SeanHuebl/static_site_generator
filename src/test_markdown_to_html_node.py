import textwrap
import unittest

from enums import BlockType
from markdown_to_html_node import markdown_to_html_node

class TestMDtoHTMLNode(unittest.TestCase):
    def test_parent(self):
        text = '''\
        # This is the heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        ```here is a block of code```
        
        >time for a qote
        >there are no chickens that hatch at night
        >you must become a night
        
        * here is a list item
        - with another list item
        
        1. here is ordered list
        2. another ordered list'''
    
        return markdown_to_html_node(textwrap.dedent(text))
if __name__ == "__main__":
    unittest.main()

