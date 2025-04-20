import joblib

# Modeli yükle
model = joblib.load('time_anomaly_detector.pkl')

# Saat formatını dakikaya çeviren fonksiyon
def convert_to_minutes(time_str):
    saat, dakika = map(int, time_str.split(':'))
    return saat * 60 + dakika

# Kullanıcıdan saat inputu al
time_input = input("Saat giriniz (HH:MM formatında): ")

# Dakikaya çevir
time_in_minutes = convert_to_minutes(time_input)

# Tahmin yap
prediction = model.predict([[time_in_minutes]])

# Sonucu yaz
if prediction[0] == 1:
    print("🔔 Uyarı: Anormal saat! Admine bildirim gönderilebilir.")
else:
    print("✅ Normal saat.")
