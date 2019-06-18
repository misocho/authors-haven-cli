from setuptools import setup

setup(
    name='ah',
    version='1.0',
    py_modules=['ah'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        ah=ah:ah
    '''
)
