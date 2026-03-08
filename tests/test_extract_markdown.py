import unittest
from src.extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "Here is an image: ![alt text](image.jpg) and another one ![another image](another_image.png)"
        expected = [("alt text", "image.jpg"), ("another image", "another_image.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = "Here is a link: [Google](https://www.google.com) and another one [GitHub](https://www.github.com)"
        expected = [("Google", "https://www.google.com"), ("GitHub", "https://www.github.com")]
        self.assertEqual(extract_markdown_links(text), expected)
        
if __name__ == "__main__":
    unittest.main()