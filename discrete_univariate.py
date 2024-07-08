import math

def afficher_tableau_statistique(matrice):
    valeurs = matrice[0]
    effectifs = matrice[1]
    total_effectifs = sum(effectifs)

    effectifs_cumules = calculer_effectifs_cumules(effectifs)
    frequences = calculer_frequences(effectifs, total_effectifs)
    frequences_cumulees = calculer_effectifs_cumules(frequences)

    print("Tableau statistique :")
    print("-" * 97)
    print("|Variable\t|Effectif\t|Effectif cumulé\t|Fréquence\t|Fréquence cumulée\t|")
    print("-" * 97)
    for i in range(len(valeurs)):
        variable = valeurs[i]
        effectif = effectifs[i]
        effectif_cumule = effectifs_cumules[i]
        frequence = frequences[i]
        frequence_cumulee = frequences_cumulees[i]
        print(f"|{variable}\t\t|\t{effectif}\t|\t{effectif_cumule}\t\t|\t{frequence:.2f}\t|\t{frequence_cumulee:.2f}\t\t|")
    print("-" * 97)
    
def afficher_valeurs_centrales(matrice):
    valeurs = matrice[0]
    effectifs = matrice[1]
    total_effectifs = sum(effectifs)
    moyenne = calculer_moyenne(matrice)

    mediane = trouver_mediane(valeurs, effectifs, total_effectifs)
    mode = trouver_mode(valeurs, effectifs)

    print("Valeurs centrales :")
    print(f"Médiane : {mediane}")
    print(f"Mode(s) : {mode}")
    print(f"Moyenne : {moyenne}")

def calculer_moyenne(matrice):
    """Calcule la moyenne d'une variable."""
    somme = 0
    for i in range(len(matrice[0])):
        somme += matrice[0][i]*matrice[1][i]
    return somme / len(matrice[0])

def afficher_valeurs_dispersion(matrice):
    valeurs = matrice[0]
    effectifs = matrice[1]
    total_effectifs = sum(effectifs)

    variance = trouver_variance(valeurs, effectifs, total_effectifs)
    ecart_type = math.sqrt(variance)

    print("Valeurs de dispersion :")
    print(f"Variance : {variance}")
    print(f"Écart-type : {ecart_type}")

def menu_variables_discretes_univariees():
    matrice = lire_matrice(2)

    while True:
        print("\nMenu - Variables discrètes univariées :\n\n")
        print("1 - Afficher le tableau statistique")
        print("2 - Afficher les valeurs centrales")
        print("3 - Afficher les valeurs de dispersion")
        print("4 - Retour")

        choix = input("Choisissez une option : ")

        if choix == '1':
            afficher_tableau_statistique(matrice)
        elif choix == '2':
            afficher_valeurs_centrales(matrice)
        elif choix == '3':
            afficher_valeurs_dispersion(matrice)
        elif choix == '4':
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

def lire_matrice(lignes):
    matrice = []
    for i in range(lignes):
        ligne = input(f"Entrez les valeurs de la ligne {i+1} séparées par des espaces : ")
        valeurs = ligne.split()
        valeurs = [float(valeur) for valeur in valeurs]
        matrice.append(valeurs)
    return matrice

def calculer_effectifs_cumules(effectifs):
    effectifs_cumules = []
    cumul = 0
    for effectif in effectifs:
        cumul += effectif
        effectifs_cumules.append(cumul)
    return effectifs_cumules

def calculer_frequences(effectifs, total_effectifs):
    frequences = []
    for effectif in effectifs:
        frequence = effectif / total_effectifs
        frequences.append(frequence)
    return frequences

def trouver_mediane(valeurs, effectifs, total_effectifs):
    mediane_idx = (total_effectifs + 1) / 2
    somme_effectifs = 0

    for i in range(len(effectifs)):
        somme_effectifs += effectifs[i]
        if somme_effectifs >= mediane_idx:
            return valeurs[i]

def trouver_mode(valeurs, effectifs):
    max_effectif = max(effectifs)
    modes = []

    for i in range(len(effectifs)):
        if effectifs[i] == max_effectif:
            modes.append(valeurs[i])

    return modes

def trouver_variance(valeurs, effectifs, total_effectifs):
    moyenne = sum([valeur * effectif for valeur, effectif in zip(valeurs, effectifs)]) / total_effectifs
    somme_carres_ecarts = sum([(valeur - moyenne) ** 2 * effectif for valeur, effectif in zip(valeurs, effectifs)])
    variance = somme_carres_ecarts / total_effectifs
    return variance