
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
    

# Exercice 1 : jeux de l'oie super simple
print('''+-------------------------------------------------------------------+
+-------------------------------------------------------------------+
+---------------------------JEUX DE L'OIE !-------------------------+
+-------------------------------------------------------------------+
+-------------------------------------------------------------------+''')   
################################################################################################################################################
# INITIALISATION : on demande de le nombre de joueurs , le nbr de dés qu'il veulent utiliser et on met en place le nombre de case .
NB_CASES= 50
nb_joueur=int(input("Bienvenue dans le jeux de L'OIE !    Combien de joueurs etes-vous ?  "))
print(f" votre jeux comportes {NB_CASES} cases ")
nb_de=int(int(input("avec combien de des allez-vous jouer ?"))) 

# Je crée le DICtionnaire pour pouvoir stocker les valeur des Joueurs 
joueurs=[] # je crée le tableau pour stocker les donner 


for t in range(nb_joueur):   
    nom=input("qu'elle est ton speudo ? " )
    joueur={
        'nom': None,   # pour l'instant je met none car il vas dmd aprés le prenom et le mettre dans le dico 
        
        'position':0
    }
    joueurs.append(joueur)  # je met les joueur dans le tableau
    joueur['nom']=nom


########################################################################################################################
#################################################  Mes fonction ###########################################################
############################################################################################################################
# je vais d'abord créé la fonction pour le nombre de dé utiliser et leur resultat 

import random

def d(nb_de): 
    
    de_tableau=[]
    de_result=0
    somme=0
    for x in range(nb_de):    
        de_result=random.randint(1,6)
        de_tableau.append(de_result)
        #print(de_result)
    somme=sum(de_tableau)+somme
    return somme 
    









# faire les cases spéciales
def case_special():
    if joueur['position']%9==0:
        joueur['position']+=9
        print(f"Bravo {joueur['nom']} avance de 9 cases !")
        print(f"{joueur['nom']} est a la {joueur['position']} case")

    #def case_pont():
    if joueur['position']==15:
        joueur['position']=20
        print(f" bien jouer {joueur['nom']} vous  cette a la case {joueur['position']}  ")

    #def case_puit():
    if joueur['position']/25==1:
        joueur['position']=10
        print(f" bien jouer {joueur['nom']} vous  cette a la case {joueur['position']}  ")

### pour faire les trais :
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
# mtn il faut lancer le jeux et les joueur vont lancer le jeux tant que un des deux ne vas pas attiendre l'objectif de 50 


jeu_termine = False
while not jeu_termine:
    for joueur in joueurs:
        joueur['position'] += d(nb_de)
        print(f"{joueur['nom']} est a la {joueur['position']} case ")
        
        
        # la ou j'appelle mes fonctionn case :
        
        case_special()
        afficher_plateau()
        input()
        
        
        
        if joueur['position'] >= NB_CASES:
            print(f"Bravo {joueur['nom']} a gagné !")
            jeu_termine = True
            break
        
        

        


#######


