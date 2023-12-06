import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

filepath_ny="./exo/fil_rouge/bikeshare/cleaned_new_york_city.csv"
filepath_c="./exo/fil_rouge/bikeshare/cleaned_chicago_city.csv"
filepath_w="./exo/fil_rouge/bikeshare/cleaned_washington_city.csv"

df_ny=pd.read_csv(filepath_ny)
df_c=pd.read_csv(filepath_c)
df_w=pd.read_csv(filepath_w)

df_ny["Start Time"]=pd.to_datetime(df_ny["Start Time"], errors='coerce') #transforme les date string en date date et les erreurs en NaD (not a date)
df_ny=df_ny[["Start Time", "Trip Duration", "User Type", "Gender", "Birth Year"]] #selectionne les 6 colonnes pertinentes
df_ny=df_ny.dropna() #retire les nan

df_c["Start Time"]=pd.to_datetime(df_c["Start Time"], errors='coerce')
df_c=df_c[["Start Time", "Trip Duration", "User Type", "Gender", "Birth Year"]]
df_c=df_c.dropna()

df_w["Start Time"]=pd.to_datetime(df_w["Start Time"], errors='coerce')
df_w=df_w[["Start Time", "Trip Duration", "User Type", "Gender", "Birth Year"]]
df_w=df_w.dropna()

# dictionnaire (enum) des villes
villes={
    1 : "new york", 2 : "chicago", 3 : "washington"
}

# dictionnaire (enum) des mois
mois={
    1 : "janvier", 2 : "fevrier", 3 : "mars", 4 : "avril", 5 : "mai", 6 : "juin",
    7 : "juillet", 8 : "aout", 9 : "septembre", 10 : "octobre", 11 : "novembre", 12 : "decembre"
}

# dictionnaire (enum) des jours de la semaine en pandas
jours_semaine={0 : "lundi", 1 : "mardi", 2 : "mercredi", 3 : "jeudi", 4 : "vendredi", 5 : "samedi", 6 : "dimanche"}

#demande a l'utilisateur de choisir une des ville disponible et renvoie son numero correspondant, 0 pour demander a sortir du programme
def menu_ville() :
    s="choissez une ville : \n"
    s+="0 - sortir du programme\n"
    for k,v in villes.items() :
        s+=str(k)+" - "+str(v)+"\n"
    while True :
        print(s)
        choix=int(input())
        if (choix in list(villes.keys())) or choix==0:
            break
    return choix


#renvoie le dataframe correspondant au numero de ville
def load_df(n_ville) : 
    if n_ville==1:
        return df_ny
    elif n_ville==2:
        return df_c
    elif n_ville==3:
        return df_w

# a partir d'un dataframe d'une ville renvoie la liste des mois disponibles
def get_available_month(df) :
    mois_disponibles=pd.DataFrame()
    mois_disponibles["mois"]=df["Start Time"].dt.month #cree une liste des mois de depart disponibles pour cette ville
    mois_disponibles=list(mois_disponibles["mois"].drop_duplicates()) #enleve les doublons et transforme en liste
    mois_disponibles=sorted(mois_disponibles)
    return mois_disponibles

#demande a l'utilisateur de choisir un des mois disponible et renvoie son numero correspondant
def menu_mois(l_mois) :
    s="choissez un mois : \n"
    for m in l_mois :
        if not m :
            break
        s+=str(m)+" - "+str(mois[m])+"\n"
    while True :
        print(s)
        choix=int(input())
        if choix in l_mois :
            break
    return choix


#traitement des donnees
#  - Le jour de la semaine avec le plus d'activité.
def show_jour_activite(df) :
    df_semaine=df
    df_semaine["jour"]=df_semaine["Start Time"].dt.dayofweek
    df_semaine=(df_semaine
        .groupby("jour").size()
        .rename("nombre_departs")
        .reset_index()
        .sort_values("nombre_departs", ascending=False)
        .head(1)
    )
    jour_activite=jours_semaine[int(df_semaine["jour"].iloc[0])]
    print(f"jour ayant le plus d'activité : {jour_activite}")


#  - L'heure de démarrage la plus courante.
def show_heure_activite(df) :
    df_heure=df
    df_heure["heure"]=df_heure["Start Time"].dt.hour
    df_semaine=(df_heure
        .groupby("heure").size()
        .rename("nombre_departs")
        .reset_index()
        .sort_values("nombre_departs", ascending=False)
        .head(1)
    )
    heure_activite=int(df_semaine["heure"].iloc[0])
    print(f"heure de demarrage ayant le plus de depart : {heure_activite}h")


#  - La durée de voyage moyen sur la période (mois).
def show_moy_duree(df) :
    df_duree=df
    df_duree=df_duree["Trip Duration"].mean()

    def m_to_string(m) :
    #convertit un nombre de minute en affichage h:mm
        if m<60 :
            return str(m)+" minutes"
        else :
            h=int(m//60)
            m=int(m%60)
            return f"{h}h{m:02d}"
    print(f"duree moyenne des voyages sur la periode : {m_to_string(df_duree)}")


#  - Le total pour chaque catégorie de User.
def show_cat_utilisateur(df) :
    df_cat_utilisateur=df
    df_cat_utilisateur=(df_cat_utilisateur
        .groupby("User Type").size()
        .rename("nombre_utilisateurs")
        .reset_index()
    )
    print("\nnombre d'utilisateur par type d'utilisateur : ")
    print(df_cat_utilisateur.to_string(index=False), "\n")


#  - Le nombre total de femmes et d'hommes sur la période.
def show_hf(df) :
    df_hf=df
    df_hf=df_hf[df_hf["Gender"]!=2]
    df_hf=(df_hf
        .groupby("Gender").size()
        .rename("nombre_utilisateurs")
        .reset_index()
    )
    df_hf["Gender"]=df_hf["Gender"].replace({0 : "Femme", 1 : "Homme"})
    print("nombre d'utilisateur par genre : ")
    print(df_hf.to_string(index=False), "\n")


#  - L'année de naissance la plus ancienne.
def show_min_annee(df) :
    df_min_annee=df
    df_min_annee=df_min_annee["Birth Year"].min()
    print(f"annee de naissance la plus ancienne : {int(df_min_annee)}")


#  - L'année de naissance la plus récente.
def show_max_annee(df) :
    df_max_annee=df
    df_max_annee=df_max_annee["Birth Year"].max()
    print(f"annee de naissance la plus recente : {int(df_max_annee)}")


#  - L'année de naissance la plus courante sur la période (avec le nombre d'occurence).
def show_courante_annee(df) :
    df_courante_annee=df
    df_courante_annee=(df_courante_annee
        .groupby("Birth Year").size()
        .rename("nombre_utilisateurs")
        .reset_index()
        .sort_values("nombre_utilisateurs", ascending=False)
        .head(1)
    )
    annee=df_courante_annee["Birth Year"].iloc[0]
    nombre=df_courante_annee["nombre_utilisateurs"].iloc[0]
    print(f"annee de naissance la plus courante : {int(annee)} ({nombre} personnes)")

#MAIN
while True :
    selected_city=menu_ville() #menu_ville affiche une liste de choix et renvoie le numero de ville chois (0 pour sortir)
    if selected_city==0 :
        break
    donnees=load_df(selected_city) #load_df prend le numero de ville en entree et renvoie le dataframe corresponsant
    mois_disponibles=get_available_month(donnees) #get_available_month prend le dataframe d'une ville en entree et renvoie la liste des numero de mois disponible
    selected_month=menu_mois(mois_disponibles) #menu_mois prend une liste de mois en entree et renvoie un nombre de cette liste choisi par l'utilisateur
    donnees=donnees[donnees["Start Time"].dt.month==selected_month] # filtre pour ne garder que le mois selectionne dans le dataframe
    print(f"donnes pour la ville de {villes[selected_city]} pour le mois de {mois[selected_month]} : ")
    show_jour_activite(donnees)
    show_heure_activite(donnees)
    show_moy_duree(donnees)
    show_cat_utilisateur(donnees)
    show_hf(donnees)
    show_min_annee(donnees)
    show_max_annee(donnees)
    show_courante_annee(donnees)
