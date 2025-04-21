import requests #1: αίτηση για δεδομένα καιρού
import pandas as pd #1:ανάλυση και χειρισμός δεδομένων
from sklearn.model_selection import train_test_split #1:εκπαίδευση και έλεγχο
from sklearn.linear_model import LinearRegression #1:γραμμική παλινδρόμηση
from sklearn.metrics import mean_squared_error #1:αξιολόγηση απόδοσης μοντέλου, μέσο τετραγωνικό σφάλμα
import matplotlib.pyplot as plt #1:επεικόνηση δεδομένων

api_key = '785576e42ec1d7dcb9c9cb0ea0677943' #2:το κλειδί εισόδου στα δεδομένα
city = 'Thessaloniki, GR'  #2:εισαγωγή επιθυμητής πολης προς μελετη 
#3:κάνουμε το request για να λάβουμε την πρόβλεψη
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}' #3:δημιουργία url
response = requests.get(url)#3:αίτημα βήματος1
data = response.json()#3:αποθήκευση απάντησης σε μεταβλητή

dates = [] #3:δημιουργία 3 κενων θεσεων 
temperatures = []
descriptions = []

if data['cod'] == '200': #4:έλεγχος επιτυχίας που ισουται με 200
    
    for forecast in data['list']: #4:ανάλυση λίστας δεδομένων που λάβαμε 
        date_time = forecast['dt_txt'] #4:ημερομινίας ώρας
        temperature = forecast['main']['temp'] - 273.15 #4:θερμοκρασίας και μετατροπή σε κελσίου
        description = forecast['weather'][0]['description'] #4:περιγραφή κατάστασης καιρού

        timestamp = pd.to_datetime(date_time).timestamp() #4:τα δεδομένα γίνονται αριθμητικά μέσω timestamp
        #4:τα δεδομένα απο κάθε πρόβλεψη προστίθενται σε λίστες
        dates.append(timestamp)#4:λίστα ημερομηνιών
        temperatures.append(temperature)#4:λίστα θερμοκρασιών
        descriptions.append(description)#4:λίστα κατάστασης καιρού

    
    weather_data = pd.DataFrame({ #5:dataframe για αποθήκευση δεδομένων
        'Date and Time': dates,#5:αριθμητική αναπαράσταση ημερομηνιών-ωρών
        'Temperature (°C)': temperatures,#5:θερμοκρασία κελσίου
        'Description': descriptions#5:καστάσταση καιρού
    })

    print("Weather forecast for", city) #5:εμφάνιση δεδομένων
    print(weather_data)

    X = weather_data[['Date and Time']] #5:προετοιμασία δεδομένων για μηχανική μάθηση
    y = weather_data['Temperature (°C)']

    #5:διαχωρισμός δεδομένων εκπαίδευσης-ελέγχου
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   
    #6:δημιουργία και εκπαίδευση μοντέλου γραμμικής παλινδρόμησης
    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)#6:πρόβλεψη θερμοκρασίας
    mse = mean_squared_error(y_test, predictions)#6:μέσο τετραγωνικό σφάλμα
    print("Mean Squared Error:", mse)#6:εμφάνιση ΜΤΣ

    #7:απεικόνηση προβλέψεων με γράφημα
    plt.scatter(X_test, y_test, color='yellow')#7:κίτρινο=πραγματικές θερμοκρασίες
    plt.plot(X_test, predictions, color='pink', linewidth=2)#7:ροζ προβλεπόμενες
    plt.xlabel("Date and Time")#7:ορισμός ετικέτας ημερομηνίας-ώρας
    plt.ylabel("Temperature (°C)")#7:ορισμός ετικέτας θερμοκρασίας
    plt.title("Weather Temperature Prediction")#7:ορισμός τίτλου
    plt.show()#:εμφάνιση γραφήματος

else:
    print(f"Error: {data['message']}")#7:μήνυμα λάθους πρόσβασης API
