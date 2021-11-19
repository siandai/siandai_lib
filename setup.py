import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="siandai",
    version="0.0.1b2",
    author="Jaspreet Singh",
    description="An EDA & Modellling assist library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/siandai/siandai_lib",
    project_urls={
        "Bug Tracker": "https://github.com/siandai/siandai_lib",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires = [
    "scikit-learn >= 1.0.1" # carries numpy and scipy    
    ],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)