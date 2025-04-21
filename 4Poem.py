import numpy as np#1:για δεδομένα αριθμητικής πολλαπλοτητας
import tensorflow as tf#1:ανοιχτού κώδικα εργασία μηχανικής-βαθιάς μάθησης
from tensorflow import keras#1:υπομοναδα TensorFlow για κατασκευή-εκπαίδευση μοντέλου ΜΜ
from tensorflow.keras.layers import Embedding, LSTM, Dense#1:επίπεδα νευρωνικού δικτύου
from tensorflow.keras.preprocessing.text import Tokenizer#1:για μετατροπή κειμένου σε ακολουθία ακεραίων
from tensorflow.keras.preprocessing.sequence import pad_sequences#1:για ευθυγράμμιση και συμπλήρωση ακολουθιών ακεραίων


#2:εισάγουμε τα δεδομένα εκπαίδευσης(κείμενα)
texts = ["Τα λουλούδια είναι όμορφα!",
         "Αισθάνομαι πολύ χαρούμενος με το φως του ήλιου.",
         "Μια επίσκεψη είναι παροδική.",
         "Οι αγκαλιές κάνουν τους ανθρώπους ευσυγκίνητους.",
         "Οι ανεμοστρόβιλοι είναι τρομακτικοί."]
#2:εισάγουμε τις ετικέτες που υποδηλώνουν το κάθε συναίσθημα
labels = [1, 1, 0, 2, 0]  # 1=Χαρά, 0=Αρνητικό, 2=Συγκίνηση
labels = np.array(labels)#2:μετατροπή κειμένου σε πίνακα NumPy για ορθή μορφή επεξεργασίας

#3:μετατροπή κειμένου σε ακολουθίες ακεραίων
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")#3:ορισμός, όριο στις λέξεις για μετατροπή, ειδικό τοκεν για ανιπαρκτή λέξη
tokenizer.fit_on_texts(texts)#3:εκπαίδευση tokenizer
sequences = tokenizer.texts_to_sequences(texts)#3:μετατροπη κειμένων σε ακεραιους
padded_texts = pad_sequences(sequences, maxlen=10, padding='post', truncating='post')#3:δημιουργία πίνακα εισόδου

#4:κατασκευή του μοντέλου
model = keras.Sequential()#4:δημιουργία κενού μοντέλου
model.add(Embedding(input_dim=1000, output_dim=16, input_length=10))#4:πρόσθεση επιπέδου Embedding
model.add(LSTM(64)) #4:πρόσθεση επιπέδου LSTM
model.add(Dense(3, activation='softmax')) #4:πρόσθεση επιπέδου Dense με 3 εξόδους

#5:μοντέλο έτοιμο για εκπαίδευση 
model.compile(optimizer='adam',#5:προσθήκη βελτιστοποιητή
              loss='sparse_categorical_crossentropy',#5:προσθήκη συνάρτησης απώλειας
              metrics=['accuracy'])#5:επιλογή μετρικής=ακρίβεια

#5: εκπαίδευση του μοντέλου
model.fit(padded_texts, labels, epochs=20, batch_size=1)

#6:αξιολόγηση συναισθημάτων, προσθήκη ποιήματος
new_texts = ["Να κλαίγεσαι που δεν έχεις πολλά. Που κι αν τα είχες, θα ήθελες περισσότερα. Να πιστεύεις ότι τα ξέρεις όλα και να μην ακούς. Να μαζεύεις λύπες και απελπισίες, να ξυπνάς κάθε μέρα ακόμη πιο βαρύς. Λες και ο χρόνος σου είναι απεριόριστος.."]
encoded_texts = tokenizer.texts_to_sequences(new_texts)#6:μετατροπή σε ακέραιο
#6:επεξεργασία και προσαρμογή σε μήκος 10 όπως και πάνω 
padded_new_texts = pad_sequences(encoded_texts, maxlen=10, padding='post', truncating='post')
#7:εκχώρηση στην μεταβλητή το αποτέλεσμα της πρόβλεψης νέου κειμένου
predictions = model.predict(padded_new_texts)
for i, prediction in enumerate(predictions):#7:πρόσβαση σε κάθε πρόβλεψη του κειμένου
    predicted_label = np.argmax(prediction)#7:δείκτης μεμεγαλύτερη πιθανότητα πρόβλεψης
    if predicted_label == 0:#7:ανάλογα με την τιμή εμφανίζεται και το συναίσθημα
        print(f"Κείμενο {i + 1}: Αρνητικό Συναίσθημα")
    elif predicted_label == 1:
        print(f"Κείμενο {i + 1}: Συναίσθημα Χαράς")
    elif predicted_label == 2:
        print(f"Κείμενο {i + 1}: Συγκινητικό Συναίσθημα")
