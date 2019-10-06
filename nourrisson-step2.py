# On importe les modules qui vont nous permettre de traiter les données

# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as plt
# csv pour lire les fichiers de données
import csv

liste_poids= []
liste_taille= []
liste_perim=[]
liste_mois=[]
liste_mois_light_poids=[]
liste_poids_5=[]
liste_poids_25=[]
liste_poids_50=[]
liste_poids_75=[]
liste_poids_95=[]
liste_mois_light_taille=[]
liste_taille_5=[]
liste_taille_25=[]
liste_taille_50=[]
liste_taille_75=[]
liste_taille_95=[]
liste_mois_light_perim=[]
liste_perim_5=[]
liste_perim_25=[]
liste_perim_50=[]
liste_perim_75=[]
liste_perim_95=[]


# Récupération des mesures dans les fichiers à faire
#fichier mesures 
# fname = "mesures.csv"
file = open('/home/bnp-renault-013/Bureau/python/python-project-trackbaby/mesures.csv', "r",newline='')

try:
    reader = csv.reader(file, delimiter = ';')
    next(reader, None)
    for row in reader:
        liste_mois.append(row[0])
        liste_poids.append(row[1])
        liste_taille.append(row[2])
        liste_perim.append(row[3])
        

finally:
    file.close()

#fichier poids filles
file = open('/home/bnp-renault-013/Bureau/python/python-project-trackbaby/constantes-nourrissons-light/poids-age-fille-0-60-light.csv', "r",newline='')

try:
    reader = csv.reader(file, delimiter = ';')
    next(reader, None) #permet de sauter les titres
    for row in reader:
        liste_mois_light_poids.append(int(row[0]))
        liste_poids_5.append(float(row[1]))
        liste_poids_25.append(float(row[2]))
        liste_poids_50.append(float(row[3]))
        liste_poids_75.append(float(row[4]))
        liste_poids_95.append(float(row[5]))
        

finally:
    file.close()

file = open('/home/bnp-renault-013/Bureau/python/python-project-trackbaby/constantes-nourrissons-light/taille-age-fille-0-60-light.csv', "r",newline='')

try:
    reader = csv.reader(file, delimiter = ';')
    next(reader, None) #permet de sauter les titres
    for row in reader:
        liste_mois_light_taille.append(int(row[0]))
        liste_taille_5.append(float(row[1]))
        liste_taille_25.append(float(row[2]))
        liste_taille_50.append(float(row[3]))
        liste_taille_75.append(float(row[4]))
        liste_taille_95.append(float(row[5]))
        

finally:
    file.close()    

file = open('/home/bnp-renault-013/Bureau/python/python-project-trackbaby/constantes-nourrissons-light/perim-cra-age-fille-0-60-light.csv', "r",newline='')

try:
    reader = csv.reader(file, delimiter = ';')
    next(reader, None) #permet de sauter les titres
    for row in reader:
        liste_mois_light_perim.append(int(row[0]))
        liste_perim_5.append(float(row[1]))
        liste_perim_25.append(float(row[2]))
        liste_perim_50.append(float(row[3]))
        liste_perim_75.append(float(row[4]))
        liste_perim_95.append(float(row[5]))
        

finally:
    file.close()        

# Affichage des graphiques à faire

#graphiques poids
plt.subplot(1,3,1)
plt.ylabel('Poids en kg')
plt.xlabel('Age en mois')
# 
indic = 0
indic_const = 0
for mois in liste_mois:
    poids = liste_poids[indic]
    plt.scatter (mois,poids, color='black')  

plt.plot (liste_mois_light_poids,liste_poids_5, color = 'blue', label = '5%') 
plt.plot (liste_mois_light_poids,liste_poids_25, color = 'orange', label ='25%') 
plt.plot (liste_mois_light_poids,liste_poids_50, color = 'green', label = '50%') 
plt.plot (liste_mois_light_poids,liste_poids_75, color = 'red', label = '75%') 
plt.plot (liste_mois_light_poids,liste_poids_95, color = 'purple', label = '95%') 
plt.legend (loc = 'upper left')

#graphiques taille
plt.subplot(1,3,2)
plt.ylabel('Taille en cm')
plt.xlabel('Age en mois')
month = 0
# 
indic = 0
for mois in liste_mois:
    taille = liste_taille[indic]
    plt.scatter (mois,taille, color = 'black')  
    indic = indic +1
plt.plot (liste_mois_light_taille,liste_taille_5, color = 'blue', label = '5%') 
plt.plot (liste_mois_light_taille,liste_taille_25, color = 'orange', label ='25%') 
plt.plot (liste_mois_light_taille,liste_taille_50, color = 'green', label = '50%') 
plt.plot (liste_mois_light_taille,liste_taille_75, color = 'red', label = '75%') 
plt.plot (liste_mois_light_taille,liste_taille_95, color = 'purple', label = '95%')     
plt.legend (loc = 'upper left')

#graphique périmètre cranien

plt.subplot(1,3,3)
plt.ylabel('périmètre cranien en cm')
plt.xlabel('Age en mois')
month = 0
# 
indic = 0
for mois in liste_mois:
    perim = liste_perim[indic]
    plt.scatter (mois,perim, color='black')  
    indic = indic +1   
plt.plot (liste_mois_light_perim,liste_perim_5, color = 'blue', label = '5%') 
plt.plot (liste_mois_light_perim,liste_perim_25, color = 'orange', label ='25%') 
plt.plot (liste_mois_light_perim,liste_perim_50, color = 'green', label = '50%') 
plt.plot (liste_mois_light_perim,liste_perim_75, color = 'red', label = '75%') 
plt.plot (liste_mois_light_perim,liste_perim_95, color = 'purple', label = '95%')      
plt.legend (loc = 'upper left')

plt.show()


