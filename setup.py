from setuptools import setup, find_packages

setup(
    name='GoFast',
    version='0.1.0',
    description='Automatically generates an API and/or static server in Go from an OpenAPI spec YAML file.',
    author='Matt Skovranek',
    author_email='mattjskov@gmail.com',
    url='https://github.com/skovranek/gofast',
    packages=find_packages(include=['gofast', 'gofast.*']),
    install_requires=[
        'pathspec==0.11.2',
        'PyYAML==6.0.1',
        'ruamel.yaml==0.17.35',
        'ruamel.yaml.clib==0.2.8',
        'yamllint==1.32.0'
    ],
    #setup_requires=['pytest-runner', 'flake8'],
    #tests_require=['pytest'],
     entry_points={
        'console_scripts': ['gofast=gofast.main:main']
    }
)
