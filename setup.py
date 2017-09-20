from distutils.core import setup

setup(
    name='jobCLI',
    version='1.a3',
    include_package_data=False,
    author='Stephan Goergen',
    author_email='stephan.goergen@gmail.com',

    url='https://www.jobcli.com',
    license='MIT',
    description='Job Search Command Line Tool',
    keywords='jobs careers jobsearch developers commandline',

    classifiers=[
        'Development Status :: 3 - Alpha', # 3 - Alpha | 4 - Beta | 5 - Prod
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
