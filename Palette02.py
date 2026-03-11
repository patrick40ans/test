#!usr/bin/env python3

'''
Bloc de commentaire en python
code source : Palette.py
Auteur : Thomas
'''

#Type de palette
palette_type = 2
if palette_type == 1:
	nb_boite_couche = 9
elif palette_type == 2:
	nb_boite_couche = 5
else:
	exit()

#Calcul
nb_boite = 45
nb_couche = int(nb_boite / nb_boite_couche)


#Affiche résultat
print("Palette de ", nb_boite, "boites")
print("Il y a ", nb_couche , " couches")
