###Exercice1
###1 Affichage d'un polynome

def afficher(p) :   #p est une liste de coefficients
    polynome = []
    for i in range (len(p)-1,-1,-1) :    #On parcourt la liste du dernier element jusqu'au premier

        if p[i] != 0 : 
            if i != 0 and i !=1 :
                polynome.append(f"{p[i]}X^{i}")
            elif i == 1 :
                polynome.append(f"{p[1]}X")
            else :
                polynome.append(f"{p[0]}")

    polynome_a_afficher = "+".join(polynome)   #on affiche une seule chaine de caractère en emttant un plus entre chaque element de la liste
    print(polynome_a_afficher)

###2 Calcul de la valeur p(x)

def get_valeur(p,x) :
    Valeur = 0
    for i in range (len(p)) :
        if p[i] !=0 :
            Valeur = Valeur + p[i]*(x**i)
    print(f"La valeur du polynome en x={x} est: {Valeur}")

###3 Derivée du polynome p

def deriver(p) :
    p_prime = []
    for i in range (len(p)-1,0,-1) :
        if i == 1 :
            p_prime.append(f"{p[i]}")
        elif i== 2 :
            p_prime.append(f"{p[i]*i}X")
        else :
            p_prime.append(f"{p[i]*i}X^{i-1}")
    print("+".join(p_prime))
    

###Test
p=[3,4,5,7,8]
x=3
afficher(p)
get_valeur(p,x)
deriver(p)