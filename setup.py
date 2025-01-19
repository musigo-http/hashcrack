from setuptools import setup

with open("README.md", "r", encoding="utf-8") as readme_file:
	long_description=readme_file.read()

setup(
	name="hashcrack",
	version="1.0.0",
	description="brute forcing tool for all sha and md5 hashes",
	long_description=long_description,
	long_description_content_type="text/markdown",
	author="MusiGo",
	author_email="mateotayeb@gmail.com",
	license="MIT",
	packages=["hashcrack"],
	package_dir={'hashcrack':'hashcrack/'},
	install_requires=[
		"colorama>=0.4.6",
	],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Environment :: Console",
		"Operating System :: POSIX :: LINUX"
	],
	entry_points={
	'console_scripts': [
        'hashcrack=hashcrack.hashcrack:help',  # Appelle `help` par défaut
		],
	},
	data_files=[
		('share/applications/',['hashcrack.desktop'])
	],
	python_requires=">=3.6"
)
