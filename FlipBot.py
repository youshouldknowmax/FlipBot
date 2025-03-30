import tkinter as tk
import random

def jouer():
    result = random.choice(['Pile', 'Face'])
    label_resultat.config(text=f"Résultat : {result}")

root = tk.Tk()
root.title("FlipBot")

label_resultat = tk.Label(root, text="Résultat : ", font=("Arial", 16))
label_resultat.pack(pady=20)

button_jouer = tk.Button(root, text="Lancer la pièce", command=jouer, font=("Arial", 14))
button_jouer.pack(pady=20)

root.mainloop()
