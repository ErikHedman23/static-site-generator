from textnode import TextNode, TextType

def main():
    textnode = TextNode("Text node", TextType.Normal, "https://www.google.com")
    print(textnode)
if __name__ == "__main__":
    main()