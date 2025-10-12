
#1/ Ecrire un programme qui prend un entier x et qui affiche un triangle rectangle de hauteur x.
# Par exemple, pour x = 5 :
#
##
###
####
#####

y=1
while y<6:
    print('#'*y)
    y=y+1
    
#2/ Dans la même idée, écrire un programme qui affiche un triangle isocèle à l’envers :
 #########
  #######
   #####
    ###
     #
ht='#'
nbr=9
for i in range(0,5):
    print(f"{" "*i}{ht*nbr}")
    nbr=nbr-2
    

#3/ Dans la même idée, écrire un programme qui affiche un triangle isocèle à l’endroit :
    #
   ###
  #####
 #######
#########
ht='#'
nbr=1
for i in range(5,0,-1):
    print(f"{" "*i}{ht*nbr}")
    nbr=nbr+2
    

# Exercice 1 : jeu de l'oie super simple
print('''+-------------------------------------------------------------------+
+-------------------------------------------------------------------+
+---------------------------JEUX DE L'OIE !-------------------------+
+-------------------------------------------------------------------+
+-------------------------------------------------------------------+''')   
################################################################################################################################################
# INITIALISATION : on demande le nombre de joueurs, le nombre de dés qu'ils veulent utiliser et on met en place le nombre de cases.
NB_CASES= 50
nb_joueur=int(input("Bienvenue dans le jeu de L'OIE ! Combien de joueurs êtes-vous ? "))
print(f"Votre jeu comporte {NB_CASES} cases.")
nb_de=int(input("Avec combien de dés allez-vous jouer ? "))


# Je crée le dictionnaire pour pouvoir stocker les valeurs des joueurs
joueurs=[] # Je crée le tableau pour stocker les données


for t in range(nb_joueur):
    nom=input("Quel est ton pseudo ? ")
    joueur={
        'nom': None,   # Pour l'instant je mets None car il va demander le prénom et le mettre dans le dico
        'position': 0
    }
    joueurs.append(joueur)  # Je mets les joueurs dans le tableau
    joueur['nom'] = nom


########################################################################################################################
#################################################  Mes fonction ###########################################################
############################################################################################################################

# Je vais d'abord créer la fonction pour le nombre de dés utilisés et leur résultat

import random

def d(nb_de): 
    
    de_tableau=[]
    de_result=0
    somme=0
    for x in range(nb_de):
        de_result = random.randint(1, 6)
        de_tableau.append(de_result)
        # print(de_result)
    somme = sum(de_tableau) + somme
    return somme
    









    # Faire les cases spéciales
def case_special():
    if joueur['position']%9==0:
        joueur['position']+=9
    print(f"Bravo {joueur['nom']} avance de 9 cases !")
    print(f"{joueur['nom']} est à la case {joueur['position']}")

    #def case_pont():
    if joueur['position']==15:
        joueur['position']=20
    print(f"Bien joué {joueur['nom']} ! Vous êtes à la case {joueur['position']}")

    #def case_puit():
    if joueur['position']/25==1:
        joueur['position']=10
    print(f"Bien joué {joueur['nom']} ! Vous êtes à la case {joueur['position']}")

### Pour faire les traits :
def afficher_plateau():
    tableau=[]
    for i in range(1,51):
        
        trouve = False
        for joueur in joueurs:
            if i==joueur["position"]:
                tableau.append(joueur['nom'])
                trouve = True
                break
        if not trouve:
            tableau.append('-')
    tableau.insert(0,'D')
    tableau.insert(len(tableau)+1,'F')
    print( tableau)






####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

# Maintenant il faut lancer le jeu et les joueurs vont lancer le jeu tant qu'aucun d'eux n'a atteint l'objectif de 50


jeu_termine = False
while not jeu_termine:
    for joueur in joueurs:
        joueur['position'] += d(nb_de)
        print(f"{joueur['nom']} est à la case {joueur['position']}")
        
        
        # la ou j'appelle mes fonctionn case :
        
        case_special()
        afficher_plateau()
        input()
        
        
        
        if joueur['position'] >= NB_CASES:
            print(f"Bravo {joueur['nom']} a gagné !")
            jeu_termine = True
            break
        
        

        


#######


