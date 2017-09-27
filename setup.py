from setuptools import setup

setup(
    name='thirtythree',
    version='0.0.1',
    description='A search for an integer solution of x^3 + y^3 + z^3 = 33',
    url='https://github.com/alphor/thirtythree',
    author='Ahmad Jarara',
    author_email='ajarara94@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: No-One',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        ],
    keywords='zulip coffee',
    packages=['thirtythree'],
    include_package_data=True,
    extras_require={
        'test': ['pytest'],
    },
    requires=['zulip'])
