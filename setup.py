#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-valet-keys',
    version='0.0.2',
    description='Django app for managing valet keys for robots',
    long_description=open('README.rst').read(),
    author='Les Orchard',
    author_email='me@lmorchard.com',
    url='http://github.com/lmorchard/django-valet-keys',
    license='MPL',
    packages=find_packages(exclude=['valet_keys_example*']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'django>=1.4',
    ],
    tests_require=[
        'nose',
        'django-nose',
        'pyquery',
        'feedparser',
    ],
    test_suite='manage.nose_collector',
)
