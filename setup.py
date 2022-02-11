#!/usr/bin/env python

from distutils.core import setup


setup(
    name="markdown2",
    version="0.0.1",
    maintainer="Laurent Meyer",
    maintainer_email="laurent@jobninja.com",
    author="Laurent Meyer",
    author_email="laurent@jobninja.com",
    url="https://github.com/laurentmmeyer",
    license="MIT",
    platforms=["any"],
    py_modules=["markdown2"],
    description="A wrapper around mistletoe",
    long_description="""A wrapper around mistletoe""",
    install_requires=['mistletoe>0.8']
)
