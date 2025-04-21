import tensorflow as tf#1:εισαγωγή βιβλιοθήκης TensorFlow 
from tensorflow import keras#1:εισαγωγή βιβλιοθήκης Keras από TensorFlow 
from tensorflow.keras import layers#1:εγκαθιστούμε το layers, υποπακέτο του Keras
from tensorflow.keras.datasets import fashion_mnist#1:εισαγωγή των δεδομένων ρούχων
import numpy as np#1:εισαγωγή για αριθμητικούς υπολογισμούς
import matplotlib.pyplot as plt#1:εισαγωγή για εμφανιση γραφικών

#2:φορτώνουμε τα δεδομένα Fashion MNIST
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
#3:κανονικοποίηση των εικόνων 
train_images, test_images = train_images / 255.0, test_images / 255.0
#4:ορίζουμε κατηγορίες
class_names = ['Μπλούζα', 'Παντελόνι', 'Πουκάμισο', 'Φόρεμα', 'Παλτό', 'Σανδάλι', 'Πουλόβερ', 'Παπούτσια', 'Τσάντα', 'Μπότες']
#5:δημιουργία μοντέλου νευρωνικού δικτύου
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),#5:μετατροπή διαστάσεων εικόνων 28x28
    layers.Dense(128, activation='relu'),#5:επίπεδο 128 νευρώνων με συνάρτηση ενεργοποίησης
    layers.Dense(10)#5:τελευταίο επίπεδο με 10 νευρώνες αντιστοιχισμένοι στις κατηγορίες
])
#6: ρυθμίσειςγια την εκπαίδευση του μοντέλου
model.compile(optimizer='adam',#6:εισαγωγή βελτιστοποιητή 
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),#6:ορισμός συνάρτησης κόστους
              metrics=['accuracy'])#6:εισαγωγή μετρικής
#7:εκπαίδευση του μοντέλου
model.fit(train_images, train_labels, epochs=50)
#8:επιλογή τυχαίας εικόνας και πρόβλεψη 
random_idx = np.random.randint(0, len(test_images))#8:επιλογή τυχαίου δείκτηεικόνας απο test_images
new_image = test_images[random_idx]#8:εκχώρηση τυχαίας εικόνας σε μεταβλητή
predictions = model.predict(np.expand_dims(new_image, axis=0))#8:πρόβλεψη της εικόνας
predicted_class = np.argmax(predictions)#8:αντιστοίχηση κατηγορίας στην τυχαία εικόνα 
#9:εμφανίση εικόνας και προβλεπόμενης κατηγορίας
plt.figure()
plt.imshow(new_image, cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.title('Η Προβλεπόμενη κατηγορία είναι: ' + class_names[predicted_class])
plt.show()
