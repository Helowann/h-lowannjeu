import random
import tkinter as tk
from tkinter import messagebox

def deviner_le_nombre():
    # Générer un nombre aléatoire entre 1 et 100
    nombre_secret = random.randint(1, 100)
    essais = 0

    # Fonction pour vérifier le nombre deviné
    def verifier():
        nonlocal essais
        try:
            essai = int(entry.get())
            essais += 1
            
            if essai < nombre_secret:
                message.config(text="Trop bas! Essaie encore.")
            elif essai > nombre_secret:
                message.config(text="Trop haut! Essaie encore.")
            else:
                messagebox.showinfo("Bravo!", f"Tu as deviné le nombre en {essais} essais.")
                # Réinitialiser le jeu
                button.config(state="disabled")
                entry.config(state="disabled")
                rejouer_button.config(state="normal")
        
        except ValueError:
            message.config(text="S'il vous plaît entrez un nombre valide.")
    
    # Fonction pour recommencer le jeu
    def recommencer():
        nonlocal nombre_secret, essais
        nombre_secret = random.randint(1, 100)
        essais = 0
        message.config(text="Devine le nombre entre 1 et 100.")
        entry.config(state="normal")
        button.config(state="normal")
        rejouer_button.config(state="disabled")
        entry.delete(0, tk.END)
    
    # Créer la fenêtre principale
    root = tk.Tk()
    root.title("Devine le Nombre")

    # Créer les éléments de l'interface
    label = tk.Label(root, text="Je pense à un nombre entre 1 et 100. À toi de le deviner!")
    label.pack(pady=10)
    
    entry = tk.Entry(root)
    entry.pack(pady=10)
    
    button = tk.Button(root, text="Valider", command=verifier)
    button.pack(pady=5)
    
    message = tk.Label(root, text="Devine le nombre entre 1 et 100.", font=("Arial", 12))
    message.pack(pady=10)
    
    rejouer_button = tk.Button(root, text="Rejouer", command=recommencer, state="disabled")
    rejouer_button.pack(pady=10)
    
    # Lancer la fenêtre principale
    root.mainloop()

# Lancer le jeu
deviner_le_nombre()