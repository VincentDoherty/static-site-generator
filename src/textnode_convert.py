from textnode import TextNode, TextType
from leafnode import LeafNode
from split_nodes_deliminator import split_nodes_delimiter, split_nodes_markdown_images, split_nodes_markdown_links

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("Link TextNode must have a URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("Image TextNode must have a URL")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")
    
def text_to_textnodes(text):
    chain = [TextNode(text,TextType.TEXT)]
    chain = split_nodes_delimiter(chain,"`",TextType.CODE)
    chain = split_nodes_delimiter(chain,"**",TextType.BOLD)
    chain = split_nodes_delimiter(chain,"_",TextType.ITALIC)
    chain = split_nodes_markdown_images(chain)
    chain = split_nodes_markdown_links(chain)

    return chain