import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'future'
]
test_requirements = [
    'future',
    'pytest'
]

setuptools.setup(
    name="geolib",
    version="1.0.5",
    author="Anu Joy",
    author_email="oss@cartographix.org",
    description="A library for geohash encoding, decoding and associated functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joyanujoy/geolib",
    packages=setuptools.find_packages(),
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=requires,
    tests_require=test_requirements,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
