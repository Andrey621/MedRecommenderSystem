#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Andrey",
    author_email='achernyavsky10@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Project for rec system",
    entry_points={
        'console_scripts': [
            'MedRecommenderSystem=MedRecommenderSystem.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='MedRecommenderSystem',
    name='MedRecommenderSystem',
    packages=find_packages(include=['MedRecommenderSystem', 'MedRecommenderSystem.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Andrey621/MedRecommenderSystem',
    version='1',
    zip_safe=False,
)
