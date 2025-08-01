from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="anime_recommender",
    version="0.1",
    author="di hao ambalabu",
    packages=find_packages(),
    install_requires = requirements,
)