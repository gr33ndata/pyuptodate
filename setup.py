from setuptools import setup

setup(
	name='pyuptodate',
	version='0.1.0',
	author='Tarek Amr',
	author_email='',
    url='https://github.com/gr33ndata/pyuptodate',
	packages=['pyuptodate'],
    scripts=['pyuptodate/pyuptodate.py'],
	license='LICENSE.txt',
	description='Check all installed Python modules and update them',
	long_description=open('README.rst').read(),
    install_requires=["setuptools"],
)
