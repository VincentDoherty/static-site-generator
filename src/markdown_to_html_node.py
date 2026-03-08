from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from parentnode import ParentNode
from textnode_convert import text_node_to_html_node, text_to_textnodes
from textnode import TextNode, TextType


def markdown_to_html_node(text):
    blocks = markdown_to_blocks(text)
    children_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                leaf = create_html_paragraph_from_block(block)
                children_nodes.append(ParentNode("p",leaf))
            case BlockType.QUOTE:
                leaf = create_html_quote_block(block)
                children_nodes.append(ParentNode("blockquote",leaf))
            case BlockType.ORDERED_LIST:
                list_items = create_html_ordered_list(block)
                children_nodes.append(ParentNode("ol",list_items))
            case BlockType.UNORDERED_LIST:
                list_items = create_html_unordered_list(block)
                children_nodes.append(ParentNode("ul",list_items))
            case BlockType.CODE:
                blockHolder = create_html_code_block(block)
                children_nodes.append(blockHolder)
            case BlockType.HEADING:
                heading,leaf = create_html_heading_from_block(block)
                children_nodes.append(ParentNode(heading,leaf))
            
    root = ParentNode("div",children_nodes)
    return root

def create_html_paragraph_from_block(block):
    block = block.replace("\n"," ")
    text_nodes = text_to_textnodes(block)
    leaf = []
    for text_node in text_nodes:
        leaf.append(text_node_to_html_node(text_node))
    return leaf

def create_html_quote_block(block):
    lines = block.split("\n")
    block_text = lines[0][2:]
    for i in range(1,len(lines)):
        block_text += lines[i][1:]
    text_nodes = text_to_textnodes(block_text)
    leaf = []
    for text_node in text_nodes:
        leaf.append(text_node_to_html_node(text_node))
    return leaf

def create_html_code_block(block):
    block_text = block[4:-3]
    text_node = TextNode(block_text, TextType.TEXT)
    leaf = text_node_to_html_node(text_node)
    leaf.tag = "code"
    return ParentNode("pre",[leaf])

def create_html_ordered_list(block):
    lines = block.split("\n")
    list_items = []
    for line in lines:
        leaf_list = []
        text_nodes = text_to_textnodes(line.split(". ",1)[1])
        for text_node in text_nodes:
            leaf_list.append(text_node_to_html_node(text_node))
        list_items.append(ParentNode("li",leaf_list))
    return list_items

def create_html_unordered_list(block):
    lines = block.split("\n")
    list_items = []
    for line in lines:
        leaf_list = []
        text_nodes = text_to_textnodes(line[2:])
        for text_node in text_nodes:
            leaf_list.append(text_node_to_html_node(text_node))
        list_items.append(ParentNode("li",leaf_list))
    return list_items

def create_html_heading_from_block(block):
    block = block.replace("\n"," ")
    count = 0
    for c in range(0,6):
        if block[c] != "#":
            break
        count+=1
    heading = "h"+str(count)
    text_nodes = text_to_textnodes(block[count+1:])
    leaf = []
    for text_node in text_nodes:
        leaf.append(text_node_to_html_node(text_node))
    
    return heading,leaf