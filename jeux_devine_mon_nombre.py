print('''
      +-----------------------------------------------------------------------------+
      +-----------------------------------------------------------------------------+
      +-------------------JEUX----DEVINE-----MON----NOMBRE--------------------------+
      +-----------------------------------------------------------------------------+
      +-----------------------------------------------------------------------------+''')

import random
Nbr=random.randint(1,30) #Nombre choisi par l'ordinateur appelé Nbr
# afficher le nbr choisi par l'ordinateur 
print(f"j'ai choisi un nombre entre 1 et 30,")
print(f"A vous de le devinez en 5 tentatives au maximum !! ")
nbr_try=1
nbr_choisi=0
   
while nbr_try<=5:
    
    print(f"essai numéro:{nbr_try}")
    nbr_choisi=int(input("vous avez choisi:"))
    nbr_try+=1
    if nbr_choisi!=Nbr and 1<=nbr_choisi<=30 :
        print('perdu')
        continue
        
    elif nbr_choisi>30:
        print("le nombre choisit est trop grand, c'est entre 1 et 30 ! ")
    elif nbr_choisi<1:
        print("le nombre choisit est trop petit, c'est entre 1 et 30 ! ")
    else:
        print(f"bien jouer vous avez trouvé(e) en {nbr_try} essais")
        break
print(f"le nombre etait {Nbr}")        

if nbr_try>=5 and nbr_choisi!=Nbr:
    print("Désolé, vous avez utilisé vos 5 essais en vain.")

       