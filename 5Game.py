import tkinter as tk #1: επιλογή tkinter για γραφικό περιβάλλον
import random #1: επιλογή random για τυχαία επιλογή

def get_ai_choice(): #2: χρήση συνάρτησης για να λάβει 1 εκ των 3 επιλογών τυχαία η ΤΝ
    return random.randint(1, 3)

 #2: συνάρτηση για καθορισμό αποτελέσματος και εύρεσης νικητή
def determine_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "Ισοπαλία!"
    elif (user_choice == 1 and ai_choice == 2) or \
         (user_choice == 2 and ai_choice == 3) or \
         (user_choice == 3 and ai_choice == 1):
        return "Συγχαρητήρια! Κερδίσατε!"
    else:
        return "Η τεχνητή νοημοσύνη κέρδισε!"

def play_game(): #3: Συνάρτηση που καλείται μόλις πατήσει ο χρήστης το κουμπί "επιλογή"
    user_choice = int(choice_var.get())#3:μετατροπή επιλογής χρήστη σε ακέραιο
    ai_choice = get_ai_choice()#3:κάλεσμα συνάρτησης για λήψη επιλογής ΤΝ
    result = determine_winner(user_choice, ai_choice)#3:καθορίζει το αποτέλεσμα

    ai_window = tk.Toplevel(root)#3: δημιουργία παραθύρου για την επιλογή της TN
    ai_window.title("Επιλογή Τεχνητής Νοημοσύνης")#3:ονομασία παραθύρου
    ai_label = tk.Label(ai_window, text=f"Επιλογή τεχνητής νοημοσύνης: {ai_choice}")#3:κείμενο στο παράθυρο
    ai_label.pack()#3:ενσωμάτωση&εμφάνιση

    result_window = tk.Toplevel(root) #3: δημιουργία διαφορετικού παραθύρου για το αποτέλεσμα
    result_window.title(" Το αποτέλεσμα είναι: ")#3:τιτλος παραθύρου
    result_label = tk.Label(result_window, text=result)#3:εμφάνιση αποτέλεσματος
    result_label.pack()

root = tk.Tk()#4:δημιουργία του κύριου παραθύρου
root.title("Πέτρα, Ψαλίδι, Χαρτί")#4:ονομασία τίτλου 

label = tk.Label(root, text="Επιλέξτε: 1 - Πέτρα, 2 - Ψαλίδι, 3 - Χαρτί") #4:δημιουργία ετικέτας
label.pack()

choice_var = tk.StringVar() #4:δημιουργία μεταβλητής για την επιλογή του χρήστη

#4:δημιουργία κουμπιών επιλογής
rock_button = tk.Radiobutton(root, text="Πέτρα", variable=choice_var, value="1")
scissors_button = tk.Radiobutton(root, text="Ψαλίδι", variable=choice_var, value="2")
paper_button = tk.Radiobutton(root, text="Χαρτί", variable=choice_var, value="3")
#4:προστίθενται τα κουμπια στο παράθυρο για επιλογή απο τον χρήστη
rock_button.pack()
scissors_button.pack()
paper_button.pack()

#4:δημιουργία κουμπιού εκτέλεσης της επιλογής
choice_button = tk.Button(root, text="Επιλογή", command=play_game)
choice_button.pack()

root.mainloop() #5:εκκίνηση της εφαρμογής και εμφάνιση γραφικού περιβάλλοντος
