import mon_package.Observateur
import csv
from pyexcel_ods3 import save_data
from collections import OrderedDict
import ezodf


def Mettre_csv_dans_Donnees_ods():
    Liste_fichier_csv=mon_package.Observateur.Observe_csv()
    Liste_fichier_ods=mon_package.Observateur.Observe_ods()
    En_tete=["Nom enfant","Prénom enfant","Repas","PAI","Nom R1","Prénom R1","Tel domicile","Tel pro","Tel port","mail","Nom R2","Prénom R2","Tel domicile R2","Tel pro R2","Tel port R2","Mail R2","Personne urg 1","Personne urg 2","Personne urg 3","Personne urg 4","Personne urg 5","Personne supp 1","Personne supp 2","Personne supp 3","Personne supp 4","Personne supp 5","Arrivé seul perisco matin","depart tap seul","depart seul extra","autorisation photo"]
    x=0
    #Initialisation de ma liste de fichier csv
    x=Liste_fichier_csv.index('cache\\Autorisation_photo.csv')
    Liste_fichier_csv.pop(x)
    x=Liste_fichier_csv.index('cache\\PAI.csv')
    Liste_fichier_csv.pop(x)
    
    
    
    #Initialisation de ma liste de fichier ods
    x=Liste_fichier_ods.index('Reception\\Autorisation_photo.ods')
    Liste_fichier_ods.pop(x)
    x=Liste_fichier_ods.index('Reception\\PAI.ods')
    Liste_fichier_ods.pop(x)
    
    #traitement des donnees
    for fichier_csv in Liste_fichier_csv:
        #print(fichier_csv)
        with open(fichier_csv,newline="") as csvfile:
            spamreader=csv.reader(csvfile,delimiter=',')
            nom_csv=""
            nom_csv=fichier_csv.replace("cache\\","")
            nom_csv=nom_csv.replace(".csv","")
            nom_fichier_ods=""
            #print(nom_csv)
            for fichier_ods in Liste_fichier_ods:
                    
                    if fichier_ods.find(nom_csv)!=-1:
                        nom_fichier_ods=fichier_ods
            nom_fichier_ods=nom_fichier_ods.replace("Reception\\","Donnees/")
            nom_fichier_ods=nom_fichier_ods.replace(nom_csv,nom_csv+"_Donnees")
                        
            Liste_donnees=[]
            Liste_donnees.append(En_tete)
            for Info_enfants in spamreader:
                Liste_donnees.append(Info_enfants)
        
        data=OrderedDict()
        data.update({"Donnees_brute":Liste_donnees})
        save_data(nom_fichier_ods,data)
                
                
            #print(nom_fichier_ods)     
                
def Traiter_pai():

    with open('cache/PAI.csv',newline="") as csvfile:
        spamreader=csv.reader(csvfile,delimiter=',')
        nb_elem=0
        i=0

        for Info_enfants in spamreader:
                nb_elem+=1
        csvfile.seek(0)
        Tableau_pai= ezodf.opendoc('Reception/PAI.ods')

        feuille=Tableau_pai.sheets[0]

        for Info_enfants in spamreader:
            if i==nb_elem:
                break
            else:
                feuille[3+i,1].set_value(Info_enfants[0])
                feuille[3+i,2].set_value(Info_enfants[1])
                feuille[3+i,3].set_value(Info_enfants[2])
                i+=1
        Tableau_pai.save()

def Traiter_photo():

    with open('cache/Autorisation_photo.csv',newline="") as csvfile:
        spamreader=csv.reader(csvfile,delimiter=',')
        nb_elem=0
        i=0

        for Info_enfants in spamreader:
                nb_elem+=1
        csvfile.seek(0)
        Tableau_pai= ezodf.opendoc('Reception/Autorisation_photo.ods')

        feuille=Tableau_pai.sheets[0]

        for Info_enfants in spamreader:
            if i==nb_elem:
                break
            else:
                feuille[3+i,1].set_value(Info_enfants[0])
                feuille[3+i,2].set_value(Info_enfants[1])
                feuille[3+i,3].set_value(Info_enfants[2])
                i+=1
        Tableau_pai.save()

def Traiter_Tableau():
    Liste_fichier_csv=mon_package.Observateur.Observe_csv()
    Liste_fichier_ods=mon_package.Observateur.Observe_ods()
    x=0
    i=0
    Liste_index=[]
    nb_elem=0

    #Initialisation de ma liste de fichier csv
    x=Liste_fichier_csv.index('cache\\Autorisation_photo.csv')
    Liste_fichier_csv.pop(x)
    x=Liste_fichier_csv.index('cache\\PAI.csv')
    Liste_fichier_csv.pop(x)
    
    
    
    #Initialisation de ma liste de fichier ods
    x=Liste_fichier_ods.index('Reception\\Autorisation_photo.ods')
    Liste_fichier_ods.pop(x)
    x=Liste_fichier_ods.index('Reception\\PAI.ods')
    Liste_fichier_ods.pop(x)
    
    for fichier in Liste_fichier_ods:
        if fichier.find("_Donnees.ods")!=-1:
            Liste_index.append(i)
        i+=1
    
    i=0

    for elem in Liste_index:
        Liste_fichier_ods.pop(elem-i)
        i+=1
    
    #Traitement de tableau
    for fichier_csv in Liste_fichier_csv:
        #print(fichier_csv)
        i=0
        nb_elem=0
        with open(fichier_csv,newline="") as csvfile:
            spamreader=csv.reader(csvfile,delimiter=',')
            nom_csv=""
            nom_csv=fichier_csv.replace("cache\\","")
            nom_csv=nom_csv.replace(".csv",".ods")
            nom_fichier_ods=""
            #print(nom_csv)
            for fichier_ods in Liste_fichier_ods:
                    
                    if fichier_ods.find(nom_csv)!=-1:
                        nom_fichier_ods=fichier_ods
            nom_fichier_ods=nom_fichier_ods.replace("\\","/")
             

            Tableau_classe=ezodf.opendoc(nom_fichier_ods)
            

            for Info_enfants in spamreader:
                nb_elem+=1
            csvfile.seek(0)
            for Info_enfants in spamreader:
                feuille=Tableau_classe.sheets[0]
                if i==nb_elem-1:
                    feuille[0,1].set_value(Info_enfants[0])
                    feuille=Tableau_classe.sheets[1]
                    feuille[1,1].set_value(Info_enfants[0])
                    break
                else:
                    feuille[2+i,1].set_value(Info_enfants[0])
                    feuille[2+i,2].set_value(Info_enfants[1])
                    feuille[2+i,3].set_value(Info_enfants[4]+" "+Info_enfants[5]+'\n'+Info_enfants[10]+" "+Info_enfants[11])
                    feuille[2+i,4].set_value(Info_enfants[6]+'\n'+Info_enfants[7]+'\n'+Info_enfants[8]+'\n'+Info_enfants[12]+'\n'+Info_enfants[13]+'\n'+Info_enfants[13])
                    feuille[2+i,5].set_value(Info_enfants[16]+'\n'+Info_enfants[17]+'\n'+Info_enfants[18]+'\n'+Info_enfants[19]+'\n'+Info_enfants[20])
                    feuille[2+i,6].set_value(Info_enfants[21]+'\n'+Info_enfants[22]+'\n'+Info_enfants[23]+'\n'+Info_enfants[24]+'\n'+Info_enfants[24])
                    feuille[2+i,7].set_value(Info_enfants[27])
                    feuille[2+i,8].set_value(Info_enfants[3])
                    feuille=Tableau_classe.sheets[1]
                    feuille[3+i,1].set_value(Info_enfants[0])
                    feuille[3+i,2].set_value(Info_enfants[1])
                    feuille[3+i,3].set_value(Info_enfants[2])

                    
                i+=1
            Tableau_classe.save()
        
            
        
    
    


     

                


                
        
    
    
    

