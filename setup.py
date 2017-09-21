from setuptools import setup

setup(
    name='jobcli',
    version='0.1.a1',
    py_modules=['jobcli'],
    install_requires=['click', 'requests',],
    entry_points={'console_scripts':['jobcli=jobcli:cli',]},
    url='https://www.jobcli.com',
    author='Stephan Goergen',
    author_email='stephan.goergen@gmail.com',
    description='Job Search from the Command Line',
    license='MIT',
    zip_safe=False,
    include_package_data=False,
    keywords='board job search command line career developer engineer',
    classifiers=[
        'License :: OSI Approved :: MIT License'
       ,'Development Status :: 3 - Alpha'
       ,'Environment :: Console'
       ,'Operating System :: OS Independent'
       ,'Natural Language :: English'
       ,'Intended Audience :: Developers'
       ,'Intended Audience :: Information Technology'
       ,'Intended Audience :: System Administrators'
       ,'Intended Audience :: Science/Research'
       ,'Topic :: Office/Business'
       ,'Programming Language :: Python :: 2'
       ,'Programming Language :: Python :: 2.7'
       ,'Programming Language :: Python :: 3'
       ,'Programming Language :: Python :: 3.3'
       ,'Programming Language :: Python :: 3.4'
       ,'Programming Language :: Python :: 3.5'
    ]
)

