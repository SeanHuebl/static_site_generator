import unittest

from text_to_textnodes import text_to_textnodes

class TestSplitNode(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) with a [superlink](https://github.com)[link2](https://link2.com)[link4](https://extra.com) end text"
        #return text_to_textnodes(text)
if __name__ == "__main__":
    unittest.main()