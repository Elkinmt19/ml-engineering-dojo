from setuptools import setup, find_packages

# Get README.md long description to add it to the builded package
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(

    # Library name (same as "pip install ____")
    name='time_series_forecasting',

    author='Elkin Javier Guerra Galeano',

    author_email='elkinmt19@gmail.com',

    # Package version (MAJOR_VERSION.MINOR_VERSION.MAINTENANCE_VERSION)
    version='0.0.1',

    url="https://github.com/Elkinmt19/data-science-dojo",

    # Simple package description
    description= "This is a time series module implemented using Tensorflow and Pandas.",

    # Long package description
    long_description=long_description,
    long_description_content_type="text/markdown",

    # Define the package's structure
    packages=find_packages(),

    # Add library dependencies
    install_requires=[
        "numpy",
        "matplotlib",
        "pandas",
        "tensorflow"
    ],

    # Add devlopment dependencies
    extras_require={
        "dev": [
            "pytest",
        ],
    },

    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],

    license="MIT License",

    # Add extra XML and JSONs needed
    include_package_data=True
)