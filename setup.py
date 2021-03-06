from setuptools import setup,find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='cxit',
  packages = find_packages(),
  version='1.0.3',
  author='Aadhitya A',
  author_email='aadhitya864@gmail.com',
  description = 'A CLI tool to create CPP files for any contest',
  long_description = long_description,
  long_description_content_type="text/markdown",
  license = 'MIT License',
  py_modules=['codeit'],
  url="https://github.com/Arch2x/codeit",
  classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ),
  python_requires='>=3.5',
  include_package_data = True,
  install_requires=[
    'clint'
  ],
  entry_points={
    'console_scripts': [
      'codeit = codeit.codeit:main'
    ]
  }
)
