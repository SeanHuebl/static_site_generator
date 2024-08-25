import unittest
from textnode import TextNode
from text_to_textnodes import text_to_textnodes

class TestSplitNode(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        return text_to_textnodes(text)
if __name__ == "__main__":
    unittest.main()