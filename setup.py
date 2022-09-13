from setuptools import setup
import setuptools

setup(
    name="python-aws-automation-tooling",
    version="1.0",
    url="https://github.com/msalman899/python-aws-automation-tooling.git",
    description="A Python wrapper package around AWS boto3 library to simplify interaction with AWS resources by providing pre-defined functions.",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        # "boto3==1.24.40",
        # "botocore==1.27.40",
    ]
)
