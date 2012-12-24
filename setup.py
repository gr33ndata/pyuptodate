from setuptools import setup

setup(
	name='PyUptodate',
	version='0.1.0',
	author='Tarek Amr',
	author_email='',
	packages=['pyuptodate'],
	license='LICENSE.txt',
	description='Check all installed Python modules and update them',
	long_description=open('README.rst').read(),
    install_requires=["setuptools"],
)
