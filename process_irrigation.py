
"""

@author: Reda Zerrari
"""

def clean_data(data):
    """
    cette fonction prend en paramètre le dataframe, elle sert à nettoyer les données de notre dataframe, 
    elle parcourt la liste data des datasets 0, 1 et 2 et elle remplace les valeur erronées (égale à 200) par np.nan.
    
    """
    for i in range(3):
        for j in range(len(data['datasets'][i]['data'])):
            if data['datasets'][i]['data'][j] == 200 :
                data['datasets'][i]['data'][j] = np.nan

def sortdate():
    """
    cette fonction sert à nettoyer notre base de données des dates,
    premierement elle supprime la partie heure des dates, et puis elle supprime 
    les dates qui se répetent,
    elle retourne une liste contenant les dates de notre dataset sans l'heure et sans repetitions
    
    """
    
    nl=list()
    for i in range(len(data['labels'][0])):
        nl.append(data['labels'][0][i][0:10])

    l = list()
    for i in range(len(nl)):
        if nl[i] not in l :
            l.append(nl[i])
    return l 

def finddate(x):
    """
    cette fonction prend en paramètre une date et retourne son indice dans la list 
    des dates dans notre dataframe
    """
    j=0
    for i in range(len(data['labels'][0])):
        if x in data['labels'][0][i]:
            return j
            break
        if i == len(data['labels'][0]) - 1 and x not in data['labels'][0] :
            return None
        j=j+1       

def find_date_in_sorted_date(e,l):
    """
    cette fonction prend 2 paramètre:
    e : la date qu'on veut chercher.
    l : la list dans on veut chercher la date e.
    et retourne l'indice de la date e dans la list l

    """
    e=e[:10]
    j=0
    for i in range(len(l)):
        if l[i]==e:
            return j
        j=j+1

def getxticks_pos_label(s,e):
    """
    cette fonction prend en paramétre 2 dates :
    s : la date du debut
    e : date de la fin 
    et elle retourne 2 listes dont la premiere contient les dates entre s et e mais avec une marge de 4 jours 
    entre les dates  et la deuxieme contient les indices de ces dates dans la liste da dates netoyer qu'on creer 
    avec la fonction sortdate.
    """
    k = find_date_in_sorted_date(s,sortdate())+3
    m = find_date_in_sorted_date(e,sortdate())
    l = sortdate()
    ticklist=list()
    labellist=list()
    while k <= m :
        ticklist.append(k)
        labellist.append(l[k])
        k=k+4
    ticklist.append(m)
    labellist.append(l[m])
    if ticklist[0]>3:
        x=ticklist[0]
        for i in range(len(ticklist)):
            ticklist[i]=ticklist[i]-x +3
            
    return ticklist,labellist
    
def config_pos(l,x) :
    """
    cette fonction sert a transformer une liste d'indice en un intervales uniforme pour qu'on puisse l'utiliser 
    comme position pour les xticks.
    elle prend en parametres 
    l : la liste des indices
    x : la liste contenant tout les dates des données qu'on va ploter
    """
    d = len(x)/len(l)
    for i in range(1,len(l)+1):
        l[i-1]=l[i-1]+i*d
    return l           


def save_plot_to_file(dataframe, title, start_date, end_date, filename):
    """
    cette fonction prend 5 paramètre 
    dataframe : notre data
    title : le titre de notre graph
    start_date : la date du debut de notre étude
    end_date : la date de la fin 
    filename : le nom de la photo contenant le graphe qu'on souhaite enregistrer
    
    elle prend la dataframe et la decoupe (selon les paramètre start_date et end_date ) pour avoir l'intervalle
    de temps qu'on souhaite transformer en graphe. elle transforme la data en un graphe et l'enregistre su notre machine.
    
    """
    
    data = dataframe
    
    #recuperation des indices des dates à l'aide de la fonction finddate    
    s = finddate(start_date)
    e = finddate(end_date)
    
    #condition si l'intervalle de temps donné est invalide      
    if s == None or e == None or s >= e :
        return ("Date error")
 
    #creation de la figure et des subplots        
    fig , (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1,figsize=(10, 10), dpi=100, sharex=True)
    
    #slicing de la data selon l'intervalle donné    
    x1= data['labels'][0][s:e]
    y1= data['datasets'][0]['data'][s:e]

    x2= data['labels'][1][s:e]
    y2= data['datasets'][1]['data'][s:e]

    x3= data['labels'][2][s:e]
    y3= data['datasets'][2]['data'][s:e]
    
    #on plot ntre data 
    ax1.plot(x1,y1,color='blue')
    ax2.plot(x2,y2,color='blue')
    ax3.plot(x3,y3,color='blue')
    
    #coloriage des zones dans les 3 subplots
    ax1.fill_between(x=[x1[0],x1[-1]] ,y1=0, y2=15, color='red', alpha=0.2)
    ax1.fill_between(x=[x1[0],x1[-1]] ,y1=15, y2=30, color='orange', alpha=0.2)
    ax1.fill_between(x=[x1[0],x1[-1]] ,y1=30, y2=60, color='green', alpha=0.2)
    ax1.fill_between(x=[x1[0],x1[-1]] ,y1=60, y2=100, color='yellow', alpha=0.2)
    ax1.fill_between(x=[x1[0],x1[-1]] ,y1=100, y2=200, color='red', alpha=0.2)

    ax2.fill_between(x=[x1[0],x1[-1]] ,y1=0, y2=15, color='red', alpha=0.2)
    ax2.fill_between(x=[x1[0],x1[-1]] ,y1=15, y2=30, color='orange', alpha=0.2)
    ax2.fill_between(x=[x1[0],x1[-1]] ,y1=30, y2=60, color='green', alpha=0.2)
    ax2.fill_between(x=[x1[0],x1[-1]] ,y1=60, y2=100, color='yellow', alpha=0.2)
    ax2.fill_between(x=[x1[0],x1[-1]] ,y1=100, y2=200, color='red', alpha=0.2)

    ax3.fill_between(x=[x1[0],x1[-1]] ,y1=0, y2=15, color='red', alpha=0.2)
    ax3.fill_between(x=[x1[0],x1[-1]] ,y1=15, y2=30, color='orange', alpha=0.2)
    ax3.fill_between(x=[x1[0],x1[-1]] ,y1=30, y2=60, color='green', alpha=0.2)
    ax3.fill_between(x=[x1[0],x1[-1]] ,y1=60, y2=100, color='yellow', alpha=0.2)
    ax3.fill_between(x=[x1[0],x1[-1]] ,y1=100, y2=200, color='red', alpha=0.2)
    
    #mettre en place les position des xticks et yticks et leurs labels
    ax1.set_yticks([15/2, 45/2, 90/2, 160/2, 300/2])
    ax1.set_yticklabels(['saturated','too wet','perfect', 'plan to water','dry'])

    ax2.set_yticks([15/2, 45/2, 90/2, 160/2, 300/2])
    ax2.set_yticklabels(['saturated','too wet','perfect', 'plan to water','dry'])

    ax3.set_yticks([15/2, 45/2, 90/2, 160/2, 300/2])
    ax3.set_yticklabels(['saturated','too wet','perfect', 'plan to water','dry'])
    
    
    tick,label = getxticks_pos_label(start_date,end_date)
    
    tick = config_pos(tick,x1)

    ax3.set_xticks(tick)
    ax3.set_xticklabels(label)
    fig.autofmt_xdate(bottom=0.2, rotation=30, ha='right', which=None)
    
    #mettre en place la limites des axes X et Y         
    plt.xlim(0,len(x1))
    ax1.set_ylim(0,200)
    ax2.set_ylim(0,200)
    ax3.set_ylim(0,200)
    
    #mettre en place les legendes des 3 subplots
    ax1.legend ( ax1.plot(x1,y1), (data['datasets'][0]['label'],) , loc='upper left')
    ax2.legend ( ax2.plot(x2,y2), (data['datasets'][1]['label'],) , loc='upper left')
    ax3.legend ( ax3.plot(x3,y3), (data['datasets'][2]['label'],) , loc='upper left')
    
    #mettre en place le titre du graph
    ax1.set_title(title)
    
    #sauvgarder le graphe sur la machine
    plt.savefig(filename)
    
    plt.show()

    
if __name__ == '__main__':
    
    #importation des librairies
    import json
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    #transformer notre fichier json en une list contenant un dictionnaire qui contient notre data
    data = json.load(open("eco-sensors_irrigation_2020-06-01_2020-08-31.json"))
    #transformer notre list en une dataframe a l'aide de pandas
    data = pd.DataFrame(data)
    
    #appel de la fonction clean_data
    clean_data(data)
    
    #appel de la fonction save_plot_to_file
    save_plot_to_file(data, "Irrigation June 2020", "2020-06-02", "2020-06-30 23:", "irrigation_graph_2020-06")
    save_plot_to_file(data, "Irrigation July 2020", "2020-07-01", "2020-07-31 23:", "irrigation_graph_2020-07")
    save_plot_to_file(data, "Irrigation August 2020", "2020-08-02", "2020-08-29 17:", "irrigation_graph_2020-08")




