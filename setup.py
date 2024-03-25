from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Pipelines used in common scrapy projects"
LONG_DESCRIPTION = "A collection of pipelines used in common scrapy projects."

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="common-pipes",
    version=VERSION,
    author="Chase Hampton",
    author_email="chase.hampton@protonmai.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "scrapy>=2.11",
        "pyyaml",
        "unidecode",
    ],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
