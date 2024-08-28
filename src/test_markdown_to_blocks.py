import unittest

from enums import BlockType
from markdown_to_blocks import markdown_to_blocks, block_to_block_type

class TestExtract(unittest.TestCase):
    def test_blocks(self):
        text = '# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        #markdown_to_blocks(text)
    def test_excessive_newline(self):
        text = '# This is a heading\n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        #markdown_to_blocks(text)
    def test_blank_text(self):
        text = ''
        with self.assertRaises(ValueError):
            markdown_to_blocks(text)
    def test_block_to_block_type(self):
        #text = '##### Heading'
        #text = '>quote\n>hello'
        #text = '```code block```'
        #text = '* part of an unordered list'
        #text = '- uo list #2'
        #text = '1. ordered list\n2. list2\n3. list3'
        #text = 'this is just a paragraph'
        with self.assertRaises(ValueError):
            block_to_block_type('* list started\n next line doesnt have correct format')
        with self.assertRaises(ValueError):
            block_to_block_type('``` no delimiter at end')
        with self.assertRaises(ValueError):
            block_to_block_type('1. o \n3. o')
        #print(block_to_block_type(text))
    
if __name__ == "__main__":
    unittest.main()