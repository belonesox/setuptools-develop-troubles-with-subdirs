#!/usr/bin/env python
'''
sudo python setup.py develop
    
then in 
/usr/lib/python2.7/site-packages/easy-install.pth

we see directory of setup.py 
..../why-python-setup-develop-incorrect-with-subdirs
but not actual packages  directory
..../why-python-setup-develop-incorrect-with-subdirs/src/
'''

from setuptools import setup, find_packages
setup(
    name="realdemopackage",
    version='1.0.0',
    package_dir={
        'realdemopackage': 'src/realdemopackage', # Realpackages subdirectories of src
    },
    packages=find_packages('src'),
)
