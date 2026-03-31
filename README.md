# desperado
Desperado: A resume generator for people aggressively seeking employment. Feed it a template, get a professionally formatted resume because desperation deserves good formatting.

## Getting started with desperado

Follow these steps to run the project locally:

---

### 1. Download the project
- Download or clone the repository  
- Extract the `.zip` file (if downloaded)  

---

### 2. Open a terminal in the project folder
Navigate to the folder where you extracted the files.

---

### 3. Create a virtual environment
```bash
python -m venv venv
```

---

### 4. Activate the virtual environment
- **Windows**
```bash
venv\scripts\activate
```

- **Mac/Linux**
```bash
source venv/bin/activate
```

---

### 5. Install dependencies
```bash
pip install -r requirements.txt
```

### 6. Run desperado
```bash
python main.py --template=TemplateA.docx
```

## ✅ Notes
- Make sure you have **Python installed (3.10+)**.
- Place your template file (e.g., 'TemplateA.docx') in the project folder.
- Place your input file (e.g., 'Sample.xlsx') in the project folder.
- You can modify the folders in the .env file.
- You can customize the template to generate your own resume.
