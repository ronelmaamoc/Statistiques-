import math

def afficher_moyenne_variables(matrice):
    # Calcul des moyennes des variables
    n = len(matrice[0])
    moyennes = []
    
    for i in range(n):
        variable = [ligne[i] for ligne in matrice]
        moyenne = sum(variable) / len(variable)
        moyennes.append(moyenne)
    
    # Affichage des moyennes des variables
    print("Moyenne des variables :")
    print("Variable\tMoyenne")
    for i in range(n):
        print(f"Variable {i+1}\t{moyennes[i]}")

def afficher_variance_et_ecart_type(matrice):
    # Calcul des variances et écart-types des variables
    n = len(matrice[0])
    variances = []
    ecart_types = []
    
    for i in range(n):
        variable = [ligne[i] for ligne in matrice]
        moyenne = sum(variable) / len(variable)
        variance = sum([(x - moyenne)**2 for x in variable]) / len(variable)
        ecart_type = math.sqrt(variance)
        variances.append(variance)
        ecart_types.append(ecart_type)
    
    # Affichage des variances et écart-types des variables
    print("Variance et écart-type des variables :")
    print("Variable\tVariance\t\tÉcart-type")
    for i in range(n):
        print(f"Variable {i+1}\t{variances[i]}\t\t{ecart_types[i]}")

def afficher_covariance(matrice):
    # Calcul de la covariance
    variable_1 = [ligne[0] for ligne in matrice]
    variable_2 = [ligne[1] for ligne in matrice]
    moyenne_1 = sum(variable_1) / len(variable_1)
    moyenne_2 = sum(variable_2) / len(variable_2)
    covariance = sum([(x - moyenne_1) * (y - moyenne_2) for x, y in zip(variable_1, variable_2)]) / len(variable_1)
    
    # Affichage de la covariance
    print("Covariance :")
    print(f"{covariance}")

def afficher_droite_correlation(matrice):
    # Calcul de la droite de corrélation
    variable_1 = [ligne[0] for ligne in matrice]
    variable_2 = [ligne[1] for ligne in matrice]
    moyenne_1 = sum(variable_1) / len(variable_1)
    moyenne_2 = sum(variable_2) / len(variable_2)
    covariance = sum([(x - moyenne_1) * (y - moyenne_2) for x, y in zip(variable_1, variable_2)]) / len(variable_1)
    coefficient_correlation = covariance / (math.sqrt(sum([(x - moyenne_1)**2 for x in variable_1]) / len(variable_1)) * math.sqrt(sum([(y - moyenne_2)**2 for y in variable_2]) / len(variable_2)))
    droite_correlation = f"y = {coefficient_correlation:.2f}x"
    
    # Affichage de la droite de corrélation
    print("Droite de corrélation :")
    print(droite_correlation)

def afficher_coefficient_correlation(matrice):
    # Calcul du coefficient de corrélation
    variable_1 = [ligne[0] for ligne in matrice]
    variable_2 = [ligne[1] for ligne in matrice]
    moyenne_1 = sum(variable_1) / len(variable_1)
    moyenne_2 = sum(variable_2) / len(variable_2)
    covariance = sum([(x - moyenne_1) * (y - moyenne_2) for x, y in zip(variable_1, variable_2)]) / len(variable_1)
    coefficient_correlation = covariance / (math.sqrt(sum([(x - moyenne_1)**2 for x in variable_1]) / len(variable_1)) * math.sqrt(sum([(y - moyenne_2)**2 for y in variable_2]) / len(variable_2)))
    
    # Affichage du coefficient de corrélation
    print("Coefficient de corrélation :")
    print(f"{coefficient_correlation:.2f}")
    
    # Conclusion
    if coefficient_correlation > 0:
        print("Il y a une corrélation positive entre les variables.")
    elif coefficient_correlation < 0:
        print("Il y a une corrélation négative entre les variables.")
    else:
        print("Il n'y a pas de corrélation entre les variables.")

def lire_matrice(lignes):
    matrice = []
    for i in range(lignes):
        ligne = input(f"Entrez les valeurs de la ligne {i+1} séparées par des espaces : ")
        valeurs = ligne.split()
        valeurs = [float(valeur) for valeur in valeurs]
        matrice.append(valeurs)
    return matrice


def menu_variables_discretes_bivariees():
    matrice = lire_matrice(2)
    
    while True:
        # Affichage du menu
        print("\nMENU - variable discrete bivariees : \n\n")
        print("1. Afficher la moyenne des variables")
        print("2. Afficher la variance et l'écart-type")
        print("3. Afficher la covariance")
        print("4. Afficher la droite de corrélation")
        print("5. Afficher le coefficient de corrélation et conclure")
        print("6. Quitter")
        
        choix = input("Choix : ")
        
        if choix == "1":
            afficher_moyenne_variables(matrice)
        elif choix == "2":
            afficher_variance_et_ecart_type(matrice)
        elif choix == "3":
            afficher_covariance(matrice)
        elif choix == "4":
            afficher_droite_correlation(matrice)
        elif choix == "5":
            afficher_coefficient_correlation(matrice)
        elif choix == "6":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
        
        
