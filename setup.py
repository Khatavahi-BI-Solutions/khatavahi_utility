from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in khatavahi_utility/__init__.py
from khatavahi_utility import __version__ as version

setup(
	name="khatavahi_utility",
	version=version,
	description="Utility that can use with frappe",
	author="Jigar Tarpara",
	author_email="jigartarpara@khatavahi.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
