import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", "This is a div", None, None)
        self.assertEqual(repr(node), "HTMLNode(div, This is a div, None, None)")
        
    # def test_to_html(self):
    #     node = HTMLNode("div", "This is a div", None, None)
    #     self.assertEqual(node.to_html(), "<div>This is a div</div>")
    
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div", None, {"class": "my-class", "id": "my-id"})
        self.assertEqual(node.props_to_html(), "class=\"my-class\" id=\"my-id\"")
        
    def test_has_tag(self):
        node = HTMLNode("div", "This is a div", None, None)
        self.assertTrue(node.tag != None)
        
if __name__ == "__main__":
    unittest.main()
