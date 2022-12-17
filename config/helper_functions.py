from config.core import read_config
from pathlib import Path
import modeling
import os

# Project Directories
PACKAGE_ROOT = Path(modeling.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
DATASET_DIR = ROOT / "datasets"
TRAINED_MODEL_DIR = ROOT / "modeling/saved_models"

config = read_config()

book_data_filename = config['Data Files']['book_data_file']
img_data_filename = config['Data Files']['img_data']

year_data_filename = config['Data Files']['year_data']
sales_data_filename= config['Data Files']['sales_data_file']

model_checkpoint_filename = config['Model checkpoint']['model_checkpoint']

def book_data_reading():
    return os.path.join(DATASET_DIR, book_data_filename), os.path.join(DATASET_DIR,img_data_filename)


def sales_data_reading():
    return os.path.join(DATASET_DIR, year_data_filename), os.path.join(DATASET_DIR, sales_data_filename)

def sales_model_file_reading():
    return os.path.join(TRAINED_MODEL_DIR, model_checkpoint_filename)

def sales_hyperparameter_dict():
    result_dict = dict(config.items('Time Series modeling'))
    result_dict = {k.upper(): v.upper() for k, v in result_dict.items()}
    return result_dict