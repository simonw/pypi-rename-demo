from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="pypy-rename-demo",
    description="pypy-rename-demo is now sqlite-utils",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    version=VERSION,
    install_requires=["sqlite-utils"],
    classifiers=["Development Status :: 7 - Inactive"],
)
