import mon_package
import mon_package.Observateur
import mon_package.Convertisseur_2
import mon_package.Analyse_txt
import mon_package.Analyse_csv
import mon_package.Convertisseur_ods

if __name__=="__main__":
    
    #Le programme parcours le dossier Fiches_sanitaire pour trouver tous les fichier .pdf et les rangent dans une liste
    Liste_fichiers=mon_package.Observateur.Observe_pdf()
    

    #Convertie les fichier.pdf 1 par 1 en .txt plsu facile a manipuler
    for fichier in Liste_fichiers:
        
        mon_package.Convertisseur_2.pdf_reader(fichier)
    
    Liste_fichiers_txt=mon_package.Observateur.Observe_txt()
    for fichier in Liste_fichiers_txt:
        
        mon_package.Analyse_txt.Analyseur_txt(fichier)
    
    mon_package.Analyse_csv.Analyse_autorisation_photo()
    mon_package.Analyse_csv.Analyse_pai()
    mon_package.Convertisseur_ods.Mettre_csv_dans_Donnees_ods()
    mon_package.Convertisseur_ods.Traiter_pai()
    mon_package.Convertisseur_ods.Traiter_photo()
    mon_package.Convertisseur_ods.Traiter_Tableau()
    #mon_package.Observateur.Nettoie_cache()
    mon_package.Observateur.Nettoie_bak()
    mon_package.Observateur.Nettoie_tmp()

    

    
    
    



