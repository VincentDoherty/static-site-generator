from textnode import TextNode, Texttype 

def main():
    node = TextNode("Hello, World!", Texttype.PLAIN)
    print(node)
    
main()