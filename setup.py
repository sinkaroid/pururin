import re

from setuptools import setup


version = ''
with open('pururin/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)


requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()



if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.md') as f:
    readme = f.read()


setup(
    name='pururin',
    author='sinkaroid',
    author_email='anakmancasan@gmail.com',
    version='0.0.6',
    long_description=readme,
    url='https://github.com/sinkaroid/pururin',
    packages=['pururin'],
    license='MIT',
    description='Pururin unofficial API',
    include_package_data=True,
    keywords = ['pururin', 'doujin', 'wrapper'],
    install_requires=requirements
)