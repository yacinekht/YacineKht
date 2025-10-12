print("+________________JEU DE DÉS_______________+")
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

import random
valeur=random.randint(1,100)    # Je donne une valeur au hasard pour que la personne qui joue n'ait pas toujours le même objectif à atteindre
print(f"Le jeu va commencer ! ATTENTION, le but est d'être le plus proche de la valeur : {valeur}") # Je préviens le joueur
le_nbr_de_joueur=int(input("Combien y a-t-il de joueurs ? ")) # Je demande aux joueurs combien ils sont
score=0     # J'initialise le score à 0 car on en aura besoin plus tard. Il y avait aussi une autre solution comme j'ai fait avec le score_final
joueurs=[]  # Je crée un tableau qui va me permettre de ranger mes joueurs et leurs caractéristiques

    
    # Je crée une boucle qui va faire la même chose pour chaque joueur. Comme chaque joueur va jouer, il faut que chacun joue et je leur demande leur nom avant.
for x in range(le_nbr_de_joueur):
    score=0
    nom=input(f"Quel est le nom du joueur ? ")
    joueur={
        "nom": nom,
        "lances": 0,
        "score": 0,
        "score_final": 0
    }
    joueurs.append(joueur) # Je range les caractéristiques de mon joueur dans le tableau pour pouvoir enregistrer les valeurs et les réutiliser si besoin de façon ordonnée et bien rangée

    # Maintenant que j'ai les caractéristiques du joueur, il faut bien que le joueur joue. Donc je le mets dans la boucle et le nombre de fois où il joue va dépendre de lui-même. Alors soit je mets une boucle while, soit for avec une valeur qui commence mais on ne sait pas quand elle va s'arrêter.
    for i in range(0, 1000000000):
        resultat_du_dés = random.randint(1, 6)
        score = score + resultat_du_dés
        reponse = input(f"La somme est {score}. Est-ce qu'on continue ? ")
        joueur["lances"] = joueur["lances"] + 1
        joueur["score"] = score
        # Ici, il y a quelque chose qui est mauvais : le continue et le break, ce n'est pas bien de les utiliser. Donc il faudrait utiliser une boucle while au début à la place et mettre par exemple un truc = True et tant que c'est vrai, on refait la boucle et au moment où le joueur donne un truc différent de True, ça va stopper.
        if reponse.upper() == 'OUI':
            continue
        else:
            break
    print(f"Le nombre de lancers est {joueur['lances']}")
    print(f"La somme est {score} pour le joueur {nom}")

    # Maintenant que chaque joueur a terminé, on doit comparer les scores, qui va gagner, qui aura le score le plus proche de l'objectif, etc.
    # Le moment où il faut comparer les scores finaux :

la_plus_petite_valeur = 1000000000000
gagnant = None

for x in range(le_nbr_de_joueur):
    score_final = valeur - joueurs[x]['score'] # x va chercher le premier joueur et après il va refaire la boucle en fonction du nombre de joueurs
    # On enregistre toujours pour pouvoir le réutiliser
    joueurs[x]['score_final'] = score_final

    if score_final < 0:
        print(f"{joueurs[x]['nom']} a perdu, vous avez dépassé {valeur}")
    else:
        # Maintenant il faut regarder lequel des joueurs restants a le score_final le plus petit
        if joueurs[x]["score_final"] >= 0 and joueurs[x]["score_final"] <= la_plus_petite_valeur:
            la_plus_petite_valeur = joueurs[x]["score_final"]
            gagnant = joueurs[x]['nom']
        else:
            continue
if gagnant is None:
    print("Il n'y a pas de gagnant.")
else:
    print(f"Le gagnant a {la_plus_petite_valeur} de différence avec l'objectif et c'est {gagnant}.")

 

    

         

