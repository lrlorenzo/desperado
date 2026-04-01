import logging
import time
from reader.folder_reader import FolderReader
from reader.template_reader import TemplateReader
from reader.input_reader import InputReader
from writer.document_generator import DocumentGenerator

_logger = logging.getLogger(__name__)

class ResumeGenerator:
    def __init__(self, template, input_folder, header, dtypes, output_folder, pooling_delay: float):
        self.template = template
        self.input_folder = input_folder
        self.header = header
        self.dtypes = dtypes
        self.output_folder = output_folder
        self.pooling_delay = pooling_delay

    def generate_resumes(self):
        _logger.info("Generating resumes using template: %s and input folder: %s", self.template, self.input_folder)

        folder_reader = FolderReader(self.input_folder)
        template_reader = TemplateReader(self.template)
        template = template_reader.load_template()
        document_generator = DocumentGenerator(template=template, output_folder=self.output_folder)

        while True:
            try:
                _logger.debug("Checking for new input data in folder: %s", self.input_folder)
                files = folder_reader.list_files()
                file_count = len(files)
                if file_count > 0:
                    _logger.info("Found %d new input file(s). Processing...", file_count)
                    for file in files:
                        _logger.debug("Processing file: %s", file)
                        input_reader = InputReader(file_path=file,
                                                   header=self.header,
                                                   dtypes=self.dtypes,
                                                   parse_dates=None)
                        df = input_reader.read()
                        _logger.debug(f"DataFrame shape: {df.shape} Columns: {df.columns.tolist()}")
                        for row in df.itertuples(index=True, name="Row"):                          
                            _logger.debug(f"Processing row: {row.Index} {row.First_Name} {row.Last_Name}")
                            skills_list = [s.strip() for s in row.Technical_Skills.splitlines() if s.strip()]
                            tech_skills_chunk = self.chunk_list(skills_list, 3)

                            certifications_list = [c.strip() for c in row.Certifications.splitlines() if c.strip()]

                            data = {
                                "First_Name": row.First_Name,
                                "Last_Name": row.Last_Name,
                                "Job_Title": row.Job_Title,
                                "Phone_Number": row.Phone_Number,
                                "Email_Address": row.Email_Address,
                                "Address": row.Address,
                                "Summary": row.Summary,
                                "Job_Title1": row.Job_Title1,
                                "Job_Company1": row.Job_Company1,
                                "Job_Employement_Date1": row.Job_Employement_Date1,
                                "Job_Summary1": row.Job_Summary1,
                                "Job_Title2": row.Job_Title2,
                                "Job_Company2": row.Job_Company2,
                                "Job_Employement_Date2": row.Job_Employement_Date2,
                                "Job_Summary2": row.Job_Summary2,
                                "Job_Title3": row.Job_Title3,
                                "Job_Company3": row.Job_Company3,
                                "Job_Employement_Date3": row.Job_Employement_Date3,
                                "Job_Summary3": row.Job_Summary3,
                                "Job_Title4": row.Job_Title4,
                                "Job_Company4": row.Job_Company4,
                                "Job_Employement_Date4": row.Job_Employement_Date4,
                                "Job_Summary4": row.Job_Summary4,
                                "Job_Title5": row.Job_Title5,
                                "Job_Company5": row.Job_Company5,
                                "Job_Employement_Date5": row.Job_Employement_Date5,                                
                                "Job_Summary5": row.Job_Summary5,
                                "Education": row.Education,
                                "Certifications": certifications_list,
                                "Technical_Skills": tech_skills_chunk
                                }
                            
                            document_generator.generate_document(data)



                _logger.debug("No new input data found. Waiting for %s seconds before checking again.", self.pooling_delay)
                time.sleep(self.pooling_delay)
            except KeyboardInterrupt:
                _logger.warning("Application interrupted by user.")
                break

        _logger.info("Resume generation process has been stopped.")

    def chunk_list(self, data, size=3):
        _logger.debug(f"Chunking data: {data} into size: {size}")
        return [data[i:i + size] for i in range(0, len(data), size)]