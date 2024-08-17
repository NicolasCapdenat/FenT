Ce fichier decrit ce que font les fonctions et ce qui est return dans chaque fontion

#DISCLAIMER Je ne suis pas programmeur donc certaines fonction sont redondantes et peuvent être amélioré (peut etre dans un futur proche)   #

**Debut_de_fichier(_chaine de caractère_)**
    Cette fonction compare _la chaine de caractère_ en argument avec "FICHE SANITAIRE ET DE LIAISON" qui symbolyse le début d'une fiche sanitaire.

    *Elle renvoie un booléen*

**Responsable_legal_2_exist(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ qui correspond à la ligne NOM des responsable légaux du fichier txt qui est analysé et verifie si il y a une chaine de caractère après le "NOM :" ce qui nous dit si il y a un second responsable légaux ou non.

    *Elle renvoie un booléen*

**Numéro_responsable_legal2(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ qu correspond à une ligne de numéro de telephone (domicie,professionnel ou portable)
    Elle regarde qu'elle est le numéro de téléphone du second responsable

    *Elle renvoie une chaine de caractère*

**Nom_enfant(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ ce qui correspond à la ligne Nom et prénom de l'enfant.
    Elle regarde qu'elle est le nom de l'enfant

    *Elle renvoie une chaine de caractère*

**Prenom_enfant(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ ce qui correspond à la ligne Nom et prénom de l'enfant.
    Elle regarde qu'elle est le prénom de l'enfant

    *Elle renvoie une chaine de caractère*

**Repas_enfant(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ ce qui correspond à la ligne repas
    Elle regarde si c'est Classique/Sans porc ou si ce n'est pas spécifié

    *Elle renvoie une chaine de caractère*

**Nom_repsonsable_legal1(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ ce qui correspond à la ligne des noms des responsables légaux
    Elle regarde qu'elle est le premier nom de la ligne

    *Elle renvoie une chaine de caractère*

**Nom_repsonsable_legal2(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ ce qui correspond à la ligne des noms des responsables légaux
    Elle regarde qu'elle est le second nom de la ligne

    *Elle renvoie une chaine de caractère*

**Prenom_repsonsable_legal(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ ce qui correspond à la ligne des prenoms des responsables légaux
    Elle regarde qu'elle est le premier prenom de la ligne

    *Elle renvoie une chaine de caractère*

**Prenom_repsonsable_legal2(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ ce qui correspond à la ligne des prenoms des responsables légaux
    Elle regarde qu'elle est le second prenom de la ligne

    *Elle renvoie une chaine de caractère*

**Tel_domicie_repsonsable_legal1(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ ce qui correspond à la ligne des numéros domiciles
    Elle regarde le premier numéro de la ligne(format 0625252525 ou 06 25 25 25 25)

    *Elle renvoie une chaine de caractère*

**Tel_professionnel_repsonsable_legal1(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ ce qui correspond à la ligne des numéros professionnels
    Elle regarde le premier numéro de la ligne(format 0625252525 ou 06 25 25 25 25)

    *Elle renvoie une chaine de caractère*

**Tel_portable_repsonsable_legal1(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ ce qui correspond à la ligne des numéros protables
    Elle regarde le premier numéro de la ligne(format 0625252525 ou 06 25 25 25 25)

    *Elle renvoie une chaine de caractère*

**Mail_responsable_legal1(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ ce qui correspond à la ligne des mails
    Elle regarde qu'elle est la première adresse mail

    *Elle renvoie une chaine de caractère*

**Mail_responsable_legal2(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ ce qui correspond à la ligne des mails
    Elle regarde qu'elle est la seconde adresse mail

    *Elle renvoie une chaine de caractère*

**Aller_nom_prenom_enfant(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et teste si la ligne est celle du nom et prénom

    *Elle renvoie une chaine de caractère*

**Aller_repas(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et teste si la ligne est celle du repas

    *Elle renvoie une chaine de caractère*

**Aller_nom_repsonsable_legaux(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et teste si la ligne est celle du nom des responsables légaux

    *Elle renvoie une chaine de caractère*

**Aller_prenom_repsonsable_legaux(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et teste si la ligne est celle du prenom des responsables légaux

    *Elle renvoie une chaine de caractère*

**Aller_tel_domicile(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et teste si la ligne est celle du tél domicile

    *Elle renvoie une chaine de caractère*

**Aller_tel_pro(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et teste si la ligne est celle du tél professionnel
    
    *Elle renvoie une chaine de caractère*

**Aller_tel_por(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et teste si la ligne est celle du tél portable
    
    *Elle renvoie une chaine de caractère*

**Aller_cas_urgence_I(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et test si la ligne est celle des peronnes à contacter en cas d'urgence et cherche à quelle numéro de ligne cela commence

    *Elle renvoie un entier*

**Aller_cas_urgence_S(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et test si la ligne est celle des peronnes à contacter en cas d'urgence 

    *Elle renvoie une chaine de caractère*

**Aller_autres_personne_I(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et test si la ligne est celle des peronnes supplémentaire et cherche à quelle numéro de ligne cela commence

    *Elle renvoie un entier*

**Aller_autres_personne_S(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et test si la ligne est celle des peronnes supplémentaire 

    *Elle renvoie une chaine de caractère*

**Aller_Autorisations_I(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et test si la ligne est celle des autorisations et cherche à quelle numéro de ligne cela commence

    *Elle renvoie un entier*

**Aller_Autorisation_S(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et test si la ligne est celle des autorisations

    *Elle renvoie une chaine de caractère*

**Aller_autorisation_photo(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et test si la ligne est celle de l'autorisation photo

    *Elle renvoie une chaine de caractère*

**Aller_mail(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et test si la ligne est celle des mails

    *Elle renvoie une chaine de caractère*

**Aller_pai(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et test si la ligne est celle des pai

    *Elle renvoie une chaine de caractère*

**Personne_en_cas_urgence(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et rentre dans une liste les personnes a contacter en cas d'urgence

    *Elle renvoie une liste de chaine de caractère*

**Personne_autre(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et rentre dans une liste les personnes supplémentaire autorisé

    *Elle renvoie une liste de chaine de caractère*

**Autorisation(_chaine de caractère_,_un entier_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et _un entier_ (qui correspond au départ de la fiche sanitaire en cour de traitement)
    Elle parcours le fichier txt et rentre dans une liste les autorisations péri et extra

    *Elle renvoie une liste de chaine de caractère*

**Analyseur_txt(_chaine de caractère_)**
    Cette fonction prend en argument: _une chaine de caractère_ (qui correspond à un chemin de fichier type "chemin"fichier.txt) et analyse ce fichier en rentrant tout dans un fichier csv

    *Elle ne renvoie rien*