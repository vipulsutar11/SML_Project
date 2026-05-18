from setuptools import setup, find_packages

hyphen_e_dot = '-e .' ## FOR REQUIREMENTS.TXT, TO AVOID ERROR: ERROR: File "setup.py" cannot be installed when an editable install is requested
req = [] ## FOR ADDING REQUIREMENTS FROM REQUIREMENTS.TXT
def read_requirements():
    with open('requirements.txt') as f:
        content = f.read().splitlines()
        req.extend(content)
        return req
    if hyphen_e_dot in req:
        req.remove(hyphen_e_dot)
    return req 



setup_ = setup(    name='my_package',
    version='0.0.1',
    packages=find_packages(),
    install_requires=read_requirements(),
    description='A sample python application',
    author='Vipul Sutar',
    author_email= "vipulsutar001@gmail.com",
    url='https://github.com/vipulsutar/my_package')
