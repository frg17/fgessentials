import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fgdownload",
    version="0.0.3",
    author="Frosti",
    author_email="super@duper.secret",
    description="eztv download package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=".",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Windows 10"
    ],
)
