from setuptools import setup

with open("README.md", 'r') as f:
    description=f.read()

setup(
    name="dashbar",
    author="xyzpw",
    maintainer="xyzpw",
    version="1.0",
    url="https://github.com/xyzpw/dashbar/",
    description="A progress-bar designed to be useful and easy to use.",
    long_description=description,
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
    ],
    long_description_content_type="text/markdown",
)
