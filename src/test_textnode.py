import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node, node2)
        
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Italic)
        self.assertNotEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", TextType.Bold, None)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")
        
    def test_url_not_none(self):
        node = TextNode("This is a text node", TextType.Bold, "https://www.google.com")
        self.assertIsNotNone(node.url)
        
if __name__ == "__main__":
    unittest.main()