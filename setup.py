from setuptools import setup
import dashbar

def getLongDescription():
    with open("README.md", 'r') as f:
        return f.read()

setup(
    name="dashbar",
    author=dashbar.__author__,
    maintainer=dashbar.__author__,
    version=dashbar.__version__,
    python_requires=">=3.7",
    license="MIT",
    url="https://github.com/xyzpw/dashbar/",
    description=dashbar.__description__,
    long_description=getLongDescription(),
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
    ],
    long_description_content_type="text/markdown",
)
