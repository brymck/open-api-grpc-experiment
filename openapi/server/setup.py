from setuptools import setup, find_packages

setup(
    name='greeter-server',
    version='0.0.1',
    description='A sample Python project',
    author='Bryan McKelvey',
    author_email='bryan.mckelvey@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Flask~=1.0',
        'flask-restplus~=0.12.0',
    ],
    package_data={},
)