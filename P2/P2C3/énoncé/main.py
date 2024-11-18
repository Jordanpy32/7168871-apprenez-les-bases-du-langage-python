# Ecrivez vos fonctions ici

def salaire_mensuel(salaire_annuel):
    salaire_mensuel = salaire_annuel / 12
    return salaire_mensuel 

def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire = salaire_mensuel / 4
    return salaire_hebdomadaire

def salaire_horaire(salaire_hebdomadaire, nombre_heures):
    salaire_horaire = salaire_hebdomadaire / nombre_heures
    return salaire_horaire

# Conversion des entrées utilisateur en float
salaire_annuel = float(input("Votre salaire annuel : "))
nombre_heures_de_travaille = float(input("Votre nombre d'heures de travail par semaine : "))

# Calculs
salaire_mensuel_calcule = salaire_mensuel(salaire_annuel)
print(f"Votre salaire mensuel est de {salaire_mensuel_calcule:.2f} euros")

salaire_hebdomadaire_calcule = salaire_hebdomadaire(salaire_mensuel_calcule)
print(f"Votre salaire hebdomadaire est de {salaire_hebdomadaire_calcule:.2f} euros")

salaire_horaire_calcule = salaire_horaire(salaire_hebdomadaire_calcule, nombre_heures_de_travaille)
print(f"Votre salaire horaire est de {salaire_horaire_calcule:.2f} euros")

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
