from setuptools import find_packages, setup
from typing import List

E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    """this function will return list of requirements

    Args:
        file_path (str): file path of the requirements text file

    Returns:
        List[str]: list of packages to be loaded 
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if E_DOT in requirements:
            requirements.remove(E_DOT)
            
    return requirements

setup(
    name = 'end to end machine learning' ,
    version = '0.0.1',
    author = 'Sameer Ahad',
    author_email = 'sameer.ahad@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)