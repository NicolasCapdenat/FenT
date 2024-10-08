import csv

def Debut_de_fiche(ligne):
    if ligne.find("FICHE SANITAIRE ET DE LIAISON")!=-1:
        return True
    else:
        return False
    
def Responsable_legal_2_exist(ligne):
    i=0
    n=0
    Erreur_ligne=""
    Erreur_ligne=ligne
    ligne=ligne.rsplit()
    try:
        ligne.pop(0)
        ligne.pop(0)

        for elem in ligne:
            if elem=="NOM":
                break
            else:
                n+=1
        while i<n:
            ligne.pop(0)
            i+=1
        
        nb_elem=0
        for elem in ligne:
            nb_elem+=1
        
        if nb_elem>2:
            
            return True
        else:
            
            return False
    except:
        print("Erreur dans la fonction Responsable_legal_2_exist",'\n',"Voici la chaine de caractère :",Erreur_ligne)
        return "Erreur_RESPONSABLE2"
    
def Numero_responsable_legal2(ligne):
    i=0
    n=0
    Erreur_ligne=""
    Erreur_ligne=ligne
    ligne=ligne.rsplit()
    try:
        ligne.pop(0)
        ligne.pop(0)
        ligne.pop(0)
        
        nb_elem=0
        for elem in ligne:
            nb_elem +=1
        for elem in ligne:
            if elem=="Tél":
                break
            else:
                n+=1
        
        
        
        while i<n:
            ligne.pop(0)
            i+=1
    
        ligne.pop(0)
        ligne.pop(0)
        ligne.pop(0)
        if not(ligne):
            return "Pas de tel"
        else:
            tel="".join(ligne)
            return tel
    except:
        print("Erreur dans la fonction Numéro_responsable_legal2",'\n',"Voici la chaine de caractère :",Erreur_ligne)
        return "Erreur_NUMEROS_R2"  
    
def Nom_enfant(ligne):
    i=0
    ligne=ligne.split()
    #print(ligne)
    nom_enfant=""
    try:

        for mot in ligne:
            #print(mot)
            if mot=="NOM":
                nom_enfant=ligne[i+2]
                if ligne[i+3]!="Prénom":
                    nom_enfant=nom_enfant+" "+ligne[i+3]
                    if ligne[i+4]!="Prénom":
                        nom_enfant=nom_enfant+" "+ligne[i+4]
            i=i+1
        
        return nom_enfant
    except:
        print("Erreur dans la fonction Nom_enfant",'\n',"Voici la chaine de caractère :",ligne)
        return "Erreur_NOM"

def Prenom_enfant(ligne):
    i=0
    prenom_enfant=""
    ligne=ligne.split()
    nb_elem=0
    for elem in ligne:
        nb_elem +=1
    
    try:

        for mot in ligne:
            #print(mot)
            if mot=="Prénom":
                prenom_enfant=ligne[i+2]
                if (i+3)<nb_elem:
                    prenom_enfant=prenom_enfant+" "+ligne[i+3]
                    if (i+4)<nb_elem:
                        prenom_enfant=prenom_enfant+" "+ligne[i+4]
            i=i+1
        
        return prenom_enfant
    except:
        print("Erreur dans la fonction Prenom_enfant",'\n',"Voici la chaine de caractère :",ligne)
        return "Erreur_PRENOM"

def Repas_enfant(ligne):
    if ligne.find("Classique")!=-1:
        return "Classique"
    elif ligne.find("Sans")!=-1:
        return "Sans porc"
    else:
        return "Pas spécifié"

def Nom_responsable_legal1(ligne):
    i=0
    ligne=ligne.split()
    #print(ligne)
    nom_responsable=""
    try:
        for mot in ligne:
            #print(mot)
            if mot=="NOM":
                nom_responsable=ligne[i+2]
                if ligne[i+3]!="NOM":
                    nom_responsable=nom_responsable+" "+ligne[i+3]
                    if ligne[i+4]!="NOM":
                        nom_responsable=nom_responsable+" "+ligne[i+4]
            i=i+1
            return nom_responsable
    except:
        print("Erreur dans la fonction Nom_responsable_legal1",'\n',"Voici la chaine de caractère :",ligne)
        return "Erreur_NOM_R1"

def Nom_responsable_legal2(ligne):
    i=0
    n=0
    Erreur_ligne=""
    Erreur_ligne=ligne
    ligne=ligne.rsplit()
    nb_elem=0
    try:

        for elem in ligne:
            nb_elem +=1
        ligne.pop(0)
        ligne.pop(0)

        for elem in ligne:
            if elem=="NOM":
                break
            else:
                n+=1
        while i<n:
            ligne.pop(0)
            i+=1
        
        ligne.pop(0)
        ligne.pop(0)
        
        nb_elem=0
        for elem in ligne:
            nb_elem +=1
        if nb_elem==1:
            return ligne[0]
        else:
            nom=" ".join(ligne)
            return nom
    except:
        print("Erreur dans la fonction Nom_responsable_legal2",'\n',"Voici la chaine de caractère :",Erreur_ligne)
        return "Erreur_NOM_R2"
    
def Prenom_responsable_legal1(ligne):
    i=0
    ligne=ligne.split()
    prenom_responsable=""
    try:

        for mot in ligne:
            #print(mot)
            if mot=="Prénom":
                if i==0:
                    prenom_responsable=ligne[i+2]
                    if ligne[i+3]!="Prénom":
                        prenom_responsable=prenom_responsable+" "+ligne[i+3]
                        if ligne[i+4]!="Prénom":
                            prenom_responsable=prenom_responsable+" "+ligne[i+4]
            i=i+1
        return prenom_responsable
    except:
        print("Erreur dans la fonction Prenom_responsable_legal1",'\n',"Voici la chaine de caractère :",ligne)
        return "Erreur_PRENOM_R1"

def Prenom_responsable_legal2(ligne):
    i=0
    n=0
    nb_elem=0
    Erreur_ligne=""
    Erreur_ligne=ligne
    ligne=ligne.rsplit()
    try:
        for elem in ligne:
            nb_elem +=1
        ligne.pop(0)
        ligne.pop(0)

        for elem in ligne:
            if elem=="Prénom":
                break
            else:
                n+=1
        while i<n:
            ligne.pop(0)
            i+=1
        
        ligne.pop(0)
        ligne.pop(0)

        nb_elem=0
        for elem in ligne:
            nb_elem +=1
        if nb_elem==1:
            return ligne[0]
        else:
            prenom=" ".join(ligne)
            return prenom
    except:
        print("Erreur dans la fonction Prenom_responsable_legal2",'\n',"Voici la chaine de caractère :",Erreur_ligne)
        return "Erreur_PRENOM_R2"

def Tel_domicile_responsable_legal1(ligne):
    i=0
    Erreur_ligne=""
    Erreur_ligne=ligne
    ligne=ligne.rsplit()
    try:
        num=""
        nb_elem=0
        for elem in ligne:
            if nb_elem<3:
                ligne.pop(0)
            
            nb_elem +=1
        
        if nb_elem>3 and ligne[0].isdigit()==True:
            if ligne[0].count("")==3:
                for elem in ligne:
                    if (i+1)<nb_elem and ligne[i].isdigit()==True and (ligne[i+1].isdigit()==True or ligne[i+1]=='Tél'):
                        num=num+elem
                    
                    i+=1
                
                return num    
            else:
                    
                    return ligne[0]
        else:
            return "Pas de numéro"
    except:
        print("Erreur dans la fonction Tel_domicile_responsable_legal1",'\n',"Voici la chaine de caractère :",Erreur_ligne)
        return "Erreur_TEL_DOMICILE_R1"   
  
def Tel_professionnel_responsable_legal1(ligne):     
    i=0
    Erreur_ligne=""
    Erreur_ligne=ligne
    ligne=ligne.rsplit()
    try:
        num=""
        nb_elem=0
        for elem in ligne:
            if nb_elem<3:
                ligne.pop(0)
            
            nb_elem +=1
        
        if nb_elem>3 and ligne[0].isdigit()==True:
            if ligne[0].count("")==3:
                for elem in ligne:
                    if (i+1)<nb_elem and ligne[i].isdigit()==True and (ligne[i+1].isdigit()==True or ligne[i+1]=='Tél'):
                        num=num+elem
                    
                    i+=1
                
                return num    
            else:
                    
                    return ligne[0]
        else:
            return "Pas de numéro"
    except:
        print("Erreur dans la fonction Tel_professionnel_responsable_legal1",'\n',"Voici la chaine de caractère :",Erreur_ligne)
        return "Erreur_TEL_PRO_R1"  
   
def Tel_portable_responsable_legal1(ligne): 
    i=0
    Erreur_ligne=""
    Erreur_ligne=ligne
    ligne=ligne.rsplit()
    try:
        num=""
        nb_elem=0
        for elem in ligne:
            if nb_elem<3:
                ligne.pop(0)
            
            nb_elem +=1
        
        if nb_elem>3 and ligne[0].isdigit()==True:
            if ligne[0].count("")==3:
                for elem in ligne:
                    if (i+1)<nb_elem and ligne[i].isdigit()==True and (ligne[i+1].isdigit()==True or ligne[i+1]=='Tél'):
                        num=num+elem
                    
                    i+=1
                
                return num    
            else:
                    
                    return ligne[0]
        else:
            return "Pas de numéro"
    except:
        print("Erreur dans la fonction Tel_portable_responsable_legal1",'\n',"Voici la chaine de caractère :",Erreur_ligne)
        return "Erreur_TEL_POR_R1"  

def Mail_responsable_legal1(ligne):
    Erreur_ligne=""
    Erreur_ligne=ligne
    ligne=ligne.rsplit()
    try:
        ligne.pop(0)
        ligne.pop(0)
        return ligne[0]
    except:
        print("Erreur dans la fonction Mail_responsable_legal1",'\n',"Voici la chaine de caractère :",Erreur_ligne)
        return "Erreur_MAIL_R1"

def Mail_responsable_legal2(ligne):
    Erreur_ligne=""
    Erreur_ligne=ligne
    ligne=ligne.rsplit()

    try:
    
        ligne.pop(0)
        ligne.pop(0)
        if ligne[0]!="Mél":
            ligne.pop(0)
        ligne.pop(0)
        ligne.pop(0)
        if not(ligne):
            return "pas de mail"
        else:
            return ligne[0]
    except:
        print("Erreur dans la fonction Mail_responsable_legal2",'\n',"Voici la chaine de caractère :",Erreur_ligne)
        return "Erreur_MAIL_R2"

def Aller_nom_prenom_enfant(txt_path,depart):

    with open(txt_path, 'r', encoding='utf8') as txt_file:
        i=0
        if depart==0:
            tligne=txt_file.readline()
            tligne=txt_file.readline()
            tligne=txt_file.readline()
            tligne=txt_file.readline()
            
            return tligne
            
        while i<depart:
            tligne=txt_file.readline()
            i=i+1
            if i==depart:
                tligne=txt_file.readline()
        
        i=0
        tligne=txt_file.readline()
        tligne=txt_file.readline()
        tligne=txt_file.readline()
    
    return tligne
    
def Aller_repas(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        i=0
        if depart==0:
            while i<9:
                ligne=txt_file.readline()
                i+=1
            
            return ligne
        i=0
        while i<depart:
            ligne=txt_file.readline()
            i+=1
            if i==depart:
                ligne=txt_file.readline()

        i=0
        while i<8:
            ligne=txt_file.readline()
            i+=1
        return ligne

def Aller_nom_responsable_legaux(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        i=0
        if depart==0:
            while i<11:
                ligne=txt_file.readline()
                i+=1
            return ligne
        i=0
        while i<depart:
            ligne=txt_file.readline()
            i+=1
            if i==depart:
                ligne=txt_file.readline()
        i=0
        while i<10:
            ligne=txt_file.readline()
            i+=1
        return ligne

def Aller_prenom_responsable_legaux(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        i=0
        if depart==0:
            while i<12:
                ligne=txt_file.readline()
                i+=1
            return ligne
        i=0
        while i<depart:
            ligne=txt_file.readline()
            i+=1
            if i==depart:
                ligne=txt_file.readline()
        
        i=0
        while i<11:
            if i>5 and ligne.find("Prénom")!=-1:
                
                return ligne
            else:
                ligne=txt_file.readline()
                i+=1
            
        return ligne

def Aller_tel_domicile(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        i=0
        if depart==0:
            while i<13:
                ligne=txt_file.readline()
                i+=1
            return ligne
        i=0
        while i<depart:
            ligne=txt_file.readline()
            i+=1
            if i==depart:
                ligne=txt_file.readline()
        i=0
        while i<16:
            if ligne.find("domicile")!=-1:
                return ligne
            else:
                ligne=txt_file.readline()
                i+=1
        return ligne
    
def Aller_tel_pro(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        i=0
        if depart==0:
            while i<14:
                ligne=txt_file.readline()
                i+=1
            return ligne
        i=0
        while i<depart:
            ligne=txt_file.readline()
            i+=1
            if i==depart:
                ligne=txt_file.readline()
        i=0
        while i<16:
            if ligne.find("professionnel")!=-1:
                return ligne
            else:
                ligne=txt_file.readline()
                i+=1
        return ligne

def Aller_tel_por(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        i=0
        if depart==0:
            while i<15:
                ligne=txt_file.readline()
                i+=1
            return ligne
        i=0
        while i<depart:
            ligne=txt_file.readline()
            i+=1
            if i==depart:
                ligne=txt_file.readline()
        i=0
        while i<16:
            if ligne.find("portable")!=-1:
                return ligne
            else:
                ligne=txt_file.readline()
                i+=1
        return ligne

def Aller_cas_urgence_I(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        fichier_entier=txt_file.readlines()
        n_lignes=len(fichier_entier)
        #print(n_lignes)
        txt_file.seek(0)
        i=0
        while i!=depart:
            ligne=txt_file.readline()
            i+=1
        
        while i<n_lignes:
            ligne=txt_file.readline()
            if ligne.find("prévenues")!=-1:
                ligne=txt_file.readline()
                
                return i
            else:
                i+=1

def Aller_cas_urgence_S(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        fichier_entier=txt_file.readlines()
        n_lignes=len(fichier_entier)
        #print(n_lignes)
        txt_file.seek(0)
        i=0
        while i!=depart:
            ligne=txt_file.readline()
            i+=1
        
        while i<n_lignes:
            ligne=txt_file.readline()
            if ligne.find("prévenues")!=-1:
                ligne=txt_file.readline()
                
                return ligne
            else:
                i+=1
              
def Aller_autres_personne_I(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        fichier_entier=txt_file.readlines()
        n_lignes=len(fichier_entier)
        #print(n_lignes)
        txt_file.seek(0)
        i=0
        while i!=depart:
            ligne=txt_file.readline()
            i+=1
        
        while i<n_lignes:
            ligne=txt_file.readline()
            if ligne.find("J’autorise d’autres personnes")!=-1:
                ligne=txt_file.readline()
                
                return i
            else:
                i+=1

def Aller_autres_personne_S(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        fichier_entier=txt_file.readlines()
        n_lignes=len(fichier_entier)
        #print(n_lignes)
        txt_file.seek(0)
        i=0
        while i!=depart:
            ligne=txt_file.readline()
            i+=1
        
        while i<n_lignes:
            ligne=txt_file.readline()
            if ligne.find("J’autorise d’autres personnes")!=-1:
                ligne=txt_file.readline()
                
                return ligne
            else:
                i+=1

def Aller_autorisations_I(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        fichier_entier=txt_file.readlines()
        n_lignes=len(fichier_entier)
        #print(n_lignes)
        txt_file.seek(0)
        i=0
        while i!=depart:
            ligne=txt_file.readline()
            i+=1
        
        while i<n_lignes:
            ligne=txt_file.readline()
            if ligne.find("périscolaire le")!=-1:
                
                
                return i
            else:
                i+=1

def Aller_autorisations_S(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        fichier_entier=txt_file.readlines()
        n_lignes=len(fichier_entier)
        #print(n_lignes)
        txt_file.seek(0)
        i=0
        while i!=depart:
            ligne=txt_file.readline()
            i+=1
        
        while i<n_lignes:
            ligne=txt_file.readline()
            if ligne.find("périscolaire le matin")!=-1:
                
                
                return ligne
            else:
                i+=1

def Aller_autorisation_photo(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        fichier_entier=txt_file.readlines()
        n_lignes=len(fichier_entier)
        #print(n_lignes)
        txt_file.seek(0)
        i=0
        while i!=depart:
            ligne=txt_file.readline()
            i+=1
        
        while i<n_lignes:
            ligne=txt_file.readline()
            
            if ligne.find("ou dans le futur.")!=-1:
                
                ligne=txt_file.readline()
                if ligne.find("OUI")!=-1:
                    return "OUI"
                else:
                    return "NON"
            else:
                i+=1
        return "A verifier"

def Aller_mail(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        i=0
        if depart==0:
            while i<16:
                ligne=txt_file.readline()
                i+=1
            return ligne
        i=0
        while i<depart:
            ligne=txt_file.readline()
            i+=1
            if i==depart:
                ligne=txt_file.readline()
        i=0
        while i<15:
            ligne=txt_file.readline()
            i+=1
        return ligne

def Aller_pai(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        i=0
        if depart==0:
            while i<28:
                ligne=txt_file.readline()
                i+=1
            
            return ligne
        i=0
        while i<depart:
            ligne=txt_file.readline()
            i+=1
            if i==depart:
                ligne=txt_file.readline()
        #print(ligne)
        i=0
        while i<35:
            
            if ligne.find("par le médecin")!=-1:
                
                ligne=txt_file.readline()
                return ligne
            
            ligne=txt_file.readline()
            i+=1
        
        return ligne

def Personne_en_cas_urgence(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        i=0
        try:

            while i<depart+4:
                ligne=txt_file.readline()
                i+=1
            Liste_personne=[]
            Liste_personne.append(ligne)
            i=0
            while i<5:
                ligne=txt_file.readline()
                if ligne.find("AUTRES")!=-1:
                    break
                else:
                    Liste_personne.append(ligne)
                i+=1
            i=0
            for elem in Liste_personne:
                Liste_personne[i]=Liste_personne[i].replace("\xa0"," ")
                Liste_personne[i]=Liste_personne[i].replace("\n","")
                i+=1
            
            return Liste_personne
        except:
            Erreur=[]
            Erreur.append("Erreur_A_VERIFIER")
            Erreur.append("Erreur_A_VERIFIER")
            Erreur.append("Erreur_A_VERIFIER")
            Erreur.append("Erreur_A_VERIFIER")
            Erreur.append("Erreur_A_VERIFIER")
            print("Erreur dans la fonction Autorisation")
            return Erreur

def Autorisation(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        i=0
        x=0
        try:

            while i<depart+2:
                ligne=txt_file.readline()
                i+=1
            
            Liste_personne=[]
            if ligne.find("l’accueil périscolaire")==-1:
                
                Liste_personne.append(ligne)
                ligne=txt_file.readline()
                ligne=txt_file.readline()
            else:
                Liste_personne.append("A verifier")
                ligne=txt_file.readline()
            
            
            if ligne.find("seul l’accueil extras")==-1:
                
                Liste_personne.append(ligne)
                ligne=txt_file.readline()
                ligne=txt_file.readline()
            else:
                Liste_personne.append("A verifier")
                ligne=txt_file.readline()
            if ligne.find("Pour Dijon Sport")!=-1:
                
                x=ligne.find("Pour Dijon Sport")
                Liste_personne.append("A verifier")
            else:
                Liste_personne.append(ligne)

            i=0
            for elem in Liste_personne:
                Liste_personne[i]=Liste_personne[i].replace("\xa0"," ")
                Liste_personne[i]=Liste_personne[i].replace("\n","")
                i+=1

            return Liste_personne
        except:
            Erreur=[]
            Erreur.append("Erreur_A_VERIFIER")
            Erreur.append("Erreur_A_VERIFIER")
            Erreur.append("Erreur_A_VERIFIER")
            print("Erreur dans la fonction Autorisation")
            return Erreur
            
def Personne_autre(txt_path,depart):
    with open(txt_path, 'r', encoding='utf8') as txt_file:
        i=0
        try:

            while i<depart+6:
                ligne=txt_file.readline()
                i+=1
            
            Liste_personne=[]
            Liste_personne.append(ligne)
            i=0
            while i<5:
                ligne=txt_file.readline()
                if ligne.find("Parents séparés")!=-1:
                    break
                else:
                    Liste_personne.append(ligne)
                i+=1
            
            i=0
            for elem in Liste_personne:
                Liste_personne[i]=Liste_personne[i].replace("\xa0"," ")
                Liste_personne[i]=Liste_personne[i].replace("\n","")
                i+=1

            return Liste_personne
        
        except:
            Erreur=[]
            Erreur.append("Erreur_A_VERIFIER")
            Erreur.append("Erreur_A_VERIFIER")
            Erreur.append("Erreur_A_VERIFIER")
            Erreur.append("Erreur_A_VERIFIER")
            Erreur.append("Erreur_A_VERIFIER")
            print("Erreur dans la fonction Autorisation")
            return Erreur

def Aller_maladie(txt_path,depart):
    try:

        with open(txt_path, 'r', encoding='utf8') as txt_file:
            i=0
            ligne=""
            while i<depart:
                ligne=txt_file.readline()
                i+=1
                if i==depart:
                    ligne=txt_file.readline()
            
            i=0
            while i<35:
                
                if ligne.find("période")!=-1 and ligne.find("évoluant")!=-1:
                    
                    ligne=txt_file.readline()
                    
                    return ligne
                
                ligne=txt_file.readline()
                i+=1
            
            return "A vérifier"
    except:
        print("ERREUR a la fonction qui renvoie la ligne des maladies Aller_maladie")
        return "ERREUR MALADIE"

def Aller_lunette_appareillage(txt_path,depart):
    try:

        with open(txt_path, 'r', encoding='utf8') as txt_file:
            i=0
            ligne=""
            Liste_ligne=[]
            while i<depart:
                ligne=txt_file.readline()
                i+=1
                if i==depart:
                    ligne=txt_file.readline()
            
            i=0
            A_trouver=False
            
            while i<35:
                
                if ligne.find("appareillage")!=-1 and ligne.find("lunettes")!=-1 and A_trouver==False:
                    ligne=txt_file.readline()
                    Liste_ligne.append(ligne)
                    A_trouver=True
                elif A_trouver==True:
                    if ligne.find("urgence")!=-1 and ligne.find("joignable")!=-1:
                        nb_elem=0
                        for elem in Liste_ligne:
                            nb_elem+=1
                        if nb_elem==1:
                            return Liste_ligne[0]
                        else:
                            ligne=" ".join(Liste_ligne)
                            return ligne
                    else:
                        Liste_ligne.append(ligne)
                ligne=txt_file.readline()
                i+=1
            
            return "A Verifier"
    except:
        print("ERREUR a la fonction qui renvoie la ligne des lunettes/appareillage")
        return "ERREUR LUNETTE"


def Aller_personne_urg2(txt_path,depart):
    try:

        with open(txt_path, 'r', encoding='utf8') as txt_file:
            i=0
            ligne=""
            Liste_ligne=[]
            while i<depart:
                ligne=txt_file.readline()
                i+=1
                if i==depart:
                    ligne=txt_file.readline()
            
            i=0
            A_trouver=False
            
            while i<35:
                
                if ligne.find("urgence")!=-1 and ligne.find("joignable")!=-1 and A_trouver==False:
                    ligne=txt_file.readline()
                    ligne=txt_file.readline()
                    ligne=txt_file.readline()
                    ligne=txt_file.readline()
                    Liste_ligne.append(ligne)
                    A_trouver=True
                elif A_trouver==True:
                    
                    if ligne.find("AUTRES")!=-1 and ligne.find("RENSEIGNEMENTS")!=-1:
                        nb_elem=0
                        for elem in Liste_ligne:
                            nb_elem+=1
                        if nb_elem==1:
                            return Liste_ligne[0]
                        else:
                            ligne=" ".join(Liste_ligne)
                            return ligne
                    
                    else:
                        Liste_ligne.append(ligne)
                ligne=txt_file.readline()
                i+=1
            
            return "Personne"
    except:
        print("ERREUR a la fonction qui renvoie les personne urg 2")
        return "ERREUR PERSONNE URG"
    
def Aller_personne_autorise2(txt_path,depart):
    try:

        with open(txt_path, 'r', encoding='utf8') as txt_file:
            i=0
            ligne=""
            Liste_ligne=[]
            while i<depart:
                ligne=txt_file.readline()
                i+=1
                if i==depart:
                    ligne=txt_file.readline()
            
            i=0
            A_trouver=False
            
            while i<55:
                
                if ligne.find("autorise")!=-1 and ligne.find("chercher")!=-1 and A_trouver==False:
                    

                    ligne=txt_file.readline()
                    ligne=txt_file.readline()
                    ligne=txt_file.readline()
                    ligne=txt_file.readline()
                    ligne=txt_file.readline()
                    Liste_ligne.append(ligne)
                    A_trouver=True
                elif A_trouver==True:
                    
                    if ligne.find("Parents")!=-1 and ligne.find("séparés")!=-1:
                        nb_elem=0
                        for elem in Liste_ligne:
                            nb_elem+=1
                        if nb_elem==1:
                            return Liste_ligne[0]
                        else:
                            ligne=" ".join(Liste_ligne)
                            return ligne
                    elif ligne.find("autorise")!=-1 and ligne.find("périscolaire")!=-1:
                        return "Personne"
                    else:
                        Liste_ligne.append(ligne)
                ligne=txt_file.readline()
                i+=1
            
            return "Personne"
    except:
        print("ERREUR a la fonction qui renvoie les personne supp 2")
        return "ERREUR PERSONNE SUPP"

def Aller_parents_separer(txt_path,depart):
    try:

        with open(txt_path, 'r', encoding='utf8') as txt_file:
            i=0
            ligne=""
            Liste_ligne=[]
            while i<depart:
                ligne=txt_file.readline()
                i+=1
                if i==depart:
                    ligne=txt_file.readline()
            
            i=0
            A_trouver=False
            
            while i<55:
                
                if ligne.find("Parents")!=-1 and ligne.find("séparés")!=-1 and A_trouver==False:
                    
                    ligne=txt_file.readline()
                    ligne=txt_file.readline()
                    
                    Liste_ligne.append(ligne)
                    A_trouver=True
                elif A_trouver==True:
                    
                    if ligne.find("autorise")!=-1 and ligne.find("périscolaire")!=-1:
                        nb_elem=0
                        for elem in Liste_ligne:
                            nb_elem+=1
                        if nb_elem==1:
                            return Liste_ligne[0]
                        else:
                            ligne=" ".join(Liste_ligne)
                            return ligne
                    else:
                        Liste_ligne.append(ligne)
                ligne=txt_file.readline()
                i+=1
            
            return "Personne"
    except:
        print("ERREUR a la fonction qui renvoie les parents séparer")
        return "ERREUR PARENTS SEPARER"

def Analyseur_txt(txt_path):

    with open(txt_path, 'r', encoding='utf8') as txt_file:
        
        fichier_entier=txt_file.readlines()
        n_lignes=len(fichier_entier)
        #print(n_lignes)
        txt_file.seek(0)
        i=0
        debut=0
        debut_urgence=0
        name_csv=txt_path.replace(".txt",".csv")
        name_classe=txt_path.replace(".txt","")
        name_classe=name_classe.replace("cache\\","")
        name=[]
        name.append(name_classe)
        
        with open(name_csv, 'w', newline='') as csvfile:
            writer=csv.writer(csvfile,delimiter=',')
            while i<n_lignes:
                Informations=[]
                ligne=txt_file.readline()
                #print(ligne)
                if Debut_de_fiche(ligne):
                    debut=i
                    i=i+1
                    #INFORMATIONS ENFANTS
                    ligne=Aller_nom_prenom_enfant(txt_path,debut)
                    Nom_e=Nom_enfant(ligne)
                    Prenom_e=Prenom_enfant(ligne)
                    ligne=Aller_repas(txt_path,debut)
                    Repas=Repas_enfant(str(ligne))
                    ligne=Aller_pai(txt_path,debut)
                    Pai=ligne

                    Informations.append(Nom_e)
                    Informations.append(Prenom_e)
                    Informations.append(Repas)
                    Informations.append(Pai)

                

                    #INFORMATIONS RESPONSABLE LEGAL 1
                    ligne=Aller_nom_responsable_legaux(txt_path,debut)
                    Nom_r1=Nom_responsable_legal1(str(ligne))
                    ligne=Aller_prenom_responsable_legaux(txt_path,debut)
                    Prenom_r1=Prenom_responsable_legal1(str(ligne))
                    ligne=Aller_tel_domicile(txt_path,debut)
                    Tel_domicile_r1=Tel_domicile_responsable_legal1(ligne)
                    ligne=Aller_tel_pro(txt_path,debut)
                    Tel_professionnel_r1=Tel_professionnel_responsable_legal1(ligne)
                    ligne=Aller_tel_por(txt_path,debut)
                    Tel_portable_r1=Tel_portable_responsable_legal1(ligne)
                    ligne=Aller_mail(txt_path,debut)
                    mail_r1=Mail_responsable_legal1(ligne)

                    Informations.append(Nom_r1)
                    Informations.append(Prenom_r1)
                    """
                    Informations.append(Tel_domicile_r1)
                    Informations.append(Tel_professionnel_r1)
                    Informations.append(Tel_portable_r1)
                    """
                    Informations.append(mail_r1)
                
                    #INFORMATIONS RESPONSABLE LEGAL 2
                    ligne=Aller_nom_responsable_legaux(txt_path,debut)

                    if Responsable_legal_2_exist(ligne)==True:
                        Nom_r2=Nom_responsable_legal2(ligne)
                        ligne=Aller_prenom_responsable_legaux(txt_path,debut)
                        Prenom_r2=Prenom_responsable_legal2(ligne)
                        ligne=Aller_tel_domicile(txt_path,debut)
                        Tel_domicile_r2=Numero_responsable_legal2(ligne)
                        ligne=Aller_tel_pro(txt_path,debut)
                        Tel_professionnel_r2=Numero_responsable_legal2(ligne)
                        ligne=Aller_tel_por(txt_path,debut)
                        Tel_portable_r2=Numero_responsable_legal2(ligne)
                        ligne=Aller_mail(txt_path,debut)
                        Mail_r2=Mail_responsable_legal2(ligne)
                    else:
                        Nom_r2="vide"
                        Prenom_r2="vide"
                        Tel_domicile_r2="vide"
                        Tel_professionnel_r2="vide"
                        Tel_portable_r2="vide"
                        Mail_r2="vide"

                    Informations.append(Nom_r2)
                    Informations.append(Prenom_r2)
                    """
                    Informations.append(Tel_domicile_r2)
                    Informations.append(Tel_professionnel_r2)
                    Informations.append(Tel_portable_r2)
                    """
                    Informations.append(Mail_r2)

                    """
                    debut_urgence=Aller_cas_urgence_I(txt_path,debut)
                    ligne=Aller_cas_urgence_S(txt_path,debut)

                    Liste_personne_urg=[]
                    if ligne.find("OUI")!=-1:
                    
                    INFORMATION PERSONNE A CONTACTER EN CAS URGENCE
                    
                        Liste_personne_urg=Personne_en_cas_urgence(txt_path,debut_urgence)
                    longueur_liste=0
                    for elem in Liste_personne_urg:
                        longueur_liste+=1
                    a=longueur_liste
                    if longueur_liste<5:
                        while a<5:
                            Liste_personne_urg.append("personne")
                            a+=1

                    Informations=Informations+Liste_personne_urg
                    """
                
                    """
                    debut_autre_personne=Aller_autres_personne_I(txt_path,debut)
                    ligne=Aller_autres_personne_S(txt_path,debut)

                    Liste_autre_personne=[]
                    if ligne.find("OUI")!=-1:
                        #INFORMATION SI AUTRES PERSONNE AUTORISEE
                    
                        Liste_autre_personne=Personne_autre(txt_path,debut_autre_personne)
                    longueur_liste=0
                    for elem in Liste_autre_personne:
                        longueur_liste+=1
                    a=longueur_liste
                    if longueur_liste<5:
                        while a<5:
                            Liste_autre_personne.append("personne")
                            a+=1

                    
                    Informations=Informations+Liste_autre_personne
                    """
                    
                    #AUTORISATIONS DE SORTIE ET ARRIVEES
                    debut_autorisation=Aller_autorisations_I(txt_path,debut)
                    ligne=Aller_autorisations_S(txt_path,debut)
                    Liste_autorisation=[]
                    Liste_autorisation=Autorisation(txt_path,debut_autorisation)
                    
                    #AUTORISATION PHOTO
                    Autorisation_photo=""
                    Autorisation_photo=Aller_autorisation_photo(txt_path,debut)
                    
                    Informations=Informations+Liste_autorisation
                    Informations.append(Autorisation_photo)
                    
                    #Rajout de la maladie et allergie
                    ligne=Aller_maladie(txt_path,debut)
                    Informations.append(ligne)

                    #Rajout Appareillage divers
                    ligne=Aller_lunette_appareillage(txt_path,debut)
                    Informations.append(ligne)
                    Tel=""
                    Liste_Tel=[Tel_domicile_r1,Tel_professionnel_r1,Tel_portable_r1,Tel_domicile_r2,Tel_professionnel_r2,Tel_portable_r2]
                    Tel=" ".join(Liste_Tel)
                    Informations.append(Tel)
                    Personne_urg=""
                    Personne_urg=Aller_personne_urg2(txt_path,debut)
                    Informations.append(Personne_urg)
                    Personne_supp=""
                    Personne_supp=Aller_personne_autorise2(txt_path,debut)
                    Informations.append(Personne_supp)
                    Parents_séparer=""
                    Parents_séparer=Aller_parents_separer(txt_path,debut)
                    Informations.append(Parents_séparer)
                    

                    
                    
                    
                
                    writer.writerow(Informations)
                    
                else:
                    i=i+1
            writer.writerow(name)
                    