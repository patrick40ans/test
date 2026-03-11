#!usr/bin/env python3

Cellule = {
    "Parts": {
        "TubeSup": 0,
        "TubeInf": 0,
        "Triangle": 0,
        "Cadre": 0
    },
    "Fixtures": {
        "ConvTriangle": 0,
        "ConvTubeInf": 0,
        "ConvTubeSup": 0,
        "PosteSoudage": 0
    },
    "RobotControllers": {
        "ARCMate100iD": 0,
        "PositionerHollowType300": 0
    },
    "Machines": {
        "ConvEvac": 0
    }
}

#fonction arbo
def arbo ():
     for index, (type_objet, elements) in enumerate(Cellule.items()):
         print(f"[{index}] {type_objet}")
         for i, (nom, prix) in enumerate(elements.items()):
             print(f"  - {nom} {index}.{i} : {prix} €")
     print("[4] Afficher le total")


#Boucle de relance
while True:
    arbo()
    choix = int(input("\nChoisissez un type (0 à 4) : "))

    
    # Vérification du choix
    if choix < 0:
        print("Choix invalide.")
        continue


    # choix total
    if choix >= 4:
        total = 0
        for elements in Cellule.values():
            total += sum(elements.values())
        print("\nTotal =", total, "€")
        break


    # Récupération du type choisi
    type_selectionne = list(Cellule.keys())[choix]
    elements = Cellule[type_selectionne]
    
    
    print(f"\nÉléments dans {type_selectionne} :")
    for index, (nom, prix) in enumerate(elements.items()):
        print(f"   [{index}] {nom} : {prix} €")


    choix_element = int(input("Choisissez un élément : "))

    if choix_element < 0 or choix_element >= len(elements):
        print("Élément invalide.")
        continue

    # Récupération du nom de l’élément
    nom_element = list(elements.keys())[choix_element]

    # écriture du nouveau prix
    nv_prix = float(input(f"Nouveau prix pour {nom_element} : "))

    # Mise à jour du prix
    Cellule[type_selectionne][nom_element] = nv_prix
    print(f"Prix mis à jour : {nom_element} = {nv_prix} €")
