from docxtpl import DocxTemplate
from io import BytesIO

class TemplateReader:
    def __init__(self, template):
        self.template = template

    def load_template(self):
        with open(self.template, "rb") as f:
            doc = DocxTemplate(BytesIO(f.read()))

        return doc