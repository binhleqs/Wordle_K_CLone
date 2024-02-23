try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'Wordle_K_CLone1',
    version = '0.1',
    packages = ['src'],
    install_requires=[],
)