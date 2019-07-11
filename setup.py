import io
import os
import re

import setuptools


def read(path):
    file_path = os.path.join(os.path.dirname(__file__), *path.split('/'))
    return io.open(file_path, encoding='utf-8').read()


# single-sourcing the package version using method 1 of:
#   https://packaging.python.org/guides/single-sourcing-package-version/
def parse_version_from(path):
    version_file = read(path)
    version_match = re.search(r"^__version__ = '(.*)'", version_file, re.M)
    if version_match is None or len(version_match.groups()) > 1:
        raise ValueError("couldn't parse version")
    return version_match.group(1)


setuptools.setup(
    name='odyssey',
    version=parse_version_from('codyssey.py'),
    description='Python interface to odc for encoding/decoding ODB files'
    long_description=read('README.rst') + read('CHANGELOG.rst'),
    author='European Centre for Medium-Range Weather Forecasts (ECMWF)',
    author_email='software.support@ecmwf.int',
    license='Apache License Version 2.0',
    url='https://github.com/ecmwf/odyssey',
    packages=setuptools.find_packages(),
    include_package_data=True,
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'cffi',
    ],
    extras_require={},
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-flakes',
    ],
    test_suite='tests',
    zip_safe=True,
    keywords='odc odb',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ]
)
