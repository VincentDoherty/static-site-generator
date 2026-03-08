import unittest
from src.textnode_convert import text_node_to_html_node, text_to_textnodes
from src.textnode import TextNode, TextType

class TestTextNodeConvert(unittest.TestCase):
    
    def test_plain_text_node(self):
        text_node = TextNode("Hello, World!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Hello, World!")
    
    def test_bold_text_node(self):
        text_node = TextNode("Bold Text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold Text</b>")
    
    def test_italic_text_node(self):
        text_node = TextNode("Italic Text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic Text</i>")
    
    def test_code_text_node(self):
        text_node = TextNode("Code Snippet", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code Snippet</code>")
    
    def test_link_text_node(self):
        text_node = TextNode("Google", TextType.LINK, url="https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">Google</a>')
    
    def test_image_text_node(self):
        text_node = TextNode("Alt Text", TextType.IMAGE, url="https://example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://example.com/image.png" alt="Alt Text" />')
    
    def test_link_text_node_without_url(self):
        text_node = TextNode("Broken Link", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)
    
    def test_image_text_node_without_url(self):
        text_node = TextNode("Broken Image", TextType.IMAGE)
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_text_to_textnodes(self):
        text = "This is **bold** and this is _italic_ and this is `code` and this is an ![image](https://i.imgur.com/zjjcJKZ.png) and this is a [link](https://www.example.com)"
        text_nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and this is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and this is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.example.com"),
        ]
        self.assertEqual(text_nodes, expected)
        
if __name__ == "__main__":
    unittest.main()