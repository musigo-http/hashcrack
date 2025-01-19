# hashcrack
hashcrack is the best tool to brute forcing all sha and md5 hashes in incremental or wordlist mode

## Automated Installation

## Debian
$ sudo apt install python3-colorama
$ dpkg -i python3-hashcrack_1.0.0-1_all.deb
$ hashcrack [parameter]

## Macos
$ ./hashcrack [parameter]

## Manual Installation

## Debian
$ sudo apt install python3-stdeb python3-colorama
$ python3 setup.py --command-packages=stdeb.command bdist_deb
$ dpkg -i deb_dist/python3-hashcrack_1.0.0-1_all.deb

## Macos
$ pip install pyinstaller
$ pyinstaller --onefile hashcrack/hashcrack.py
$ dist/hashcrack [parameter]

## Usage
Brute Force all sha and md5 hashes

Usage: hashcrack [parameter]

## License
hashcrack is release under the MIT license. See LICENSE for details.
