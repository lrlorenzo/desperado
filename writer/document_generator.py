import logging
import os
import uuid
from io import BytesIO

_logger = logging.getLogger(__name__)

class DocumentGenerator:
    def __init__(self, template, output_folder, output_file_prefix="CV"):
        self.template = template
        self.output_folder = output_folder
        self.output_file_prefix = output_file_prefix

    def generate_document(self, data):
            _logger.debug(f"Data for template rendering: {data}")

            output_file_docx = f"{self.output_file_prefix}_{data.get('Last_Name', 'Unknown')}_{data.get('First_Name', 'Unknown')}_{uuid.uuid4().hex}.docx"
            output_full_path_docx = os.path.join(self.output_folder, output_file_docx)

            self.template.render(data)  
            output_bytes = BytesIO()
            self.template.save(output_bytes)

            output_bytes.seek(0)
            with open(output_full_path_docx, "wb") as f:
                f.write(output_bytes.getvalue())