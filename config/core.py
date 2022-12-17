from pathlib import Path
import configparser
import modeling
ROOT = Path(modeling.__file__).resolve().parent
PACKAGE_ROOT = ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.ini"


# Method to read config file settings
def read_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)
    return config
