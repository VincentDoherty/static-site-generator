import re

from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid markdown syntax: missing closing delimiter {delimiter}")

        for i, part in enumerate(parts):
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

def split_nodes_markdown_images(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        for alt, url in images:
            image_markdown = f"![{alt}]({url})"
            sections = text.split(image_markdown, 1)

            if len(sections) != 2:
                raise ValueError("Invalid markdown image syntax")

            before, text = sections

            new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_markdown_links(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        current_text = node.text
        for link_text, url in links:
            parts = current_text.split(f"[{link_text}]({url})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            current_text = parts[1] if len(parts) > 1 else ""
        
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes
