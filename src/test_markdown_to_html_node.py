import textwrap
import unittest

from markdown_to_html_node import markdown_to_html_node, ParentNode, LeafNode

class TestMDtoHTMLNode(unittest.TestCase):

    def setUp(self):
        """Set maxDiff to None to see the full difference between generated and expected HTML."""
        self.maxDiff = None

    def test_parent(self):
        """Test conversion of Markdown to HTML nodes for various Markdown elements."""
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
     
        # Normalize input text by replacing tabs with four spaces and stripping excess whitespace
        normalized_text = textwrap.dedent(text).replace('\t', '    ')

        # Generate the HTML node structure from Markdown
        html_node = markdown_to_html_node(normalized_text)

        # Expected HTML structure for the given Markdown input
        expected_html = (
            "<div>"
            "<h1>This is the heading</h1>"
            "<h3>Here is a big heading</h3>"
            "<p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>"
            "<pre><code>\ndef my_function():\n"
            "   x = 0\n"
            "   for i in range(9):\n"
            "       print('hello')</code></pre>"
            "<blockquote>time for a quote<br>there are no chickens that hatch at night<br>you must become a night</blockquote>"
            "<ul><li>here is a list item</li><li>with another list item<br>that is multiline<br>and another line</li></ul>"
            "<ol><li>here is ordered list</li><li>another ordered list<br>with a new line</li></ol>"
            "</div>"
        )

        # Convert the HTML node structure to HTML and normalize whitespace
        generated_html = html_node.to_html().strip()
        print(generated_html)

        # Assert that the generated HTML matches the expected HTML after normalization
        self.assertEqual(generated_html, expected_html)

if __name__ == "__main__":
    unittest.main()
