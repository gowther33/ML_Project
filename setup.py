"""
This file enables us to create our project(application) as a python package and we can also deploy it on PyPI
The Python Package Index, abbreviated as PyPI and also known as the Cheese Shop, is the official third-party software repository for Python. 
It is analogous to the CPAN repository for Perl and to the CRAN repository for R. PyPI is run by the Python Software Foundation, a charity.
"""

from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function returns a list of requirement packages
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove .\n 
        requirements = [req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Hanan',
    author_email='hananjohn111@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)