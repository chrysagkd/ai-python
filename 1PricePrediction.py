import pandas as pd#1:εισαγωγή pandas για φόρτωση-επεξεργασία-προετοιμασία
from sklearn.model_selection import train_test_split#1:εισαγωγή για διαχωρισμό υποσύνολων εκπαίδευσης και ελέγχου
from sklearn.neighbors import KNeighborsRegressor#1:εισαγωγή αλγορίθμου K-Nearest Neighbors (KNN)
from sklearn.metrics import mean_squared_error#1:εισαγωγή μετρικής ΜΤΣ
from sklearn.preprocessing import StandardScaler, OneHotEncoder#1:εισαγωγή 2 μετασχηματιστών
from sklearn.compose import ColumnTransformer#1:εισαγωγη μετασχηματισμου για επεξεργασία τμημάτων των άνω 
from sklearn.pipeline import Pipeline#1:εισαγωγή pipelone

#2:διαβάζουμε τα δεδομένα από το αρχείο CSV
data = pd.read_csv("C:\\Users\\chrysagkd\\Downloads\\HOUSE_PRICES_25102023130159717.csv")
#2:επιλογή των στηλών που θα χρησιμοποιησουμε ως χαρακτηριστικά
features = data[['Country', 'Value']]#2:στήλη χώρας και αξίας
features = features.dropna(subset=['Value'])#2:διαγραφή γραμμών που περιέχουν NaN τιμές στη στήλη 'Value'
features['Value'] = features['Value'].astype(float)#2:μετατροπή των τιμών της στήλης Value σε float

categorical_columns = ['Country']#3:ορίζουμε τις στήλες που χρειάζονται κωδικοποίηση
categorical_transformer = Pipeline(steps=[#3:ορίζουμε τον μετασχηματιστή για One-Hot Encoding
    ('onehot', OneHotEncoder(sparse=False, drop='first'))
])
numeric_transformer = Pipeline(steps=[#3:ορίζουμε τον μετασχηματιστή για τυποποίηση
    ('scaler', StandardScaler())
])

preprocessor = ColumnTransformer(#4:ορίζουμε τον μετασχηματιστή για τις διάφορες στήλες
    transformers=[
        ('num', numeric_transformer, ['Value']),
        ('cat', categorical_transformer, categorical_columns)
    ])

#5:ορίζουμε το πλήρες pipeline με τον KNeighborsRegressor
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('regressor', KNeighborsRegressor(n_neighbors=3))])
#5:διαχωρισμός των δεδομένων σε σύνολα εκπαίδευσης και ελέγχου
features_train, features_test, target_train, target_test = train_test_split(features, features['Value'], test_size=0.5, random_state=42)
pipeline.fit(features_train, target_train)#5:εκπαίδευση του μοντέλου
predicted_prices = pipeline.predict(features_test)#5:πρόβλεψη των τιμών για το σύνολο ελέγχου

for i in range(len(predicted_prices)):#6:εκτύπωση των πραγματικών τιμών, των προβλέψεων και της χώρας
    print(f"Χώρα: {features_test['Country'].iloc[i]}, Πραγματική τιμή: {target_test.iloc[i]}, Πρόβλεψη: {predicted_prices[i]}")
#6:υπολογισμός και εμφάνιση Root Mean Squared Error (RMSE) για αξιολόγηση της απόδοσης
rmse = mean_squared_error(target_test, predicted_prices, squared=False)
print(f"The root mean squared error (RMSE) of the KNN model is: {rmse}")
