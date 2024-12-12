import random #line:1
import tkinter as tk #line:2
from tkinter import messagebox #line:3
departements_data ={"14":{"nom":"Calvados","villes":["Caen","Bayeux","Lisieux","Vire"]},"69":{"nom":"Rhône","villes":["Lyon","Villeurbanne","Vénissieux","Oullins"]},"75":{"nom":"Paris","villes":["Paris"]},"33":{"nom":"Gironde","villes":["Bordeaux","Arcachon","Mérignac","Pessac"]},"59":{"nom":"Nord","villes":["Lille","Roubaix","Tourcoing","Dunkerque"]},"81":{"nom":"Castre","villes":["Castre","mazamet ","fontalba "," Saint Pons "]},"13":{"nom":"Bouche du Rhone","villes":["aix en provence","Arles ","marseille ","célony"]},}#line:14
noms_rues =["rue de la Liberté","avenue des Champs","chemin des Fleurs","boulevard Saint-Michel","rue de la Gare","allée des Acacias","place Victor Hugo","rue des Écoles","rue Nationale"]#line:19
prenoms_jeunes =["Soan","Léna","Noé","Lina","Ethan","Anaïs","Lucas","Emma","julian"]#line:22
prenoms_adultes =["Jean","Marie","Paul","Lucie","Sophie","Pierre","Julie","Claire"]#line:23
prenoms_ages =["Jacques","Marguerite","Henri","Germaine","René","Suzanne","André","Yvonne"]#line:24
noms_famille =["Martin","Bernard","Dubois","Durand","Moreau","Simon","Laurent","Michel","Garcia","Thomas"]#line:28
def choisir_prenom (O000O000O000OOOO0 ):#line:31
    if O000O000O000OOOO0 <=20 :#line:32
        return random .choice (prenoms_jeunes )#line:33
    elif O000O000O000OOOO0 <=40 :#line:34
        return random .choice (prenoms_adultes )#line:35
    else :#line:36
        return random .choice (prenoms_ages )#line:37
def generer_adresse (O00OO0O0OOOO00000 ):#line:40
    if O00OO0O0OOOO00000 not in departements_data :#line:41
        return "Département invalide."#line:42
    O0OO0000000O00O0O =random .choice (departements_data [O00OO0O0OOOO00000 ]["villes"])#line:44
    O0O0O0O0O0O00O000 =f"{O00OO0O0OOOO00000}{random.randint(0, 99):02d}"#line:45
    OOOO0O0O0000OO00O =random .randint (1 ,200 )#line:46
    OO00O0O00O00O00OO =random .choice (noms_rues )#line:47
    return f"{OOOO0O0O0000OO00O} {OO00O0O00O00O00OO}, {O0O0O0O0O0O00O000} {O0OO0000000O00O0O}"#line:49
def generer_donnees ():#line:52
    O0OO0OOO0O0OO000O =entry_departement .get ().strip ()#line:53
    O00O000OOO0O000OO =entry_age .get ().strip ()#line:54
    if O0OO0OOO0O0OO000O not in departements_data :#line:56
        messagebox .showerror ("Erreur","Veuillez entrer un code de département valide (ex : 14).")#line:57
        return #line:58
    if not O00O000OOO0O000OO .isdigit ()or int (O00O000OOO0O000OO )<10 or int (O00O000OOO0O000OO )>60 :#line:60
        messagebox .showerror ("Erreur","Veuillez entrer un âge valide entre 10 et 60 ans.")#line:61
        return #line:62
    O0OOOO0OOO00O00O0 =int (O00O000OOO0O000OO )#line:64
    OOOO0000OOO0O0O00 =choisir_prenom (O0OOOO0OOO00O00O0 )#line:65
    O00O0O00OO0OOO000 =random .choice (noms_famille )#line:66
    O00OOOOOO000OOOOO =generer_adresse (O0OO0OOO0O0OO000O )#line:67
    label_nom .config (text =f"Nom : {OOOO0000OOO0O0O00} {O00O0O00OO0OOO000}")#line:70
    label_age .config (text =f"Âge : {O0OOOO0OOO00O00O0} ans")#line:71
    label_adresse .config (text =f"Adresse : {O00OOOOOO000OOOOO}")#line:72
def copier_donnees ():#line:75
    O000OOO0O0O0OO0O0 =f"{label_nom.cget('text')}\n{label_age.cget('text')}\n{label_adresse.cget('text')}"#line:76
    root .clipboard_clear ()#line:77
    root .clipboard_append (O000OOO0O0O0OO0O0 )#line:78
    messagebox .showinfo ("Copié","Les données ont été copiées dans le presse-papier.")#line:79
root =tk .Tk ()#line:82
root .title ("Générateur d'adresses aléatoires")#line:83
label_departement =tk .Label (root ,text ="Entrez le code du département (ex: 14 pour Calvados) :")#line:86
label_departement .pack (pady =5 )#line:87
entry_departement =tk .Entry (root )#line:88
entry_departement .pack (pady =5 )#line:89
label_age =tk .Label (root ,text ="Entrez l'âge (entre 10 et 60 ans) :")#line:92
label_age .pack (pady =5 )#line:93
entry_age =tk .Entry (root )#line:94
entry_age .pack (pady =5 )#line:95
btn_generer =tk .Button (root ,text ="Générer les données",command =generer_donnees )#line:98
btn_generer .pack (pady =10 )#line:99
label_nom =tk .Label (root ,text ="Nom :")#line:102
label_nom .pack (pady =5 )#line:103
label_age =tk .Label (root ,text ="Âge :")#line:105
label_age .pack (pady =5 )#line:106
label_adresse =tk .Label (root ,text ="Adresse :")#line:108
label_adresse .pack (pady =5 )#line:109
btn_copier =tk .Button (root ,text ="Copier les données",command =copier_donnees )#line:112
btn_copier .pack (pady =10 )#line:113
root .mainloop ()#line:116
