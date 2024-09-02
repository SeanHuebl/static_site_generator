import textwrap
import unittest

from markdown_to_html_node import markdown_to_html_node

class TestMDtoHTMLNode(unittest.TestCase):
    def test_parent(self):
        text = '''\
        # This is the heading

        ### Here is a big heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        ```
        def my_function():
            x = 0
            for i in range(9):
                print('hello')
        ```
        
        >time for a quote
        >there are no chickens that hatch at night
        >you must become a night
        
        * here is a list item
        - with another list item
            that is multiline
            and another line
            
        1. here is ordered list
        2. another ordered list
            with a new line'''
    
        print(markdown_to_html_node(textwrap.dedent(text)))
if __name__ == "__main__":
    unittest.main()

