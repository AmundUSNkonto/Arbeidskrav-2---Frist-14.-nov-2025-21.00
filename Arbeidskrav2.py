# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 20:21:31 2025

@author: Amund 
"""


Koden er skrevet i Spyder og jeg bruker derfor #%% for å skille mellom oppgavene.


#Oppgave 1

alder = int(input("Hvilket år er du født?"))
                  
print("Du var", 2024-alder,"år gammel i 2024") #Oppgaveteksten spesifiserer 2024

#%% 
#Oppgave 2

import math #Importerer math for å kunne bruke en funksjon for å runde opp.

antall_elever = int(input("Skriv inn antall elever:")) #Variabel for input av antall elever

antall_pizza = antall_elever*(1/4) #Antallet pizzar man må kjøpe for antallet elever
Heltall_antall_pizzaer = math.ceil(antall_pizza) #Heltall antall pizzaer avrundet oppover

print("Du må kjøpe inn", Heltall_antall_pizzaer, "pizzaer")

#%%

#Oppgave 3

import numpy as np

v_grad = float(input("Skriv inn gradtallet:")) #Formel fra oppgavearket

v_rad = v_grad*np.pi/180 #Formel fra oppgavearket

print(f"Vinkelen i radianer (avrundet til 4 desimaler) blir, {v_rad:.4f}") #Bruker en formatted string for å kunne runde av

#%%

#Oppgave 4

#Oppgave 4a

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]   
        }

#Oppgave 4b

land =input("Skriv inn hvilken land du ønsker å vite mer om: ")

if land in data: #Denne virker bare dersom input fra land er med i datasettet
    Hovedstad, innbyggerantall = data[land] # Gir navn til dataen som tilhører "land"
    print(Hovedstad, "er hovedstadet i", land, "og det er", innbyggerantall, "milioner innbyggere i" , Hovedstad )
else: print( "Prøv igjen, husk å bruk stor bokstav i landet ditt!") # Påminnelse om at inputen må være nøyaktig lik enhetene i datasettet


#Oppgave 4c

nytt_land = input("Legg til nytt land: ") 
ny_hovedstad = input("Legg til ny hovedstad: ")
ny_inbyggertall = float(input("Legg til inbyggertall i antall milioner med 3 desimaler: "))

data[nytt_land] = [ny_hovedstad, ny_inbyggertall]

print("oppdatert liste vil nå være", data)


#%%

#Oppgave 5

import numpy as np
import math

a = float(input("Skriv inn lengden til a: "))
b = float(input("Skriv inn lengden til b: "))

areal_halvsirkel = ((np.pi*a**2)/2)
areal_trekant = (a*b/2)
total_arealet = areal_halvsirkel + areal_trekant

omkrets_halvsirkel = (2*np.pi*a)/2
omkrets_trekant = b + math.sqrt(a**2+b**2)
total_omkrets = omkrets_halvsirkel + omkrets_trekant

print("Det totale arealet av figren er", round(total_arealet,3)) #Bruker round for å runde av til 3 desimaler
print("Den totale omkretsen til figuren er", round(total_omkrets,3))


#%%

#Oppgave 6

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,200)

f = (-x**2) - 5

plt.plot(x, f)

plt.xlabel('x') # Legger til x-aksen 
plt.ylabel('f(x)') # Legger til y-aksen
plt.title('Plot av funksjonen f(x) i intervallet -10 til 10') #Legger til tittel

plt.axhline(0, color='black') #Legger til horisontal origolinje i svart
plt.axvline(0, color='black') #Legger til vertikal origolinje i svart


plt.grid() #Legger til rutenett
plt.show() #Viser plottet 










