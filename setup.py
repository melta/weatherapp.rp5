from setuptools import setup, find_namespace_packages

setup(
    name='weatherapp.rp5',
    version='0.1.0',
    author='Taras Melnychuk',
    description="rp5 provider",
    long_descriptoin="",
    packages=find_namespace_packages(),
    entry_points={
        'weatherapp.provider': 'rp5=weatherapp.rp5.provider:RP5Provider',
    },
    install_requires=[
        'bs4'
    ]
)
