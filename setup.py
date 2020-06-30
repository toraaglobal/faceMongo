# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:15:06 2020

@author: teeja
"""


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="faceMongo-toraaglobal", 
    version="0.0.1",
    author="Tajudeen Abdulazeez",
    author_email="toabdula@syr.edu",
    description="Scrape facebook public page to mongo database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toraaglobal/faceMongo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)