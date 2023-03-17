import customtkinter as ctk
#Master = übergabe Parameter
class CounterApp:
    def __init__(self, master):
        # Initialisierung einer Instanzvariable fuer den Zaehler
        self.count = 0

        # Erstellen eines Toplevel-Fensters als uebergeordnetes Fenster
        self.top = ctk.CTkToplevel(master)
        # Erstellen eines Labels, das den aktuellen Zaehlerstand anzeigt 
        self.label = ctk.CTkLabel(self.top, text=str(self.count))
        self.label.pack()

        # Erstellen von Buttons fuer das Erhoehen, Verringern und das Zuruecksetzen des Zaehlers
        self.button_increment = ctk.CTkButton(self.top, text="Erhoehen", command=self.increment)
        self.button_increment.pack()

        self.button_decrement = ctk.CTkButton(self.top, text="Verringern", command=self.decrement)
        self.button_decrement.pack()

        self.button_reset = ctk.CTkButton(self.top, text="Reset", command=self.reset)
        self.button_reset.pack()

        
    # Methode zum Inkrementieren des Zaehlers und Aktualisieren des Labels
    def increment(self):
        self.count += 1
        self.label.configure(text=str(self.count))

    # Methode zum Dekrementieren des Zaehlers und Aktualisieren des Labels
    def decrement(self):
        self.count -= 1
        self.label.configure(text=str(self.count))

 # Methode zum Zuruecksetzen des Zaehlers und Aktualisieren des Labels
    def reset(self):
        self.count = 0
        self.label.configure(text=str(self.count))
