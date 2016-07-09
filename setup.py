from setuptools import setup, find_packages
from train import __version__

setup(
    name='train_12306',
    version=__version__,
    packages=find_packages(),
    author='ecmadao',
    author_email='wlec@outlook.com',
    url='https://github.com/ecmadao/Spider-12306',
    description='simple python application to get 12306 tickets',
    platforms='any',
    install_requires=[
        'prettytable',
        'Click'
    ],
    entry_points={
        'console_scripts': ['train=train.__main__:main']
    },
    license='MIT',
    py_modules=['run'],
    include_package_data=True
)
