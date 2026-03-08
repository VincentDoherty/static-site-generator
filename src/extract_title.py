def extract_title(markdown_text):
    if not markdown_text.startswith("# "):
        raise ValueError("The supplied markdown does not lead with # and a space for h1 heading")
    return markdown_text[2:] 