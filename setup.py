from gettext import install
from setuptools import setup,find_packages
from typing import List
from housing.logger import logging
NAME = "ML_Project"
VERSION = "0.0.1"
AUTHOR = "Yaseer"
DESCRIPTION = "This is a self made project"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements_list():
    '''
    This function will read the contents of requirements.txt file
    i.e., all packages and returns it as a strig List
    '''
    with open(REQUIREMENTS_FILE_NAME) as rf:
        return rf.readlines().remove("-e .")
setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires = get_requirements_list()
)
