from setuptools import setup, find_packages

with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(

    name="MHDdatalearn",
    version="1.0.0",
    author="Samuel Simon, Yan, Kris",
    author_email="ns650@exter.ac.uk, ky297@exeter.ac.uk, kjb230@exeter.ac.uk, simon.wellesley-miller@nhs.net",
    url="https://github.com/N-Sam/MhDataLearn",
    descriptions="This package helps you to select the best classification model Algorithm in sklearn librarry ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["calculate", "clean", "load",
                "process", "model_selector", "prediction"],
    packages=find_packages(include=["mhdatalearn", "mhdatalearn.*"]),
    # package_dir={'': 'mdatalearn'}
    install_requires=[
        'numpy>=1.14.0',
        'pandas>=1.0.0',
        'matplotlib>=3.2.0',
        'seaborn>=0.9.1',
        'sklearn>=1.0.0'
    ],
    classifiers=[
        "Development status:: Executable",
        "Intended ODience: Data Scientist",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License V2 or Latter (GPLv2+)",
        "Operating System :: OS independent",

    ],

    extras_require={
        "dev": [
            "python>=3.8",
            "sklearn>=1.0.0",
            "seaborn>=0.9.1",
            "pandas>=1.14.0",
            "matplotlib>=3.2.0",
            "unittest>=3.7"
        ],
    },

)
