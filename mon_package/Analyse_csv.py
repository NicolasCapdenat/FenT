import csv
import mon_package.Observateur

def Analyse_pai():
    Liste_fichier=mon_package.Observateur.Observe_csv()
    
    with open('cache/PAI.csv', 'w', newline='') as csvfile_w:
        Pai_writer=csv.writer(csvfile_w, delimiter=',')
        
        for fichier in Liste_fichier:
            classe=""
            if fichier.find("PAI")==-1 and fichier.find("photo")==-1:
                with open(fichier, newline='') as csvfile:
                    freader = csv.reader(csvfile, delimiter=',')
                    
                    
                    classe=fichier.replace("cache\\","")
                    classe=classe.replace(".csv","")
                    for row in freader:
                        i=0
                        for nb_elem in row:
                            i+=1       
                        Nom_prenom_classe=[]
                        if i>3 and row[3].find("OUI")!=-1:
                            
                            Nom_prenom_classe.append(row[0])
                            Nom_prenom_classe.append(row[1])
                            Nom_prenom_classe.append(classe)
                            
                            Pai_writer.writerow(Nom_prenom_classe)
                            

def Analyse_autorisation_photo():
    Liste_fichier=mon_package.Observateur.Observe_csv()
    
    with open('cache/Autorisation_photo.csv', 'w', newline='') as csvfile_w:
        Autorisation_writer=csv.writer(csvfile_w, delimiter=',')
        
        for fichier in Liste_fichier:
            classe=""
            if fichier.find("PAI")==-1 and fichier.find("photo")==-1:
                with open(fichier, newline='') as csvfile:
                    freader = csv.reader(csvfile, delimiter=',')
                    
                    
                    classe=fichier.replace("cache\\","")
                    classe=classe.replace(".csv","")
                    for row in freader:
                        i=0       
                        Nom_prenom_classe=[]
                        for nb_elem in row:
                            i+=1  
                        if i>3 and (row[29].find("NON")!=-1 or row[29].find("A verifier")!=-1):
                            
                            Nom_prenom_classe.append(row[0])
                            Nom_prenom_classe.append(row[1])
                            Nom_prenom_classe.append(classe)
                            
                            Autorisation_writer.writerow(Nom_prenom_classe)
                            
                    
    




        