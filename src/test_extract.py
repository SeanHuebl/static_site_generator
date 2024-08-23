import unittest
from extract import *


class TestExtract(unittest.TestCase):
    def test_img_link(self):
        print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
    def test_url_link(self):
        print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdev)"))
if __name__ == "__main__":
    unittest.main()