from textnode import TextNode
from enums import TextType


def main():
    first_node = TextNode("Hello", TextType.BOLD, "www.boot.dev")
    print(first_node)


if __name__ == "__main__":
    main()