import tkinter as tk #1: για γραφικο περιβάλλον
from tkinter import messagebox #1: για εμφάνιση  μηνυμάτων στον χρήστη
import speech_recognition as sr #1: για αναγνώριση φωνής του χρήστη

recognizer = sr.Recognizer() #2:Ενεργοποήση αναγνώρισης φωνής

app = tk.Tk() #2:δημιουργία του βασικού παραθύρου 
app.title("Προσωπικός Ρομποτικός Βοηθός")#2:τίτλος παραθύρου
app.geometry("600x400")#2:διαστάσεις παραθύρου

def recognize_speech(): #3:συνάρτηση για αναγνώριση της φωνής του χρήστη
    with sr.Microphone() as source: #3: σύνδεση με το μικρόφωνο του υπολογιστή
        recognizer.adjust_for_ambient_noise(source) #3: αφαίρεση του θορύβου περιβάλλοντος
        print("Πείτε κάτι...")#3:εντολή για να μιλήσει ο χρήστης
        audio = recognizer.listen(source) #3:ακρόαση και καταγραφή ήχου
        
        try:
            #3:μετατροπή φωνητικών εντολών σε κείμενο&επιλογή γλώσσας
            user_input = recognizer.recognize_google(audio, language="el-GR")
            response = process_user_input(user_input)#3:επιστροφή απάντησης
            messagebox.showinfo("Απάντηση", response) #3: εμφάνιση μηνυμάτων σε γραφικό περιβάλλον
        except sr.UnknownValueError: #3:μηνύματα σφάλματος
            messagebox.showinfo("Σφάλμα!!", "Δεν αντιλαμβάνομαι τι λέτε.")
        except sr.RequestError as e:
            messagebox.showinfo("Σφάλμα!!", f"Σφάλμα κατά την αναγνώριση της φωνής: {e}")

#4:συνάρτηση για κείμενο που υπαγόρευσε ο χρήστης
def process_user_input(user_input): 

    return f"Είπατε: {user_input}"

#5:δημιουργία κουμπιού για την ενεργοποίηση της αναγνώρισης φωνής
speech_button = tk.Button(app, text="Αναγνώριση Φωνής", command=recognize_speech) 

speech_button.pack()#5:πρόσθεη μπουτόν στο γραφηκό παράθυρο

app.mainloop()#6:εκτέλεση μέχρι κλείσιμο γραφικού παραθύρου
