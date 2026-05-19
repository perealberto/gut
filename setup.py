from setuptools import setup

setup(
    name="gut",
    version="0.0.1",
    packages=["src"],
    entry_points={"console_scripts": ["gut = src.cli:main"]},
)
