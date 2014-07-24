import unittest


class TemplateTestCase(unittest.TestCase):
    def flatten_text(self, element):
        text = element.text or ""
        for child in element:
            text += self.flatten_text(child)
        return text
