from setuptools import find_packages,setup

from typing import List

setup(
    name= "fraud_detection",
    version= "0.0.1",
    author= "Ganesh Jadhav",
    author_email= "grjadhav409@gmail.com",
    description= "A package to detect fraudulent transactions",
    packages=find_packages(),
    # install_requires=[
    #     "pandas",
    #     "numpy",
    #     "scikit-learn",
    #     "matplotlib",]      # requirements.txt is already created
)


