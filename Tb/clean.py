file_list = [
	'embl',
	'F11.fasta',
	'F11.original.embl',
	'clean.py',
	'embl_list.py',
	'embl_locus.py',
	'main.py',
	'main.ipynb'
]

import os
import shutil

for item in os.listdir('.'):
	if item in file_list: continue
	if os.path.isdir(item): 
		print('Removing directory: ', item)
		shutil.rmtree(item)
	if os.path.isfile(item): 
		print('Removing file: ', item)
		os.remove(item)
