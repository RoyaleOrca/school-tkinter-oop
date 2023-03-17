import customtkinter as ctk
import counter 

#Parent-Klasse
class PopUp:
    #Konstruktor, der den Top-Level-Container des Pop-Ups erstellt
    def __init__(self, parent) -> None:
        self.top = ctk.CTkToplevel(parent)
        #Erstellen und Hinzufuegen eines Labels zum Pop-Up-Fenster
        self.label = ctk.CTkLabel(self.top, text="hi")
        self.label.pack(pady=20)

        #Erstellen und Hinzufuegen eines Buttons zum Pop-Up-Fenster
        self.button = ctk.CTkButton(self.top, text="OK", command=self.close)
        self.button.pack(pady=10)

    #Methode, die das Pop-Up-Fenster schliesst  
    def close(self):
        self.top.destroy()
        

#child-Klasse von Popup 
class LogIn(PopUp):
    #Konstruktor, der den Text und den Parent des Log-In-Pop-Ups erhaelt und die Parent-Klasse initialisiert
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        #"text" wird global in der Klasse gespeichert
        self.text=text
        self.parent=parent
         #Das Label des Pop-Ups wird auf den uebergebenen Text aktualisiert
        self.label.configure(text=text)

     #Ueberschreibung der "close"-Methode aus der Parent-Klasse
    def close(self):
        #Wenn der Text des Pop-Ups "Einloggen erfolgreich" ist, wird eine neue CounterApp erstellt
        if self.text =="Einloggen erfolgreich":
            counter.CounterApp(self.parent)
        #Ansonsten wird das Pop-Up-Fenster geschlossen
        else:
            super().close()
