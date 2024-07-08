import math

def afficher_distribution_marginale(matrice):
    # Calcul des distributions marginales
    n = len(matrice[0])
    distributions = []
    
    for i in range(n):
        variable = [ligne[i] for ligne in matrice]
        distribution = {}
        
        for valeur in variable:
            if valeur in distribution:
                distribution[valeur] += 1
            else:
                distribution[valeur] = 1
        
        distributions.append(distribution)
    
    # Affichage des distributions marginales
    print("Distribution marginale :")
    for i in range(n):
        print(f"Variable {i+1}:")
        print("Valeur\tFréquence")
        for valeur, frequence in distributions[i].items():
            print(f"{valeur}\t{frequence}")
        print()

def afficher_moyennes_marginales(matrice):
    # Calcul des moyennes marginales
    n = len(matrice[0])
    moyennes = []
    
    for i in range(n):
        variable = [ligne[i] for ligne in matrice]
        moyenne = sum(variable) / len(variable)
        moyennes.append(moyenne)
    
    # Affichage des moyennes marginales
    print("Moyennes marginales :")
    print("Variable\tMoyenne")
    for i in range(n):
        print(f"Variable {i+1}\t{moyennes[i]}")

def afficher_covariance(matrice):
    # Calcul de la covariance
    n = len(matrice[0])
    variables = [[ligne[i] for ligne in matrice] for i in range(n)]
    covariances = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            variable_1 = variables[i]
            variable_2 = variables[j]
            moyenne_1 = sum(variable_1) / len(variable_1)
            moyenne_2 = sum(variable_2) / len(variable_2)
            covariance = sum([(x - moyenne_1) * (y - moyenne_2) for x, y in zip(variable_1, variable_2)]) / len(variable_1)
            covariances[i][j] = covariance
    
    # Affichage de la covariance
    print("Covariance :")
    for i in range(n):
        for j in range(n):
            print(f"Cov({i+1}, {j+1}) = {covariances[i][j]}")
        print()

def afficher_droite_regression(matrice):
    # Calcul de la droite de régression
    n = len(matrice[0])
    variable_x = [ligne[0] for ligne in matrice]
    variable_y = [ligne[1] for ligne in matrice]
    moyenne_x = sum(variable_x) / len(variable_x)
    moyenne_y = sum(variable_y) / len(variable_y)
    covariance = sum([(x - moyenne_x) * (y - moyenne_y) for x, y in zip(variable_x, variable_y)]) / len(variable_x)
    variance_x = sum([(x - moyenne_x)**2 for x in variable_x]) / len(variable_x)
    a = covariance / variance_x
    b = moyenne_y - a * moyenne_x
    droite_regression = f"y = {a:.2f}x + {b:.2f}"
    
    # Affichage de la droite de régression
    print("Droite de régression :")
    print(droite_regression)


def lire_matrice(lignes):
    matrice = []
    for i in range(lignes):
        ligne = input(f"Entrez les valeurs de la ligne {i+1} séparées par des espaces : ")
        valeurs = ligne.split()
        valeurs = [float(valeur) for valeur in valeurs]
        matrice.append(valeurs)
    return matrice

def menu_variables_continue_bivariees():
    matrice = lire_matrice(2)
    while True:
        # Affichage du menu
        print("\nMENU - variable continue bivariees : \n\n")
        print("1. Afficher la distribution marginale")
        print("2. Afficher les moyennes marginales")
        print("3. Afficher la covariance")
        print("4. Afficher la droite de régression")
        print("5. Quitter")
        
        choix = input("Choix : ")
        
        if choix == "1":
            afficher_distribution_marginale(matrice)
        elif choix == "2":
            afficher_moyennes_marginales(matrice)
        elif choix == "3":
            afficher_covariance(matrice)
        elif choix == "4":
            afficher_droite_regression(matrice)
        elif choix == "5":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")