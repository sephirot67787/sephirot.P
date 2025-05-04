import tkinter as tk
import random
import winsound
from PIL import Image, ImageTk
import os

# Definizioni di colori, frequenze e immagini
colori = ["#32CD32", "#FF6347", "#1E90FF", "#FFD700", "#FF69B4", "#8A2BE2", "#00CED1", "#FF4500"]  # Colori per i tasti
frequenze = [400, 500, 600, 700, 800, 900, 1000, 1100]  # Frequenze per ciascun colore
immagini_bottoni = ["gaynnaro.png", "gaynnaro2.jpg", "gaynnaro3.jpg", "gaynnaro4.jpg", "gaynnaro5.jpg", "gaynnaro6.jpg", "gaynnaro7.jpg", "gaynnaro8.jpg"]  # Immagini per i bottoni
immagini_logo = ["gaynnaro.png", "gaynnaro2.jpg", "gaynnaro3.jpg", "gaynnaro4.jpg", "gaynnaro5.jpg", "gaynnaro6.jpg", "gaynnaro7.jpg", "gaynnaro8.jpg"]  # Immagini per il logo
colore_frequenza = dict(zip(colori, frequenze))

# Percorso delle immagini
current_dir = os.path.dirname(os.path.abspath(__file__))

# Verifica che tutte le immagini siano disponibili
def verifica_immagini(lista_immagini):
    for immagine in lista_immagini:
        if not os.path.exists(os.path.join(current_dir, immagine)):
            print(f"Errore: Immagine '{immagine}' non trovata.")
            exit(1)

verifica_immagini(immagini_bottoni)
verifica_immagini(immagini_logo)

# Variabili globali
sequenza = []
colori_selezionati = []
punteggio = 0

# Dimensioni predefinite per bottoni e logo
button_size = 200  # Bottone con una dimensione fissa
logo_size = 350  # Logo più grande

# Funzione che genera o estende la sequenza di colori
def genera_sequenza():
    global sequenza
    if punteggio == 0:  # Iniziamo con 3 colori
        sequenza = [random.choice(colori) for _ in range(3)]
    else:  # Ogni punto incrementa la lunghezza della sequenza
        sequenza.append(random.choice(colori))

# Funzione che mostra la sequenza di colori all'utente
def mostra_sequenza():
    tempo_illuminazione = 300  # Ridotto il tempo per rendere la sequenza più veloce

    def illumina(index):
        if index < len(sequenza):
            bottone = bottoni[colori.index(sequenza[index])]
            bottone.config(bg="white")
            winsound.Beep(colore_frequenza[sequenza[index]], 500)
            finestra.after(tempo_illuminazione, lambda: spegni(index))

    def spegni(index):
        if index < len(sequenza):
            bottone = bottoni[colori.index(sequenza[index])]
            bottone.config(bg=sequenza[index])
            finestra.after(tempo_illuminazione, lambda: illumina(index + 1))

    illumina(0)

# Verifica la sequenza selezionata dall'utente
def verifica_sequenza():
    global punteggio
    if colori_selezionati == sequenza:
        punteggio += 1
        cambia_immagini_bottoni()
        cambia_logo()
        reset_gioco()  # Reset della sequenza per continuare il gioco
    else:
        punteggio -= 1
        if punteggio < 0:
            etichetta.config(text="Hai perso definitivamente!")
            finestra.after(2000, finestra.destroy)
        else:
            etichetta.config(text=f"Hai sbagliato! Punteggio: {punteggio}")
            reset_gioco()

# Funzione che viene chiamata quando un tasto viene premuto
def al_click_colore(index):
    colore = bottoni[index].cget("bg")
    colori_selezionati.append(colore)
    frequenza_random = random.choice(frequenze)
    winsound.Beep(frequenza_random, 200)
    if len(colori_selezionati) == len(sequenza):
        verifica_sequenza()

# Cambia l'immagine del logo in modo casuale
def cambia_logo():
    img_path = os.path.join(current_dir, random.choice(immagini_logo))
    img = Image.open(img_path).resize((logo_size, logo_size), Image.Resampling.LANCZOS)  # Logo più grande
    img_tk = ImageTk.PhotoImage(img)
    label_logo.config(image=img_tk)
    label_logo.image = img_tk

# Cambia le immagini dei bottoni, ogni bottone avrà un'immagine unica
def cambia_immagini_bottoni():
    # Creiamo una lista di immagini random senza ripetizioni
    immagini_disp = immagini_bottoni.copy()
    random.shuffle(immagini_disp)  # Mescoliamo le immagini
    for i, bottone in enumerate(bottoni):
        img_path = os.path.join(current_dir, immagini_disp[i])  # Assegniamo una diversa immagine per ogni bottone
        img = Image.open(img_path).resize((button_size, button_size), Image.Resampling.LANCZOS)  # Immagini più grandi
        img_tk = ImageTk.PhotoImage(img)
        bottone.config(image=img_tk)
        bottone.image = img_tk

# Reset del gioco, genera una nuova sequenza
def reset_gioco():
    global colori_selezionati
    colori_selezionati = []
    genera_sequenza()  # Genera una nuova sequenza che aumenta ad ogni punto
    etichetta.config(text=f"Punteggio: {punteggio}")
    finestra.after(1000, mostra_sequenza)

# Inizializzazione finestra di gioco
finestra = tk.Tk()
finestra.title("SIMON DUCE")
finestra.config(bg="black")

# Impostiamo la finestra a schermo intero
finestra.attributes('-fullscreen', True)
finestra.bind("<Escape>", lambda e: finestra.attributes('-fullscreen', False))  # Escape per uscire dal full screen

etichetta = tk.Label(finestra, text="Clicca per iniziare", font=("Arial", 20), fg="white", bg="black")
etichetta.pack(pady=10)

# Layout griglia principale
frame_principale = tk.Frame(finestra, bg="black")
frame_principale.pack(expand=True, fill="both")

for r in range(3):
    frame_principale.grid_rowconfigure(r, weight=1)
for c in range(3):
    frame_principale.grid_columnconfigure(c, weight=1)

# Bottoni principali (8 tasti con logo al centro)
bottoni = []
posti_bottoni = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
for i, (r, c) in enumerate(posti_bottoni):
    bottone = tk.Button(frame_principale, bg=colori[i], width=10, height=5, command=lambda i=i: al_click_colore(i))
    bottone.grid(row=r, column=c, padx=0, pady=0, sticky="nsew")  # Ridotto il padding tra i bottoni
    bottoni.append(bottone)

# Logo centrale incastrato tra i bottoni
label_logo = tk.Label(frame_principale, bg="black")
label_logo.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")  # Logo più vicino ai bottoni
cambia_logo()

# Avvio del gioco
sequenza = []
genera_sequenza()
reset_gioco()

finestra.mainloop()
