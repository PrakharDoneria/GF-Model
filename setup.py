import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gfmodel",
    version="1.0.0",
    author_email="prakhardoneria3@gmail.com",
    description="Simple Python client for GitHub Models API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prakhardoneria/gfmodel",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
