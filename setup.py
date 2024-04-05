from setuptools import setup
import dashbar


with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="dashbar",
    author=dashbar.__author__,
    maintainer=dashbar.__author__,
    version=dashbar.__version__,
    python_requires=">=3.7",
    license="MIT",
    url="https://github.com/xyzpw/dashbar/",
    description=dashbar.__description__,
    long_description=readme,
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Environment :: Console :: Curses",
        "Environment :: Console",
    ],
    long_description_content_type="text/markdown",
)
