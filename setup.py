from setuptools import setup, find_packages

setup(
    name='cleanText',
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'click >= 6.6',
        'pytest >= 3.0.2',
    ],
    packages=find_packages(),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
