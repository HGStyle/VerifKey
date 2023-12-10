import shutil, os
print('DO NOT USE THIS. IT WAS BROKEN, ITS STILL BROKEN AND WILL BE BROKEN FOREVER BECAUSE I DONT WANT TO UPDATE IT. THE MODULE ISNT BROKEN ITSELF, JUST THE INSTALLER. BUT I DONT WANT TO SUPPORT THIS. THIS WAS MADE LESS THAN A YEAR AGO (when i wrote that) BUT I EVOLVED AND THIS SHOULD NOT BE USED ANYMORE. CODE RELEASED UNDER THE UNLICENSE. FOR MORE INFO, GOTO https://github.com/HGStyle/VerifKey/')
print('Starting installation of VerifKey...')
print('This will only take a second...')

# Get the Python lib folder
libdir = os.sep.join(shutil.__file__.split(os.sep)[:-1])
if not libdir.endswith(os.sep):
	libdir += os.sep

# Try downloading VerifKey with `requests` module or `urllib` module
try:
	import urllib.request
	r = urllib.request.urlopen('https://raw.githubusercontent.com/HGStyle/VerifKey/main/VerifKey.py')
	with open('VerifKey.py', 'wb') as f:
		f.write(r.readlines()[0])
except ImportError:
	import requests
	r = requests.get('https://raw.githubusercontent.com/HGStyle/VerifKey/main/VerifKey.py')
	with open('VerifKey.py', 'wb') as f:
		f.write(r.content)

# Install VerifKey
try:
	shutil.move('VerifKey.py', libdir + 'VerifKey.py')
except PermissionError:
	print('Please run this programm as administrator/root !')
	os.remove('VerifKey.py')
	exit(1)

print('VerifKey module is now installed !')
print('Note that VerifKey is only installed for this Python version !')
