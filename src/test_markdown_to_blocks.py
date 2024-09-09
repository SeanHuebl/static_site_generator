import unittest

from markdown_to_blocks import block_to_block_type, BlockType, markdown_to_blocks

class TestExtract(unittest.TestCase):

    def test_blocks(self):
        """Test the splitting of markdown text into blocks."""
        text = '# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        expected_blocks = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        self.assertEqual(markdown_to_blocks(text), expected_blocks)

    def test_excessive_newline(self):
        """Test handling of excessive newlines in markdown text."""
        text = '# This is a heading\n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        expected_blocks = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        self.assertEqual(markdown_to_blocks(text), expected_blocks)

    def test_blank_text(self):
        """Test that markdown_to_blocks raises a ValueError for blank text input."""
        text = ''
        with self.assertRaises(ValueError):
            markdown_to_blocks(text)

    def test_block_to_block_type(self):
        """Test classification of markdown blocks into their types."""
        # Test different markdown block types
        self.assertEqual(block_to_block_type('##### Heading'), BlockType.H5)
        self.assertEqual(block_to_block_type('>quote\n>hello'), BlockType.QUOTE)
        self.assertEqual(block_to_block_type('```code block```'), BlockType.CODE)
        self.assertEqual(block_to_block_type('* part of an unordered list'), BlockType.LIST_UNORDERED)
        self.assertEqual(block_to_block_type('- uo list #2'), BlockType.LIST_UNORDERED)
        self.assertEqual(block_to_block_type('1. ordered list\n2. list2\n3. list3'), BlockType.LIST_ORDERED)
        self.assertEqual(block_to_block_type('this is just a paragraph'), BlockType.PARAGRAPH)
        
        # Test for errors with incorrect block formatting
        with self.assertRaises(ValueError):
            block_to_block_type('* list started\n next line doesnt have correct format')
        with self.assertRaises(ValueError):
            block_to_block_type('``` no delimiter at end')
        with self.assertRaises(ValueError):
            block_to_block_type('1. o \n3. o')

if __name__ == "__main__":
    unittest.main()
