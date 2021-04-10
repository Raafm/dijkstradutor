"""
Program for creating lists and dictionaries that relate numbers, initials
and names of countries and languages.
"""

from pathlib import Path

# base is the path to the dijkstradutor directory. This is necessary because
# the files needed (siglas_nomes.txt, unicodelang.language.txt,
# unicodelang_country.txt) are not in the current directory or in a
# subdirectory, so relative paths won't work.
base = str(Path().absolute().parent.parent.parent)

# creating a dictionary that maps initials to names. This is done by using
# siglas_nomes.txt, which provides the initials of each name of country.
initals_name = {}

with open(base+r"\Create_graph\Nodes\siglas_nomes.txt", 'r') as file1:
	for line in file1:
		if line == '\n':
			continue
		line = line.split()
		name = ''
		i = 1
		# see the siglas_nomes.txt file to check the format of each line
		while True:
			name += line[i] + ' '
			if name[-2] == ",":
				break
			i += 1
		name = name[:-2]  # taking the comma and the space out
		i += 2
		initials = line[i]
		if line[0][0] == 'c':  # then it's a country entry
			initals_name[initials[:-1]] = name  # taking the final comma out
		else:  # then it's a language entry
			initals_name[initials] = name

# creating a tk language code key so that it is consistent with the unicodelang
# database
initals_name["tk"] = initals_name["tkl"]
# adding some cases not catched by the above code or not existent in the used
# database (siglas_nomes.txt)
initals_name["TT"] = "Trinidad and Tobago"
initals_name["kk"] = "Kazakh"
initals_name["arq"] = "Algerian Arabic"
initals_name["ku"] = "Ku"
initals_name["az"] = "Azeri"
initals_name["zh"] = "Chinese"
initals_name["wbp"] = "Warlpiri"
initals_name["bar"] = "Bavarian"
initals_name["tly"] = "Talysh"
initals_name["ttt"] = "Muslim Tat"
initals_name["tkr"] = "Tsakhur"
initals_name["vls"] = "Vlaams"
initals_name["aro"] = "Araona"
# there are too many missing initials, i'll simply stop here and handle
# it in main.py with try-except

# creating a list such that its i-th index has the initials of the
# country/language associated with vertex i. It's a "num-to-initials"
# list. This is done by using both unicode.language.txt, for getting 
# the initials of languages, and unicodelang_country.txt, for getting
# the initials of countries. They are from the Database folder.
num_initials = [None]

# creating a dictionary that maps initials back to the associated number.
# It's the opposite/inverse of num_initials. It uses the same data as
# num_initials.
initials_num = {}


counter = 1
# languages are numbered from 1 to 614
with open(base+r"\Database\unicodelang.language.txt", 'r') as file2:
	for line in file2:
		initials = line[:-1]
		num_initials.append(initials)
		initials_num[initials] = counter
		counter += 1

# countries will be renumbered from 615 to 868
with open(base+r"\Database\unicodelang_country.txt", 'r') as file3:
	# same thing as with file2
	for line in file3:
		initials = line[:-1]
		num_initials.append(initials)
		initials_num[initials] = counter
		counter += 1

# now we have a list that maps numbers to initials and a dicionary that maps
# initials to numbers. The first dictionary, from initials to names, will be
# used when possible. All three will now be saved as constants in a file.

with open(base+r"\Create_graph\Nodes\data_relations\data_relations.py", 'w') as out_file:
	# definig the proper encodig
	out_file.write("#!/usr/bin/env python\n# -*- coding: latin-1 -*-\n\n")
	out_file.write("initials_name = " + str(initals_name) + "\n\n")
	out_file.write("num_initials = " + str(num_initials) + "\n\n")
	out_file.write("initials_num = " + str(initials_num) + "\n")
