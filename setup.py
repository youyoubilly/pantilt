from setuptools import setup, find_packages

setup(
    name='pantilt', 
    version='1.0.0', 
    packages=['utils'],
    description='A pantilt control utility',
    author='Billy Wang, Kevin Peng, Shawn Ling',
    url='https://github.com/youyoubilly/pantilt',
    keywords=['pan tilt', 'servo control'],
    install_requires=['Adafruit_PCA9685'
                    ],
)