
import math
import discrete_univariate
import discrete_bivariate
import continuous_univariate
import continuous_bivariate

def menu_principal():
    """Affiche le menu principal du programme."""
    print("Menu principal:")
    print("1 - Variables discrètes univariées")
    print("2 - Variables discrètes bivariées")
    print("3 - Variables continues univariées")
    print("4 - Variables continues bivariées")
    print("5 - Sortir")

    while True:
        try:
            choix = int(input("Entrez votre choix (1-5): "))
            if 1 <= choix <= 5:
                return choix
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

if __name__ == "__main__":
    while True:
        choix = menu_principal()

        if choix == 1:
                discrete_univariate.menu_variables_discretes_univariees()

        elif choix == 2:
                discrete_bivariate.menu_variables_discretes_bivariees()

        elif choix == 3:
                continuous_univariate.menu_variables_continue_univariees()

        elif choix == 4:
                continuous_bivariate.menu_variables_continue_bivariees()

        elif choix == 5:
            break

        else:
            print("Choix invalide.")