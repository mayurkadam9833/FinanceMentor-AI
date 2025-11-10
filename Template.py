import os 
import logging 
from pathlib import Path

logging.basicConfig(level=logging.INFO,format="[%(asctime)s : %(message)s]")


list_of_files=[
    "src/__init__.py",
    "src/helper.py",
    "src/store_index.py",
    "src/prompt.py", 
    "static/style.css", 
    "templates/index.html", 
    "app.py", 
    "setup.py", 
    "requirements.py", 
    "research/experiments.ipynb"
]

for file_path in list_of_files: 
    file_path=Path(file_path)
    file_dir,file_name=os.path.split(file_path)

    if file_dir != "": 
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"create {file_dir} for {file_name}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0): 
        with open(file_path,"w")as file: 
            pass 
            logging.info(f"create empty {file_name} at {file_path}")
    
    else: 
        logging.info(f"{file_path} is already exists.......")
