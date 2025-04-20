import random
import csv
from datetime import datetime, timedelta

# Normal saat araligi (08:30 - 18:00)
normal_start = datetime.strptime("08:30", "%H:%M")
normal_end = datetime.strptime("18:00", "%H:%M")

# Absurt saat araliklari
absurt_ranges = [
    (datetime.strptime("00:00", "%H:%M"), datetime.strptime("08:29", "%H:%M")),
    (datetime.strptime("18:01", "%H:%M"), datetime.strptime("23:59", "%H:%M"))
]

def generate_random_time(start, end):
    delta = end - start
    random_minutes = random.randint(0, int(delta.total_seconds() / 60))
    return (start + timedelta(minutes=random_minutes)).strftime("%H:%M")

# Veriler
data = []

# 1000 normal saat verisi
for _ in range(1000):
    time = generate_random_time(normal_start, normal_end)
    data.append((time, 0))

# 200 absurt saat verisi
for _ in range(200):
    range_choice = random.choice(absurt_ranges)
    time = generate_random_time(range_choice[0], range_choice[1])
    data.append((time, 1))

# Verileri karistiralim
random.shuffle(data)

# CSV dosyasina yazalim
with open("time_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["saat_dakika", "label"])  # Baslik satiri
    writer.writerows(data)

print("CSV dosyasi basariyla olusturuldu! (time_data.csv)")