import pandas as pd
import matplotlib.pyplot as plt

# read the excel file
df = pd.read_csv('202310-11_trip_categoria_strada.csv')

# Count how many users
num_users = df['id_veicolo'].nunique()
print("Number of different users:", num_users)

# We apply filter about tot_km_categoria_strada because in the data we have some trips with no
# movements

df_filtered = df[df['tot_km_categoria_strada'] != 0.0]
trip_count_by_vehicle = df_filtered.groupby('id_veicolo')['id_viaggio'].nunique()

# Show how many trips for each user
print(trip_count_by_vehicle)

df['istante_start'] = pd.to_datetime(df['istante_start'], format='ISO8601')


df['data'] = df['istante_start'].dt.date
df_filtered = df[df['tot_km_categoria_strada'] != 0]

average_km_per_day_by_vehicle = df_filtered.groupby(['id_veicolo', 'data'])['tot_km_categoria_strada'].mean()
#print(average_km_per_day_by_vehicle)

average_km_per_day_overall = average_km_per_day_by_vehicle.groupby('id_veicolo').mean()
print(average_km_per_day_overall)

top_50_vehicles = average_km_per_day_overall.head(50)

# plt.figure(figsize=(12, 6))
# top_50_vehicles.plot(kind='bar', color='blue')
# plt.title('Average day Kms of 50 users')
# plt.xlabel('vehicle_id')
# plt.ylabel('AVG Kms')
# plt.show()

# plt.figure(figsize=(12, 6))
# plt.plot(top_50_vehicles.index, top_50_vehicles.values, linestyle='-', color='blue')
# plt.title('Distribution of Average day Kms of 50 users')
# plt.xlabel('vehicle_id')
# plt.ylabel('AVG Kms')
# plt.grid(True)
# plt.show()

print("------- URBAN ROAD -------------")
df_filtered_Urban = df_filtered[df_filtered['categoria_strada'] == 'U']

average_km_per_day_by_vehicle_U = df_filtered_Urban.groupby(['id_veicolo', 'data'])['tot_km_categoria_strada'].mean()
# print(average_km_per_day_by_vehicle)

average_km_per_day_overall_U = average_km_per_day_by_vehicle_U.groupby('id_veicolo').mean()
print(average_km_per_day_overall_U)

print("------- EXTRA-URBAN ROAD -------------")
df_filtered_EUrban = df_filtered[df_filtered['categoria_strada'] == 'E']

average_km_per_day_by_vehicle_E = df_filtered_EUrban.groupby(['id_veicolo', 'data'])['tot_km_categoria_strada'].mean()
# print(average_km_per_day_by_vehicle)

average_km_per_day_overall_E = average_km_per_day_by_vehicle_E.groupby('id_veicolo').mean()
print(average_km_per_day_overall_E)

print("------- HIGHWAY -------------")
df_filtered_A = df_filtered[df_filtered['categoria_strada'] == 'A']

average_km_per_day_by_vehicle_A = df_filtered_A.groupby(['id_veicolo', 'data'])['tot_km_categoria_strada'].mean()
# print(average_km_per_day_by_vehicle)

average_km_per_day_overall_A = average_km_per_day_by_vehicle_A.groupby('id_veicolo').mean()
print(average_km_per_day_overall_A)


plt.figure(figsize=(12, 6))

top_50_vehicles_A = average_km_per_day_overall_A.head(50)
top_50_vehicles_E = average_km_per_day_overall_E.head(50)
top_50_vehicles_U = average_km_per_day_overall_U.head(50)


plt.bar(top_50_vehicles_A.index, top_50_vehicles_A.values, label='Autostrada', alpha=0.7)
plt.bar(top_50_vehicles_E.index, top_50_vehicles_E.values, label='Extra-Urbana', alpha=0.7)
plt.bar(top_50_vehicles_U.index, top_50_vehicles_U.values, label='Urbana', alpha=0.7)

# Aggiungi le etichette e il titolo del grafico
plt.xlabel('vehicle_id')
plt.ylabel('Avg day Kms')
plt.title('Average day Kms of 50 users - per type of road')
plt.legend(title='Type of road')

# Mostra il grafico
plt.show()


trip_length_distribution = df_filtered.groupby(['id_veicolo','id_viaggio'])['tot_km_categoria_strada'].sum()

plt.figure(figsize=(12, 6))
plt.hist(trip_length_distribution, bins=30, color='skyblue', edgecolor='black')
plt.title('Distribuzione della Lunghezza dei Viaggi')
plt.xlabel('Lunghezza del Viaggio (km)')
plt.ylabel('Frequenza')
plt.grid(True)
plt.show()