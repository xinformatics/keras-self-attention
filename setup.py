from setuptools import setup

setup(
    name='keras-self-attention',
    version='0.0.13',
    packages=['keras_self_attention'],
    url='https://github.com/CyberZHG/keras-self-attention',
    license='MIT',
    author='CyberZHG',
    author_email='CyberZHG@gmail.com',
    description='Attention mechanism for processing sequence data that considers the context for each timestamp',
    long_description=open('README.rst', 'r').read(),
    install_requires=[
        'numpy',
        'keras',
    ],
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
