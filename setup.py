from setuptools import setup

setup(
    name="dao_pymongo",
    packages=["dao_pymongo"],
    description="Implementation of DAO pattern for pymongo",
    version="0.1",
    url="https://github.com/lamasne/dao_pymongo",
    author="Neil",
    author_email="neillamas@gmail.com",
    install_requires=["requests", "numpy>=1.22.4", "pandas>=1.4.2", "pymongo>=4.1.1"],
)
