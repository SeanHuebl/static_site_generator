import unittest

from extract import extract_markdown_images, extract_markdown_links

class TestExtract(unittest.TestCase):

    def test_img_link(self):
        """Test extraction of Markdown image links."""
        input_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_output = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        # Use assertEqual to check if the extracted images match the expected output
        self.assertEqual(extract_markdown_images(input_text), expected_output)

    def test_url_link(self):
        """Test extraction of Markdown URL links."""
        input_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdev)"
        expected_output = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdev")
        ]
        # Use assertEqual to check if the extracted URLs match the expected output
        self.assertEqual(extract_markdown_links(input_text), expected_output)

if __name__ == "__main__":
    unittest.main()