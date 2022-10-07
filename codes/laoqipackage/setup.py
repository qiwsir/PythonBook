import setuptools
import os
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))  #①
with open("README.md", "r") as fh:  #②
    long_description = fh.read()
setuptools.setup(
    name="laoqipackage",  
    version="1.0.0",
    author="laoqi", 
    author_email="qiwsir@gmail.com",
    description="You can listen the speaking of programming language.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    py_modules = ['langspeak',],
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ),
    )