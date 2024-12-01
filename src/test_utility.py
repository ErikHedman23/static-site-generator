import unittest

from textnode import TextNode, TextType
from utility import text_node_to_html_node as text_node_to_html_node, split_nodes_delimiter as split_nodes_delimiter
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
            
    def test_split_nodes_delimiter_no_old_nodes(self):
        with self.assertRaises(TypeError):
            split_nodes_delimiter(None, "**", TextType.Bold)
            
    def test_split_nodes_delimiter_no_delimiter(self):
        with self.assertRaises(TypeError):
            split_nodes_delimiter([], None, TextType.Bold)
            
    def test_split_nodes_delimiter_no_text_type(self):
        with self.assertRaises(TypeError):
            split_nodes_delimiter([], "**", None)
            
    def test_split_nodes_delimiter_unsupported_text_type(self):
        with self.assertRaises(TypeError):
            split_nodes_delimiter([], "**", type('TextType', (object,), {'value': 'unknown'}))
            
    def test_split_nodes_delimiter(self):
    # Only include nodes relevant to each test
        bold_nodes = [
            TextNode("This **is bold** text", TextType.Bold)
        ]
        italic_nodes = [
            TextNode("This *is italic* text", TextType.Italic)
        ]
        code_nodes = [
            TextNode("This `is code` text", TextType.Code)
        ]
    
        expected_nodes_bold = [
            TextNode("This ", TextType.Text),
            TextNode("is bold", TextType.Bold),
            TextNode(" text", TextType.Text),
        ]

        expected_nodes_italic = [
            TextNode("This ", TextType.Text),
            TextNode("is italic", TextType.Italic),
            TextNode(" text", TextType.Text),
        ]
    
        expected_nodes_code = [
            TextNode("This ", TextType.Text),
            TextNode("is code", TextType.Code),
            TextNode(" text", TextType.Text),
        ]

        actual_nodes = split_nodes_delimiter(bold_nodes, "**", TextType.Bold)
        self.assertEqual(actual_nodes, expected_nodes_bold)
    
        actual_nodes = split_nodes_delimiter(italic_nodes, "*", TextType.Italic)
        self.assertEqual(actual_nodes, expected_nodes_italic)
    
        actual_nodes = split_nodes_delimiter(code_nodes, "`", TextType.Code)
        self.assertEqual(actual_nodes, expected_nodes_code)
        
        #this is a test comment
        
        
        
if __name__ == "__main__":
    unittest.main()