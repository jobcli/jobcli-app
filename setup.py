from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='jobCLI',
    version='1.a3',
    include_package_data=False,
    author='Stephan Goergen',
    author_email='stephan.goergen@gmail.com',

    url='https://www.jobcli.com',
    license='MIT',
    description='Job Search Command Line Tool',
    long_description=readme(),
    keywords='jobs careers jobsearch developers commandline',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    install_requires=['click',],
    python_requires='>=3',
    scripts=['jobcli.py'],
    zip_safe=False,
)
