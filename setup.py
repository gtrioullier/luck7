from setuptools import find_packages, setup

with open ('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setup(
    name='lucky7',
    version='0.1.0',
    author='',
    author_email='',
    description='A slot game.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github/gtrioullier/lucky7',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    entry_points={
        'console_scripts':[
            'lucky7=lucky7.cli:main'
        ],
    }
)