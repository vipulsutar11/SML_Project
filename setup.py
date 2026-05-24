from setuptools import setup, find_packages

def read_requirements(path: str = 'requirements.txt'):
    try:
        with open(path) as f:
            requirements = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
    except FileNotFoundError:
        return []

    return [line for line in requirements if line != '-e .']



setup(
    name='my_package',
    version='0.0.1',
    packages=find_packages(),
    install_requires=read_requirements(),
    description='A sample python application',
    author='Vipul Sutar',
    author_email='vipulsutar001@gmail.com',
    url='https://github.com/vipulsutar/my_package')
