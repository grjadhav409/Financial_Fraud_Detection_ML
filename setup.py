from setuptools import find_packages,setup

from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    return requirement_list


setup(
    name= "fraud_detection",
    version= "0.0.1",
    author= "Ganesh Jadhav",
    author_email= "grjadhav409@gmail.com",
    description= "A package to detect fraudulent transactions",
    packages=find_packages(),
    install_requires=get_requirements(),   
)


