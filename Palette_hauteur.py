#!usr/bin/env python3
'''
Pallete_hauteur.py
'''

#Gestion du nombres de boites
nb_boite = int(input("Nombre de boîtes (1 à 100) : "))
if nb_boite < 1:
	print("Erreur : Impossible le nombre a été forcé a 1")
	nb_boite = 1
if nb_boite >100:
	print("Erreur : Impossible le nombre a été forcé a 100")
	nb_boite = 100



#Gestion du nombre de couches
nb_boite_couche = int(input("Boîtes par couche (4, 5, 6 ou 9) : "))
dispositions_valides = [4, 5, 6, 9]

if nb_boite_couche not in dispositions_valides:
    print("Erreur : disposition inconnue. Valeurs possibles : 4, 5, 6 ou 9.")
    exit()
    

#Calcul
Boite_hauteur_cm = 25
nb_boite_hauteur = nb_boite / nb_boite_couche
test= nb_boite_hauteur - int(nb_boite_hauteur)

if test > 0 :
	boite_hauteur = int(nb_boite_hauteur)+1
else:
	boite_hauteur = int(nb_boite_hauteur)

Boite_hauteur_m = (boite_hauteur * Boite_hauteur_cm)/100

#Resultat
print(f"Hauteur totale de la palette : {Boite_hauteur_m} m")
