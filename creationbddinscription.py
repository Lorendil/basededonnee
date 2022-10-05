#L'objectif de ce script est de créer une base de donnée de type inscription pour un service
import json


def ajoutbdd(bdd, fichierbdd):
    """Cette fonction permet d'ajouter à un fichier des informations de type inscription demandés à l'user"""
    #On va demander chaque information nous intéressant
    nom = str(input("Indiquez votre nom de famille\n"))
    prenom = str(input("Indiquez votre prénom\n"))
    age = str(input("Indiquez votre âge\n"))
    ville = str(input("Indiquez votre ville\n"))
    codepostal = str(input("Indiquez votre code postal\n"))
    adresse = str(input("Indiquez votre adresse\n"))
    sexe = str(input("Indiquez votre sexe(M/F)\n"))
    
    #Ça ne sert à rien, mais c'est pour debug
    bdd[nom, prenom] = (age,ville,codepostal,adresse,sexe)
    
    #On écrit la string qui sera copiée dans le fichier en plaçant le \n pour le retour à la ligne
    dicoponctuel = {}
    dicoponctuel["Nom"], dicoponctuel["Prénom"], dicoponctuel["Age"], dicoponctuel["Ville"], dicoponctuel["Code Postal"], dicoponctuel["Adresse"], dicoponctuel["Sexe"] = nom, prenom, age, ville, codepostal, adresse, sexe

    
    #Listgen est la liste contenue dans le fichier
    bddad = open(fichierbdd, 'r', encoding="utf-8")
    listgen = json.load(bddad)
    bddad.close()

    listgen.append(dicoponctuel)
    
    bddad = open(fichierbdd,'w', encoding="utf-8")
    json.dump(listgen,bddad,indent=4)
    bddad.close()

fichierbdd = "bddadherents"

dicoinscription = {}
dicoinscription["Nom"] = ("Prénom","Âge","Ville", "Code Postal", "Adresse", "Sexe")
rec = "oui"

while(rec == "oui"):
    ajoutbdd(dicoinscription,fichierbdd)
    rec = str(input("Ajouter un nouveau membre ? (Oui/Non)"))
    rec = rec.lower()
    
print(dicoinscription)
