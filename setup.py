import sys
from setuptools import setup, find_packages
from codecs import open
from os import path
from subprocess import Popen, PIPE

if sys.version_info < (2,7) or sys.version_info >= (3,0):
   sys.exit("Error: You are using Python "+str(sys.version_info)+"; Python3 and Python 2.6 and below are not supported. Please use 2.7.X\n")
try:
  cmd = 'Rscript --version'
  p = Popen(cmd.split(),stderr=PIPE,stdout=PIPE)
  v = p.communicate()[1]
  #if v[0] != 'R':
  #   sys.exit("Unexpected R problem.  has been tested with R 3.4\n")
except:
  sys.exit("Error: You need R installed so that the Rscript command is in the path\n")

this_folder = path.abspath(path.dirname(__file__))
with open(path.join(this_folder,'README.md'),encoding='utf-8') as inf:
  long_description = inf.read()

setup(
  name='AlignQC',
  version='1.3.0',
  description='Python tools for working with biological sequence data',
  long_description=long_description,
  url='https://github.com/jason-weirather/AlignQC',
  author='Jason L Weirather',
  author_email='jason.weirather@gmail.com',
  license='Apache License, Version 2.0',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'License :: OSI Approved :: Apache Software License'
  ],
  keywords='bioinformatics, sequence, alignment',
  packages=['alignqc'],
  install_requires = ['seq-tools==1.0.0',
                     ],
  entry_points = {
    'console_scripts':['alignqc=alignqc.alignqc:main']
  }
)
  
