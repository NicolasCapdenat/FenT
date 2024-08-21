import os
import shutil

def Observe_pdf():
    Liste_fichiers=[]
    directory = 'Fiches_sanitaire'
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f) and filename.endswith('.pdf'):
            
            Liste_fichiers.append(f)
    
    return Liste_fichiers

def Nettoie_cache():
    
    directory = 'cache'
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f) and filename.endswith('.md')==False:
            os.remove(f)

def Nettoie_bak():
    directory = 'Reception'
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f) and filename.endswith('.bak'):
            os.remove(f)

def Nettoie_tmp():
    directory = 'Reception'
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f) and filename.endswith('.tmp'):
            os.remove(f)

def Nettoie_ods():
    directory = 'Reception'
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f) and filename.endswith('.ods'):
            os.remove(f)
 

def Observe_txt():
    Liste_fichiers=[]
    directory = 'cache'
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f) and filename.endswith('.txt'):
            
            Liste_fichiers.append(f)
            f=f.replace("cache\\","")
            f=f.replace(".txt","")
            f=f+".ods"
            
            shutil.copy('Liste_referente.ods','Reception/'+f)
    
    shutil.copy('Autorisation_photo_reference.ods','Reception/Autorisation_photo.ods')
    shutil.copy('Pai_reference.ods','Reception/_PAI_.ods')
    
    #print(Liste_fichiers)
    return Liste_fichiers

def Observe_csv():
    Liste_fichiers=[]
    directory = 'cache'
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f) and filename.endswith('.csv'):
            
            Liste_fichiers.append(f)
            
    
    #print(Liste_fichiers)
    return Liste_fichiers

def Observe_ods():
    Liste_fichiers=[]
    directory = 'Reception'
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f) and filename.endswith('.ods'):
            
            Liste_fichiers.append(f)
            
    
    #print(Liste_fichiers)
    return Liste_fichiers




