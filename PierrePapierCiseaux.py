
print('''
      -------------------------JEUX--------------------------
      PIERRE------------------PAPIER-------------------CISEAU''')
import random
print("Pierre, Papier, Ciseaux , le premier a 5 point a gagné(e)!!")


def score(nombre):
    if nombre==1:
        return 'Pierre'
    elif nombre==2:
        return 'Papier'
    else:
        return 'Ciseau'

def totalDesPoints(MOI,ORDINATEUR):
    if MOI==ORDINATEUR:
        return point_moi==0, point_ordi==0  # égalité
    elif (MOI==3 and ORDINATEUR==2) or (MOI==2 and ORDINATEUR==1) or (MOI==1 and ORDINATEUR==3):
        return point_moi==1, point_ordi==0  # humain gagne
    else:
        return point_moi==0, point_ordi==1  # ordinateur gagne

score_moi=0
score_ordinateur=0
while score_moi < 5 and score_ordinateur < 5:
    MOI=int(input("1:Pierre,2:Papier,3:Ciseau   : "))
    while MOI<1 or MOI>3 :
        MOI=int(input("1:Pierre,2:Papier,3:Ciseau   : "))
    ORDINATEUR=random.randint(1,3)
    print(f"l'humain montre {score(nombre=MOI)}")
    print(f"l'ordinateur montre {score(nombre=ORDINATEUR)}")
    point_moi, point_ordi = totalDesPoints(MOI,ORDINATEUR)
    score_moi += point_moi
    score_ordinateur += point_ordi
    print(f" l'humain a {score_moi} et l'ordinateur a {score_ordinateur}")

if score_moi == 5:
    print("Bravo, l'humain a gagné !")
elif score_ordinateur == 5:
    print("L'ordinateur a gagné !")


    
    
