import tkinter as Grafica
from tkinter import messagebox
import random

class RadiantCowSteakHouse:
    def __init__(self, root):
        self.root = root
        self.root.title("Radiant Cow Steak House")
        self.conto = 0
        self.order_items = []
        self.active_shifts = []

        self.main_menu()

    def main_menu(self):
        self.clear_window()

        title = Grafica.Label(self.root, text="Radiant Cow Steak House", font=("Helvetica", 18, "bold"))
        title.pack(pady=10)

        mode_label = Grafica.Label(self.root, text="Seleziona Modalità:", font=("Helvetica", 14))
        mode_label.pack(pady=5)

        client_button = Grafica.Button(self.root, text="Cliente", font=("Helvetica", 12), command=self.client_menu)
        client_button.pack(pady=5)

        employee_button = Grafica.Button(self.root, text="Dipendente", font=("Helvetica", 12), command=self.employee_menu)
        employee_button.pack(pady=5)

    def client_menu(self):
        self.clear_window()

        title = Grafica.Label(self.root, text="Menu Clienti", font=("Helvetica", 16, "bold"))
        title.pack(pady=10)





        menu_items = [
            ("Carpaccio di manzo", 15.00),
            ("Tartare di manzo", 16.00),
            ("Bruschette miste", 8.00),
            ("Tagliatelle al ragù", 14.00),
            ("Risotto ai funghi", 13.00),
            ("Gnocchi al gorgonzola", 12.00),
            ("Ribeye Steak (300g)", 28.00),
            ("Filetto (250g)", 32.00),
            ("T-Bone (500g)", 35.00),
            ("Tomahawk (800g)", 45.00),
            ("Patate arrosto", 5.00),
            ("Verdure grigliate", 6.00),
            ("Insalata mista", 4.00),
            ("Vino della casa", 18.00),
            ("Birra artigianale", 6.00),
            ("Acqua minerale", 2.50),
            ("Tiramisù", 6.00),
            ("Panna cotta", 5.00),
            ("Cheesecake", 6.00),

        ]

        for i, (item, price) in enumerate(menu_items, start=1):
            btn = Grafica.Button(self.root, text=f"{i}. {item} - €{price:.2f}", font=("Helvetica", 10), command=lambda item=item, price=price: self.add_to_bill(item, price))
            btn.pack(anchor="w", padx=20, pady=2)

        finish_button = Grafica.Button(self.root, text="Completa Ordine", font=("Helvetica", 12), command=self.complete_order)
        finish_button.pack(pady=10)

    def add_to_bill(self, item, price):
        self.conto += price
        self.order_items.append((item, price))
        messagebox.showinfo("Ordine", f"{item} aggiunto al conto! Totale attuale: €{self.conto:.2f}")

    def complete_order(self):
        luck = random.randint(0, 1)
        message = f"Grazie per aver ordinato! Il conto è di €{self.conto:.2f}."

        if messagebox.askyesno("Extra", "Vuoi aggiungere un caffè (€1.00) o un digestivo (€4.00)?"):
            if luck == 0:
                drink = random.choice(["caffè", "digestivo"])
                price = 1 if drink == "caffè" else 4
                self.conto += price
                message += f"\nHai scelto un {drink} al prezzo di €{price:.2f}."
            else:
                message += "\nIl caffè o il digestivo lo offre la casa!"

        messagebox.showinfo("Grazie", message)

        # Reset order
        self.conto = 0
        self.order_items = []
        self.main_menu()

    def employee_menu(self):
        self.clear_window()

        title = Grafica.Label(self.root, text="Menu Dipendenti", font=("Helvetica", 16, "bold"))
        title.pack(pady=10)

        name_label = Grafica.Label(self.root, text="Inserisci il tuo nome:", font=("Helvetica", 12))
        name_label.pack(pady=5)
        name_entry = Grafica.Entry(self.root, font=("Helvetica", 12))
        name_entry.pack(pady=5)

        age_label = Grafica.Label(self.root, text="Inserisci la tua età:", font=("Helvetica", 12))
        age_label.pack(pady=5)
        age_entry = Grafica.Entry(self.root, font=("Helvetica", 12))
        age_entry.pack(pady=5)

        submit_button = Grafica.Button(self.root, text="Conferma", font=("Helvetica", 12), command=lambda: self.employee_shift(name_entry.get(), age_entry.get()))
        submit_button.pack(pady=10)

        # Show current active shifts
        if self.active_shifts:
            shifts_label = Grafica.Label(self.root, text="Turni attivi:", font=("Helvetica", 12))
            shifts_label.pack(pady=5)

            for shift in self.active_shifts:
                shift_label = Grafica.Label(self.root, text=shift, font=("Helvetica", 10))
                shift_label.pack(pady=2)

    def employee_shift(self, name, age):
        if not name or not age.isdigit() or not (18 <= int(age) <= 70):
            messagebox.showerror("Errore", "Per favore inserisci un nome valido e un'età numerica tra 18 e 70.")
            return

        code = random.randint(1000000, 9999999)
        shift_hours = random.randint(1, 9)
        start_hour = random.randint(0, 23)
        end_hour = (start_hour + shift_hours) % 24

        shift_message = (
            f"Benvenuto, {name}! Hai {age} anni.\n"
            f"Il tuo codice dipendente è: {code}.\n"
            f"Il tuo turno è dalle {start_hour:02d}:00 alle {end_hour:02d}:00."
        )

        # Add to active shifts
        self.active_shifts.append(shift_message)

        messagebox.showinfo("Turno", shift_message)
        self.main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Grafica.Tk()
    app = RadiantCowSteakHouse(root)
    root.mainloop()
