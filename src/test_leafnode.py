import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_repr(self):
        node = LeafNode("div", "This is a div", None)
        self.assertEqual(repr(node), "LeafNode(div, This is a div, None)")
        
    def test_to_html_no_props(self):
        node = LeafNode("div", "This is a div", None)
        self.assertEqual(node.to_html(), "<div>This is a div</div>")
        
    def test_to_html_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("div", None, None).to_html()
        
    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError):
            LeafNode(None, "This is a div", None).to_html()
        
    def test_to_html_no_tag_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode(None, None, None).to_html()
        
    def test_to_html_props(self):
        node = LeafNode("div", "This is a div", {"class": "my-class", "id": "my-id"})
        self.assertEqual(node.to_html(), "<div class=\"my-class\" id=\"my-id\">This is a div</div>")
        
    def test_to_html_props_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("div", None, {"class": "my-class", "id": "my-id"}).to_html()
        
    def test_to_html_props_no_tag(self):
        with self.assertRaises(ValueError):
            LeafNode(None, "This is a div", {"class": "my-class", "id": "my-id"}).to_html()
        
if __name__ == "__main__":
    unittest.main()