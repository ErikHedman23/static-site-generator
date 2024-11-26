import unittest

from textnode import TextNode, TextType
from utility import text_node_to_html_node
from leafnode import LeafNode

class TestUtility(unittest.TestCase):

    def test_text_node_to_html_node(self):
        text_node = TextNode("This is a text node", TextType.Bold)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_text_node_to_html_node_no_text(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode(None, TextType.Bold))
            
    def test_text_node_to_html_node_no_text_type(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("This is a text node", None))
        
    def test_text_node_to_html_node_unsupported_text_type(self):
        invalid_text_type = type('TextType', (object,), {'value': 'unknown'})
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("This is a text node", invalid_text_type))
        
if __name__ == "__main__":
    unittest.main()