import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. CSV'den veriyi oku
data = pd.read_csv('time_data.csv')

# 2. 'saat:dakika' -> dakikaya çevir
def convert_to_minutes(time_str):
    saat, dakika = map(int, time_str.split(':'))
    return saat * 60 + dakika

data['minutes'] = data['saat_dakika'].apply(convert_to_minutes)

# Özellikler (X) ve hedef değişken (y)
X = data[['minutes']]
y = data['label']

# 3. Veriyi eğitim ve test setine böl
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Modeli oluştur ve eğit
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test seti başarımını yazdır
accuracy = model.score(X_test, y_test)
print(f"Model Test Accuracy: {accuracy:.2f}")

# 5. Modeli kaydet
joblib.dump(model, 'time_anomaly_detector.pkl')

print("Model eğitildi ve kaydedildi!")
