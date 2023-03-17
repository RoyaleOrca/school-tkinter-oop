#gemacht mit Luka Jandric 
#Importiert die benoetigten Module
#customtkinter im Terminal installieren mit pip install cutomtkinter
import customtkinter as ctk
import pop_up

#Definiert die Klasse "MainSinnlos", welche von "ctk.CTk" erbt
#ctk.CTk Parent-Klasse
#MainSinnlos Child-Class
class MainSinnlos(ctk.CTk):

#Konstruktor-Methode ("_init_") mit dem Parameter "self" 
    def __init__(self, ) -> None:    
        #Rufe den Konstruktor der Superklasse ("ctk.CTk") auf
        super().__init__() 
        
        #Setzt den Fenstertitel auf "Sinnlos"
        self.title ("Sinnlos")

        #Erstellt einen Button mit dem Text "Hallo" und bindet ihn an die Methode "click_submit_button"
        self.b_pop_up = ctk.CTkButton(self, text = 'Hallo', command = self.click_submit_button)
        self.b_pop_up.pack()
        
        #Erstellt ein Textfeld 
        self.text_box = ctk.CTkTextbox(self, height=35,width=140)
        self.text_box.pack()
    
        #Erstellt ein Textfeld fuer den Benutzernamen und eins fuer das Passwort
        self.benutzer_name = ctk.CTkEntry(self)
        self.passwort = ctk.CTkEntry(self, show='*')
        #Erstellt einen Button zum Einloggen und bindet ihn an die Methode "einloggen_command"
        self.b_einloggen = ctk.CTkButton(self, text='Log in', command=self.einloggen_command) 
        
        #Fuegt die Widgets dem Fenster hinzu
        self.benutzer_name .pack(padx=10, pady=10)
        self.passwort.pack()
        self.b_einloggen.pack()
    #Methode zum Ueberpruefen des Benutzernamens und Passworts
    def einloggen_command (self):
        #Liest die eingegebenen Werte aus den Textfeldern aus
        benutzer_name= self.benutzer_name.get()
        passwort= self.passwort.get()
        #Ueberprueft, ob der Benutzername und das Passwort korrekt sind
        if benutzer_name == "Royale_Orca"and passwort == "Gandalf123":           # = variable werte gebne == schasut ob sie deng leichen wert haben 
            print("Hurra, es laeuft") 
            #Oeffnet ein Popup-Fenster mit der Meldung "Einloggen erfolgreich"
            pop_up.LogIn(self,"Einloggen erfolgreich")
            
        else:
            print("Falsche Eingabe!")
            #Oeffnet ein Popup-Fenster mit der Meldung "Einloggen fehlgeschlagen"
            pop_up.LogIn(self,"Einloggen fehlgeschlagen")       
    #Methode zum Einfuegen von Text in das Textfeld
    def click_submit_button(self):
        self.text_box.insert(ctk.END, "Meister")

        #Oeffnet ein Popup-Fenster
        pop_up.PopUp(self)
        
#Erstellet ein Objekt der Klasse "MainSinnlos"
fenster = MainSinnlos() 

#Starte die GUI-Schleife
fenster.mainloop()

    
