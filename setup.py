# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='pyqt_led',
      version='0.0.2',
      description='Simple LED widget for PyQt5',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/Neur1n/pyqt_led',
      author='Jihang Li',
      author_email='Jihang.Li@outlook.com',
      license='MIT',
      packages=['pyqt_led'],
      install_requires=['numpy'],
      zip_safe=False)
