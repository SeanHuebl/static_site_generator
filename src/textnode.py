class TextNode():
    def __init__(self, text_type, text, url=None, alt_text=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        self.alt_text = alt_text

    def __eq__(self, other):
        if (self.text, self.text_type, self.url, self.alt_text) == (other.text, other.text_type, other.url, other.alt_text):
            return True
        return False
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url}, {self.alt_text})"