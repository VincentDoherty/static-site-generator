from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")

        html = f"<{self.tag}{self.props_to_html()}>"
        if self.children:
            for child in self.children:
                html += child.to_html()
        html += f"</{self.tag}>"
        return html

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"