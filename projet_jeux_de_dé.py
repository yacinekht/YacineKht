print('''+________________JEUX DE DES_______________+
--------------------------------------------
--------------------------------------------
--------------------------------------------''')
import random
# joueur1=input('Quelle est ton nom ? ')
# joueur2=input('Quelle est ton nom ? ')
# somme1=0
# somme2=0

# for i in range(10):
#     resulat_du_dés1=random.randint(1,6)
#     resulat_du_dés2=random.randint(1,6)
#     somme1= somme1+resulat_du_dés1 
#     somme2= somme2+resulat_du_dés2 
#     d=i
#     print(f"{joueur1} le dés {d} a donner {resulat_du_dés1}")
#     print(f"{joueur2} le dés {d} a donner {resulat_du_dés2}")
# print(f'la somme de {joueur1} est {somme1} ')
# print(f'la somme de {joueur2} est {somme2} ')
valeur=random.randint(1,100)    # je donne une valeur au azard pour que la psn qui jouer n'est pas tjr le meme objectif a attiendre 
print(f" le jeux vas commencer !!! ATTENTION le but est d'etre le plus proches de la valeur: {valeur}") # je previen le joueur 
le_nbr_de_joueur=int(input("combien y'a t'il de joueurs ? ")) # je demande au joueurs combien ils ont 
score=0     # j'initialise le score a 0 parceque on en auras besoin plus tard il y avait aussi une autre solution comme j'ai fait avec le score_final 
joueurs=[]  # je crée un tableau qui vas me permettre de ranger mes joueurs et leur caractéristique 

# je créé un boucle que vas faire la meme chose pour chaque joueur et comme chaque joueur vas jouer il faut que chaqu'un joue et je leur dmd leur nom avant 
for x in range(le_nbr_de_joueur):
    score=0  
    nom=input(f"quelle est le nom du joueur ? ")
    joueur={
        "nom": nom,
        "lances":0,
        "score":0,
        "score_final":0 
         
    }
    joueurs.append(joueur) # je range comme je les dit les caractéristique de mon joueurs dans le tableau comme ca je vais pouvoirs enregistrer mes valeur et les réutiliser si besoin de facon ordonner et bien ranger 
    
# mtn que j'ai les caractéristique du joueur mtn il faut bine que le joueur joue , donc je le met bien dasn la boucle et le nombre de fois ou il joue vas dependre de lui meme alors soit je met un boucle while , soit for avec une vzaleur qui commencer met que on ne c pas quand elle vas s'arreter
    
    for i in range(0,1000000000):
        
        resultat_du_dés=random.randint(1,6)
        score=score+resultat_du_dés
        reponse=input(f"la somme est {score} est ce que on continue ? ")
        
        # a ce moment la il faut enregistrer les valeurs si je m'arrete la sans ecrire append bas els valeur vont pas s'enregistrer pour le joeueur et du coup bon courage pas les reutiliser 
        joueur["lances"]=joueur["lances"]+1
        joueur["score"]=score
        # ici y'a quelque chose qui est mauvais c le continue et le break c pas bien de les utiliser donc il faudrais utiliser une boucle while au debut a la place et mettre jor un truc= true et tant que il est vrai pas on refait la boucle et au moment ou le mec vas donner un truc differend de true pas sava stopper 
        # reponse=True
        # while reponse:
        #     resultat_du_dés=random.randint(1,6)
        # score=score+resultat_du_dés
        # reponse=input(f"la somme est {score} est ce que on continue ? ")
        # joueur["lances"]=joueur["lances"]+1
        # joueur["score"]=score
        if reponse== 'OUI':
            continue
        else:
            break
    print(f"le nombre de lancer est {joueur["lances"]}")
    
        # joueur["score"]=score
    print(f"la somme est {score} pour le joueur {nom}")

# mtn on a termine ceque chaque joueur vas faire on doit mtn comparer les score , qui vas gagné qui auras le score le plus proche de l'objectif etc...
# le moment ou il faut comparer les score_final :   

la_plus_petit_valeur=1000000000000


for x in range(le_nbr_de_joueur):
    
    score_final=valeur-joueurs[x]['score'] # pk x parceque il vas aller chercher le premier joueur et aprés il vas refaire la boucle ne fonction du nombre de joueur voila pk dans le for j'ai ecrit nbr de joueur 
    # on enregistre tjr pour pouvoir le réutiliser 
    joueurs[x]['score_final']=score_final

    if score_final<0:
        print(f'{joueurs[x]['nom']} a perdu , vous avez dépasser  {valeur}')
    else:
#mtn il faut regarder le quelle des joeur restant a le score_final le plus petit
            if joueurs[x]["score_final"]>=0 and joueurs[x]["score_final"]<=la_plus_petit_valeur:
                la_plus_petit_valeur=joueurs[x]["score_final"]
            else:
                continue
if la_plus_petit_valeur==None:
    print("il y a pas de gagnant")

print( f"le gagant a {la_plus_petit_valeur} de difference avec l'objectif et c'est {joueurs[x]['nom']}")

 

    

         

