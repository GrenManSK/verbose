from setuptools import setup
from setuptools import find_packages
from verbose import VERSION, AUTHOR

setup(
    name="verbose",
    version=VERSION,
    description="verbose",
    author=AUTHOR,
    packages=find_packages(exclude=("tests*", "testing*")),
)
