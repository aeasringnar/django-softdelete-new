import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-softdelete-new',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A simple Python package can provide soft deletion function for Django.',
    long_description=README,
    url='https://github.com/aeasringnar/django-softdelete-new',
    author='Aeasringnar',
    author_email='Aeasringnar@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
