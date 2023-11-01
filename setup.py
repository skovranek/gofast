from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='BuildGoFast',
    version='0.0.0',
    description='Generate an API Go module from an OpenAPI Description YAML file.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/skovranek/gofast',
    author='Matt Skovranek',
    author_email='mattjskov@gmail.com',
    #license='MIT',
    classifiers=['Private :: Do Not Upload'],
    #keywords='go golang generator api openapi yaml',
    packages=find_packages(['gofast', 'gofast.*']),
    install_requires=[
        'pathspec==0.11.2',
        'PyYAML==6.0.1',
        'ruamel.yaml==0.17.35',
        'ruamel.yaml.clib==0.2.8',
        'yamllint==1.32.0'
    ],
    #python_requires='>=3',
    #setup_requires=['pytest-runner', 'flake8'],
    #tests_require=['pytest'],
    entry_points={
        'console_scripts': ['gofast=gofast.main:main']
    }
)
