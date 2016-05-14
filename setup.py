import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages


setup(
    name="recomend",
    version="0.1.0",
    author="Dmitry A. Paramonov",
    author_email="asmatic075@gmail.com",
    packages=find_packages(
        exclude=[
            "*test*",
            "*build*",
            "*__pycache__*"
        ]
    ),
    include_package_data=True,
    description="Recomendation engine"
)
