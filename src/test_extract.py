import unittest

from extract import extract_markdown_images, extract_markdown_links


class TestExtract(unittest.TestCase):
    def test_img_link(self):
        #print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
        x = 0
    def test_url_link(self):
        #print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdev)"))
        x = 0
if __name__ == "__main__":
    unittest.main()