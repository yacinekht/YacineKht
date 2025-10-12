print('''
      +-----------------------------------------------------------------------------+
      +-----------------------------------------------------------------------------+
      +-------------------JEUX----DEVINE-----MON----NOMBRE--------------------------+
      +-----------------------------------------------------------------------------+
      +-----------------------------------------------------------------------------+''')

import random
Nbr=random.randint(1,30) #Nombre choisi par l'ordinateur appelé Nbr
# afficher le nbr choisi par l'ordinateur 
print(f"J'ai choisi un nombre entre 1 et 30.")
print(f"À vous de le deviner en 5 tentatives au maximum !")
nbr_try=1
nbr_choisi=0
   
while nbr_try<=5:
    
    print(f"Essai numéro : {nbr_try}")
    nbr_choisi=int(input("Vous avez choisi : "))
    nbr_try+=1
    if nbr_choisi != Nbr and 1 <= nbr_choisi <= 30:
        print('Perdu')
        continue
    elif nbr_choisi > 30:
        print("Le nombre choisi est trop grand, c'est entre 1 et 30 !")
    elif nbr_choisi < 1:
        print("Le nombre choisi est trop petit, c'est entre 1 et 30 !")
    else:
        print(f"Bien joué, vous avez trouvé en {nbr_try} essais !")
        break
print(f"Le nombre était {Nbr}")

if nbr_try > 5 and nbr_choisi != Nbr:
    print("Désolé, vous avez utilisé vos 5 essais en vain.")

       