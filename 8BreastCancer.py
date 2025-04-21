import matplotlib.pyplot as plt #1: βιβλιοθήκη για γράφημα οπτικοποίησης
from sklearn.datasets import load_breast_cancer #1:βιβλίοθηκη με ενσωματομένο το ενδιαφερόμενο dataset
from sklearn.model_selection import train_test_split#1:για διαχωρισμό σε εκπαίδευση-έλεγχο
from sklearn.tree import DecisionTreeClassifier#1: ταξινομητής decision tree
#1:ακρίβειας-πίνακας συγχυσης-αναφοράς ταξινόμησης 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = load_breast_cancer()#2: Φόρτωση του dataset
X = data.data #2:φόρτωση χαρακτηριστικών
y = data.target #2:κατηγοριών
#2:διαχωρισμός του dataset σε σύνολο εκπαίδευσης και σύνολο ελέγχου
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier()#3:δημιουργία του ταξινομητή Decision Tree
clf = clf.fit(X_train, y_train)#3:εκπαίδευση του ταξινομητή Decision Tree
y_pred = clf.predict(X_test)#3:πρόβλεψη των απαντήσεων για το σύνολο ελέγχου

#4: υπολογισμός&εκτύπωση ακρίβειας
accuracy = accuracy_score(y_test, y_pred)
print("Ακρίβεια:", accuracy)
#4: υπολογισμός&εκτύπωση πίνακα σύγχυσης
conf_matrix = confusion_matrix(y_test, y_pred)
print("Πίνακας Σύγχυσης:\n", conf_matrix)
#4:υπολογισμός&εκτύπωση αναφοράς ταξινόμησης
class_report = classification_report(y_test, y_pred)
print("Αναφορά Ταξινόμησης:\n", class_report)

plt.figure(figsize=(8, 7)) #5:επιλογή διαστάσεων πίνακα
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Pastel1)#5:συνάρτηση&χρώμα 
plt.title('Πίνακας Σύγχυσης')#5:ορισμός τίτλου
plt.colorbar()#5:αντιστοίχηση τιμών με χρώματα
tick_marks = range(len(data.target_names))#5:λίστα με ετικέτες
plt.xticks(tick_marks, data.target_names, rotation=45)#5:ορισμός ετικετών x-ονομασίες κατηγοριών-γωνία περιστροφής
plt.yticks(tick_marks, data.target_names)#5:ορισμός ετικετών y-ονομασία κατηγοριών
plt.ylabel('Πραγματική Κατηγορία')#5:ορισμός ετικέτας άξονα y
plt.xlabel('Προβλεπόμενη Κατηγορία')#5:ορισμός ετικέτας άξονα x
plt.show()#5:εμφάνιση γραφήματος 