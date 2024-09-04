import unittest

from generate_page import extract_title, generate_page

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        text = '# this is the title'
        text2 = 'this should throw an exception'
        #print(extract_title(text))
        with self.assertRaises(Exception):
            extract_title(text2)

    def test_generate_page(self):

        generate_page('./content/index.md', './template.html', './public/index.html')
if __name__ == "__main__":
    unittest.main()