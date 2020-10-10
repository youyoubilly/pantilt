from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pantilt', 
    version='0.0.2', 
    packages=find_packages(),
    description='A pantilt control utility',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Billy Wang, Kevin Peng, Shawn Ling',
    url='https://github.com/youyoubilly/pantilt',
    keywords=['pan tilt', 'servo control'],
    install_requires=['bcam','Adafruit_PCA9685'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)