#L'objectif de ce script est de créer une base de donnée de type inscription pour un service
import json


def ajoutdico(listtemp):
    """Cette fonction permet d'ajouter à un dictionnaire des informations de type inscription demandés à l'user"""
    rec = "oui"
    while(rec == "oui"):
        #On va demander chaque information nous intéressant
        nom = str(input("Indiquez votre nom de famille\n"))
        prenom = str(input("Indiquez votre prénom\n"))
        age = str(input("Indiquez votre âge\n"))
        ville = str(input("Indiquez votre ville\n"))
        codepostal = str(input("Indiquez votre code postal\n"))
        adresse = str(input("Indiquez votre adresse\n"))
        sexe = str(input("Indiquez votre sexe(M/F)\n"))
        
        #On écrit le dictionnaire qui sera ajouté dans le fichier quand on le souhaitera
        dicoponctuel = {}
        dicoponctuel["Nom"], dicoponctuel["Prénom"], dicoponctuel["Age"], dicoponctuel["Ville"], dicoponctuel["Code Postal"], dicoponctuel["Adresse"], dicoponctuel["Sexe"] = nom, prenom, age, ville, codepostal, adresse, sexe
        listtemp.append(dicoponctuel)
        print(listtemp)
        rec = str(input("Ajouter un nouveau membre ? (Oui/Non)"))
        rec = rec.lower()



def save(fichierbdd,listtemp):
    """Cette fonction permet d'ajouter les dictionnaires à la liste d'un fichier"""
    #Listgen est la liste contenue dans le fichier
    bddad = open(fichierbdd, 'r', encoding="utf-8")
    listgen = json.load(bddad)
    bddad.close()

    #On ajoute le dictionnaire à la liste du fichier
    for v in range(len(listtemp)):
        listgen.append(listtemp[v])
    del listtemp[:]
    bddad = open(fichierbdd,'w', encoding="utf-8")
    json.dump(listgen,bddad,indent=4)
    bddad.close()


def consult(listtemp):
    print(listtemp)

def recupbdd(fichierbdd):
    bddad = open(fichierbdd, 'r', encoding="utf-8")
    listgen = json.load(bddad)
    bddad.close()
    print(listgen)
    
def main():
    """Fonction principale permettant de sélectionner la fonction à effectuer"""
    boucle = 1
    listtemp = []
    while(boucle):
        fichierbdd = "bddadherents"
        choix = str(input("Bonjour, que souhaitez-vous faire ?\n(A)jouter des données au dictionnaire courant\n(C)onsulter le dictionnaire courant\n" +
        "(R)écupérer les dictionnaires du fichier\n(S)auvegarder le dictionnaire courant dans un fichier\n(T)erminer\n -->")).upper()
        
        if(choix == "A"):
            ajoutdico(listtemp)
            print(listtemp)
        elif(choix == "C"):
            consult(listtemp)
        elif(choix == "S"):
            save(fichierbdd,listtemp)
        elif(choix == "R"):
            recupbdd(fichierbdd)
        elif(choix == "T"):
            boucle = 0
        else:
            print("Les réponses possibles sont : A,C,S,R et T, votre réponse ne semble pas correspondre")

if __name__ == "__main__":
    main()