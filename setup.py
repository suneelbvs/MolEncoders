from platform import release
from setuptools import setup, find_packages

setup(
    name="molencoder",
    version="0.1.0",
    release="July'2024",
    packages=find_packages(),
    install_requires=[
        "rdkit",
        "numpy",
        "selfies",
        "torch"
    ],
    author="Suneel Kumar BVS, Ph.D.,",
    author_email="suneelkumar.bvs@gmail.com",
    description="A package for molecular representations and encodings",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/suneelbvs/molencoder",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)