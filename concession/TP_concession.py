import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath="./exo/fil_rouge/concession/cleaned_autos.csv"

donnees=pd.read_csv(filepath)

# Nombre total de véhicules en vente selon le type de véhicule.
def get_df_type_vehicle(df):
    df_type_vehicle=(
    df.groupby("vehicleType").size()
      .rename("nombre_voiture")
      .reset_index()
      .sort_values(by=['nombre_voiture'])
    )
    print(df_type_vehicle.to_string(index=False),"\n")

    #matplotlib
    plt.style.use("ggplot")
    plt.pie(df_type_vehicle["nombre_voiture"], labels=df_type_vehicle["vehicleType"], autopct='%1.1f%%')
    plt.title("nombre de voiture par type de vehicule")
    plt.show()

# get_df_type_vehicle(donnees)


# Répartition des véhicules en fonction de l'année d'immatriculation
def get_df_year_registration(df):
    df_year_registration=(
    df.groupby("yearOfRegistration").size()
      .rename("nombre_voiture")
      .reset_index()
      .sort_values(by=['yearOfRegistration'])
    )
    df_year_registration=df_year_registration[df_year_registration["yearOfRegistration"]>1980] # retire les annes en dessous de 1980 pour la lisibilite (peu de donnees)
    print(df_year_registration.to_string(index=False),"\n")

    #matplotlib
    plt.style.use("ggplot")
    plt.bar(df_year_registration["yearOfRegistration"], df_year_registration["nombre_voiture"])
    plt.xlabel("type de vehicule")
    plt.ylabel("nombre de voitures")
    plt.title("nombre de voiture par annee d'immmatriculation (1980 - 2015)")
    plt.show()

# get_df_year_registration(donnees)

# Nombre de véhicules par marque
def get_df_brand_vehicle(df):
    df_brand_vehicle=(
    df.groupby("brand").size()
      .rename("nombre_voiture")
      .reset_index()
      .sort_values(by=['nombre_voiture'], ascending=False)
    )
    print(df_brand_vehicle.to_string(index=False),"\n")
    df_max_brand_vehicle=df_brand_vehicle[df_brand_vehicle["nombre_voiture"]>=6000] #selectionne les marque de + de 6000 voitures
    df_min_brand_vehicle=df_brand_vehicle[df_brand_vehicle["nombre_voiture"]<6000] #selectionne les marque de + de 6000 voitures

    #matplotlib
    plt.style.use("ggplot")
    plt.bar(df_max_brand_vehicle["brand"], df_max_brand_vehicle["nombre_voiture"])
    plt.xlabel("marque de vehicule")
    plt.ylabel("nombre de voitures")
    plt.title("nombre de voiture par marque (nombre de voitures > 6000)")
    plt.show()

    plt.bar(df_min_brand_vehicle["brand"], df_min_brand_vehicle["nombre_voiture"])
    plt.xlabel("marque de vehicule")
    plt.xticks(fontsize=6)
    plt.ylabel("nombre de voitures")
    plt.title("nombre de voiture par marque (nombre de voitures < 6000)")
    plt.show()

# get_df_brand_vehicle(donnees)

# Prix moyen des véhicules par type de véhicule et type de boîte de vitesses
def get_df_vtype_gearbox(df):
    df_vtype_gearbox=(
    df.groupby(["vehicleType","gearbox"])["price"].mean()
    .rename("prix_moyen")
    .reset_index()
    .sort_values(by=["vehicleType", 'gearbox'])
    )
    df_manuel_vtype_gearbox=df_vtype_gearbox[df_vtype_gearbox["gearbox"]=="manuell"]#dataframe representant les voitures manuelles
    df_auto_vtype_gearbox=df_vtype_gearbox[df_vtype_gearbox["gearbox"]=="automatik"]#dataframe representant les voitures automatiques
    df_unspecified_vtype_gearbox=df_vtype_gearbox[df_vtype_gearbox["gearbox"]=="Unspecified"]#dataframe representant les voitures de boit de vitesse non specifiee
    print(df_vtype_gearbox.to_string(index=False),"\n")

    #matplotlib
    plt.style.use("ggplot")
    X = df_manuel_vtype_gearbox["vehicleType"]
    Y_manuel=df_manuel_vtype_gearbox["prix_moyen"]
    Y_auto=df_auto_vtype_gearbox["prix_moyen"]
    Y_unspecified=df_unspecified_vtype_gearbox["prix_moyen"]
    
    X_axis = np.arange(len(X)) # cree une abscisse numerique pour chaque groupe de type de vehicule
    
    plt.bar(X_axis - 0.3, Y_manuel, width=0.3, label = 'manuel') #decale le graph de 0.3 vers la gauche
    plt.bar(X_axis + 0, Y_auto, width=0.3, label = 'automatique') #ne decale pas le graph
    plt.bar(X_axis + 0.3, Y_unspecified, width=0.3, label = 'unspecified') #decale le graph de 0.3 vers la droite
    
    plt.xticks(X_axis, X) #renomme chacun des groupe numerique par leur nom correspondant
    plt.xlabel("type de vehicule") 
    plt.ylabel("prix moyen")
    plt.title("prix moyen par type de vehicule et boite de vitesse") 
    plt.legend(["manuelle","automatique","non-specifie"])
    plt.show() 

# get_df_vtype_gearbox(donnees)

# Prix moyen des véhicules selon le type de carburant et le type de boîte de vitesses
def get_df_ctype_gearbox(df):
    df_ctype_gearbox=(
    df.groupby(["fuelType","gearbox"])["price"].mean()
    .rename("prix_moyen")
    .reset_index()
    .sort_values(by=["fuelType", 'gearbox'])
    )
    df_manuel_ctype_gearbox=df_ctype_gearbox[df_ctype_gearbox["gearbox"]=="manuell"]
    df_auto_ctype_gearbox=df_ctype_gearbox[df_ctype_gearbox["gearbox"]=="automatik"]
    df_unspecified_ctype_gearbox=df_ctype_gearbox[df_ctype_gearbox["gearbox"]=="Unspecified"]
    print(df_ctype_gearbox.to_string(index=False),"\n")

    
    #matplotlib
    plt.style.use("ggplot")
    X = df_manuel_ctype_gearbox["fuelType"]
    Y_manuel=df_manuel_ctype_gearbox["prix_moyen"]
    Y_auto=df_auto_ctype_gearbox["prix_moyen"]
    Y_unspecified=df_unspecified_ctype_gearbox["prix_moyen"]

    X_axis = np.arange(len(X))
    
    plt.bar(X_axis - 0.3, Y_manuel, width=0.3, label = 'manuel')
    plt.bar(X_axis + 0, Y_auto, width=0.3, label = 'automatique') 
    plt.bar(X_axis + 0.3, Y_unspecified, width=0.3, label = 'unspecified') 
    
    plt.xticks(X_axis, X) 
    plt.xlabel("type de carburant") 
    plt.ylabel("prix moyen")
    plt.title("prix moyen par type de carburant et boite de vitesse") 
    plt.legend(["manuel","automatique","non-specifie"])
    plt.show() 

# get_df_ctype_gearbox(donnees)


# trouver les 2 marques les plus cheres et les 2 type de vehicules les plus chers parmis ces 2 marques 
def get_max_price_vtype_brand(df):
    df_max_brand=(
    df.groupby("brand")["price"].mean()
    .rename("prix_moyen")
    .reset_index()
    .sort_values(by="prix_moyen", ascending=False)
    .head(2)
    )
    list_max_2_brand=list(df_max_brand["brand"])
    print("2 marques les plus cheres : "+str(list_max_2_brand))

    df_porsche_rover=pd.concat([df[df["brand"]==list_max_2_brand[0]],df[df["brand"]==list_max_2_brand[1]]])

    df_porsche_rover=(
        df_porsche_rover.groupby("vehicleType")["price"].mean()
        .rename("prix_moyen")
        .reset_index()
        .sort_values(by="prix_moyen", ascending=False)
        .head(2)
    )
    list_max_2_vtype=list(df_porsche_rover["vehicleType"])
    print("2 type de vehicule les plus cheres parmis les porshe et land rover : "+str(list_max_2_vtype))

# get_max_price_vtype_brand(donnees)


# trouver les Prix moyens des véhicules par type de véhicule et marque (heatmap)
def get_df_vtype_brand(df):
    df_vtype_brand=(
    df.groupby(["vehicleType","brand"])["price"].mean()
    .rename("prix_moyen")
    .reset_index()
    .sort_values(by=["vehicleType", 'brand'])
    )
    df_vtype_brand=df_vtype_brand.pivot(index="brand", columns="vehicleType",values='prix_moyen')
    df_vtype_brand=df_vtype_brand.fillna(float(0))
    df_vtype_brand=df_vtype_brand.astype('int32')
    df_vtype_brand.style.background_gradient(cmap='Greens') # marche pas
    print(df_vtype_brand)

    #matplotlib
    plt.imshow(df_vtype_brand) 
    plt.xticks(range(len(df_vtype_brand.columns)), df_vtype_brand.columns) 
    plt.yticks(range(len(df_vtype_brand)), df_vtype_brand.index)
    plt.show()

    # seaborn
    import seaborn as sns
    sns.heatmap(df_vtype_brand, annot=True, fmt="d", linewidths=.5, cmap="Blues")
    plt.show()

# get_df_vtype_brand(donnees)
