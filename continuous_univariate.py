
import math

def afficher_tableau_statistique(matrice):
    # Calcul des statistiques
    n = len(matrice[0])
    moyennes = []
    ecarts_types = []
    
    for i in range(n):
        colonne = [ligne[i] for ligne in matrice]
        moyenne = sum(colonne) / len(colonne)
        ecart_type = math.sqrt(sum([(x - moyenne)**2 for x in colonne]) / len(colonne))
        moyennes.append(moyenne)
        ecarts_types.append(ecart_type)
    
    # Affichage du tableau statistique
    print("Tableau statistique :")
    print("Variable\tMoyenne\t\tÉcart-type")
    for i in range(n):
        print(f"Variable {i+1}\t{moyennes[i]}\t\t{ecarts_types[i]}")

def afficher_valeurs_centrales(matrice):
    # Calcul des valeurs centrales
    n = len(matrice[0])
    medians = []
    quartiles_1 = []
    quartiles_3 = []
    
    for i in range(n):
        colonne = sorted([ligne[i] for ligne in matrice])
        median = colonne[len(colonne) // 2]
        quartile_1 = colonne[len(colonne) // 4]
        quartile_3 = colonne[len(colonne) * 3 // 4]
        medians.append(median)
        quartiles_1.append(quartile_1)
        quartiles_3.append(quartile_3)
    
    # Affichage des valeurs centrales
    print("Valeurs centrales :")
    print("Variable\tMédiane\t\t1er quartile\t3e quartile")
    for i in range(n):
        print(f"Variable {i+1}\t{medians[i]}\t\t{quartiles_1[i]}\t\t{quartiles_3[i]}")

def afficher_valeurs_dispersion(matrice):
    # Calcul des valeurs de dispersion
    n = len(matrice[0])
    minimums = []
    maximums = []
    amplitudes = []
    
    for i in range(n):
        colonne = [ligne[i] for ligne in matrice]
        minimum = min(colonne)
        maximum = max(colonne)
        amplitude = maximum - minimum
        minimums.append(minimum)
        maximums.append(maximum)
        amplitudes.append(amplitude)
    
    # Affichage des valeurs de dispersion
    print("Valeurs de dispersion :")
    print("Variable\tMinimum\t\tMaximum\t\tAmplitude")
    for i in range(n):
        print(f"Variable {i+1}\t{minimums[i]}\t\t{maximums[i]}\t\t{amplitudes[i]}")


def lire_matrice(lignes):
    matrice = []
    for i in range(lignes):
        ligne = input(f"Entrez les valeurs de la ligne {i+1} séparées par des espaces : ")
        valeurs = ligne.split()
        valeurs = [float(valeur) for valeur in valeurs]
        matrice.append(valeurs)
    return matrice

def menu_variables_continue_univariees():
    matrice = lire_matrice(2)
    while True:
        # Affichage du menu
        print("\nMENU - variables continues univariees : \n\n")
        print("1. Afficher le tableau statistique")
        print("2. Afficher les valeurs centrales")
        print("3. Afficher les valeurs de dispersion")
        print("4. Quitter")
        
        choix = input("Choix : ")
        
        if choix == "1":
            afficher_tableau_statistique(matrice)
        elif choix == "2":
            afficher_valeurs_centrales(matrice)
        elif choix == "3":
            afficher_valeurs_dispersion(matrice)
        elif choix == "4":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
