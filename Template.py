import os 
import logging 
from pathlib import Path 

# config for logging of project directories creation
logging.basicConfig(level=logging.INFO,format="[%(asctime)s : %(message)s]")

# list of files and folder required for project
list_of_files=[
    "src/__init__.py", 
    "src/helper.py", 
    "src/store_index.py", 
    "src/prompt.py", 
    "requirements.txt", 
    "app.py", 
    "setup.py",
    "research/exp.ipynb", 
    "templates/index.html", 
    "static/style.css"
]

# loop through list of files
for filepath in list_of_files: 
    filepath=Path(filepath)            
    file_dir,file_name=os.path.split(filepath)   # split file directory and file 

    # create file directory if not exists
    if file_dir != "": 
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"create {file_dir} sucessfully")

    # create file if not exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)): 
        with open(filepath,"w")as file: 
            pass 
            logging.info(f"create empty {file_name} for {file_dir}")
    
    # if file already exists
    else: 
        logging.info(f"{file_name} is already exists.....")

