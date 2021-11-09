import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='codegenlib',
    author='Umut Boz',
    author_email='umut.boz@outlook.com',
    version="0.3.0",
    description='Code Generation library written by python. can use bash script, can be extend python code, can use mustache files or can use any string content for any code generation structure.',
    keywords='code generation, file generation, pypi, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/umutboz/code-gen-lib',
    project_urls={
        'Documentation': 'https://github.com/umutboz/code-gen-lib',
        'Bug Reports':
        'https://github.com/umutboz/code-gen-lib/issues',
        'Source Code': 'https://github.com/umutboz/code-gen-lib'
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=2.7',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)