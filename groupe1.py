import tkinter as tk
from tkinter import messagebox

# Variables globales d'affichage
fenetre = None
boutons_grille = []
label_message = None

def initialiser_affichage():
    """Initialise l'interface graphique"""
    global fenetre, boutons_grille, label_message
   
    fenetre = tk.Tk()
    fenetre.title("Morpion - Équipe 1")
    fenetre.resizable(False, False)
   
    # Création de la grille visuelle
    frame_grille = tk.Frame(fenetre)
    boutons_grille = []
   
    # Création des 9 boutons (désactivés par défaut)
    for i in range(3):
        ligne = []
        for j in range(3):
            btn = tk.Button(frame_grille,
                          text=' ',
                          font=('Arial', 30),
                          width=4,
                          height=2,
                          state='disabled')
            btn.grid(row=i, column=j, padx=2, pady=2)
            ligne.append(btn)
        boutons_grille.append(ligne)
   
    frame_grille.pack(pady=15)
   
    # Zone des messages
    label_message = tk.Label(fenetre,
                           font=("Arial", 14, "bold"),
                           fg="#333333")
    label_message.pack(pady=10)
   
    fenetre.mainloop()

def maj_grille(ligne, colonne, symbole):
    """Met à jour l'affichage d'une case"""
    boutons_grille[ligne][colonne].config(
        text=symbole,
        disabledforeground='red' if symbole == 'X' else 'blue'
    )

def afficher_message(texte, est_fin=False):
    """Affiche les messages de statut"""
    label_message.config(text=texte)
    if est_fin:
        label_message.config(fg="green" if "gagné" in texte else "orange")

def changer_etat_grille(actif):
    """Active/désactive l'affichage des cases"""
    etat = 'normal' if actif else 'disabled'
    for ligne in boutons_grille:
        for btn in ligne:
            btn.config(state=etat)

# Test minimal de l'affichage
if __name__ == "__main__":
    initialiser_affichage()
