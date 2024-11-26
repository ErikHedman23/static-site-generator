import unittest 

from parentnode import ParentNode

from htmlnode import HTMLNode

from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_repr(self):
        node = ParentNode("div", [HTMLNode("div", "This is a div", None, None)], {"class": "my-class", "id": "my-id"})
        self.assertEqual(repr(node), "ParentNode(div, [HTMLNode(div, This is a div, None, None)], {'class': 'my-class', 'id': 'my-id'})")
        
    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [HTMLNode("div", "This is a div", None, None)], None).to_html()
        
    def test_to_html_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None, None).to_html()
        
    def test_to_html_no_children_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, None, None).to_html()
        
    def test_to_html_props(self):
        node = ParentNode("div", [LeafNode("div", "This is a div", None)], {"class": "my-class", "id": "my-id"})
        self.assertEqual(node.to_html(), "<div class=\"my-class\" id=\"my-id\"><div>This is a div</div></div>")
        
    def test_to_html_props_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [HTMLNode("div", "This is a div", None, None)], {"class": "my-class", "id": "my-id"}).to_html()
        
    def test_children_to_html(self):
        node = ParentNode("div", [LeafNode("div", "This is a div", None), LeafNode("div", "This is another div", None)], None)
        self.assertEqual(node.children_to_html(), "<div>This is a div</div><div>This is another div</div>")
        
    def test_nested_parent_node_to_html(self):
        child1 = LeafNode("div", "This is a div", None)
        child2 = LeafNode("div", "This is a div", None)
        node = ParentNode("div", [child1, child2], None)
        self.assertEqual(node.to_html(), "<div><div>This is a div</div><div>This is a div</div></div>")
        
if __name__ == "__main__":
    unittest.main()
