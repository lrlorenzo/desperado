import os

class FolderReader:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def list_files(self):
        
        return [
            os.path.join(self.folder_path, f)
            for f in os.listdir(self.folder_path)
            if os.path.isfile(os.path.join(self.folder_path, f)) and f.lower().endswith('.xlsx')
        ]
