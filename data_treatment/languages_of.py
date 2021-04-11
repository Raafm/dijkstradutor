"""
This program gets all the languages incident with any of these chosen
countries: Brazil (BR), Germany (DE), Russia (RU), India (IN), United
States (US) and China (CN). The subgraph containing these countries
and some of these languages will be used in an animation for illustration 
purposes.
"""

from names_initials.data_relations.data_relations import initials_num, num_initials, initials_name
from adjacency import adj

br_num = initials_num["BR"]
de_num = initials_num["DE"]
ru_num = initials_num["RU"]
in_num = initials_num["IN"]
us_num = initials_num["US"]
cn_num = initials_num["CN"]

# the set of all languages incident with any of these 5 countries
lang_set = set()
# the subgraph induced by these 5 countries
induced_adj = {br_num: [], de_num: [], ru_num: [], in_num: [], us_num: [], cn_num: []}

for country_num in induced_adj:
	for lang_num, weight in adj[country_num]:
		lang_set.add(lang_num)
		induced_adj[country_num].append((lang_num, weight))

with open("text_languages_of.txt", 'w') as file:

	file.write("The countries are ")
	for country_num in induced_adj:
		country_initials = num_initials[country_num]
		country_name = initials_name[country_initials]
		file.write(f"{country_name} ({country_initials}), ")

	file.write("\n\n")

	file.write("The languages incident with any of these countries are:\n\n")
	file.write("NAME (INITIALS)\n")
	for lang_num in lang_set:
		lang_initials = num_initials[lang_num]
		lang_name = "name_not_found"
		try:
			lang_name = initials_name[lang_initials]
		except KeyError:
			pass
		file.write(f"{lang_name} ({lang_initials})\n")

	file.write("\n\nThe languages incident with each country are:\n\n")
	for country_num in induced_adj:
		country_initials = num_initials[country_num]
		country_name = initials_name[country_initials]
		file.write(f"{country_name} ({country_initials}):\n")

		for lang_num, weight in induced_adj[country_num]:
			lang_initials = num_initials[lang_num]
			lang_name = "name_not_found"
			try:
				lang_name = initials_name[lang_initials]
			except KeyError:
				pass
			file.write(f"\t{lang_name} ({lang_initials}), {weight}\n")
		file.write("\n")
