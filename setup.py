from setuptools import setup, find_packages

setup(
    name='contractions_expander',
    version='0.1',
    author='Krishna Kumar',
    author_email='krish.kk.1095@gmail.com',
    description='A Python library to expand contractions in multiple languages.',
    long_description='A Python library to expand contractions in English, Spanish, French, Italian, and Romanian languages.',
    url='https://github.com/Krish1095-projects/contractions_expander',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    install_requires=['nltk'],  # Add any dependencies here
)
