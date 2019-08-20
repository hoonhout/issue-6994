"""Package setup."""
from setuptools import setup, find_packages

setup(
    name="issue-6994",
    packages=find_packages(),
    install_requires=["pytest", "pytest-cov", "pytest-black", "pylama"],
)
