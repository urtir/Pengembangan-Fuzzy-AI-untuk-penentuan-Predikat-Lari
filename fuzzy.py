import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Load dataset
data = pd.read_csv('guns.csv')

# Fuzzy logic variables
berat = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'berat')  # Berat dalam kg
panjang_kaliber = ctrl.Antecedent(np.arange(0, 70.1, 0.1), 'panjang_kaliber')  # Panjang kaliber dalam inci
harga = ctrl.Antecedent(np.arange(0, 10001, 1), 'harga')  # Harga dalam dollar

mobilitas = ctrl.Consequent(np.arange(0, 101, 1), 'mobilitas')  # Tingkat mobilitas (0-100)

# Membership functions
berat['ringan'] = fuzz.trimf(berat.universe, [0, 3, 6])
berat['sedang'] = fuzz.trimf(berat.universe, [3, 6, 9])
berat['berat'] = fuzz.trimf(berat.universe, [6, 9, 10])

panjang_kaliber['pendek'] = fuzz.trimf(panjang_kaliber.universe, [0, 20, 40])
panjang_kaliber['sedang'] = fuzz.trimf(panjang_kaliber.universe, [20, 40, 60])
panjang_kaliber['panjang'] = fuzz.trimf(panjang_kaliber.universe, [40, 60, 70])

harga['murah'] = fuzz.trimf(harga.universe, [0, 2000, 4000])
harga['sedang'] = fuzz.trimf(harga.universe, [2000, 4000, 6000])
harga['mahal'] = fuzz.trimf(harga.universe, [4000, 6000, 10000])

mobilitas['rendah'] = fuzz.trimf(mobilitas.universe, [0, 50, 100])
mobilitas['sedang'] = fuzz.trimf(mobilitas.universe, [0, 50, 100])
mobilitas['tinggi'] = fuzz.trimf(mobilitas.universe, [0, 50, 100])

# Rules
rule1 = ctrl.Rule(berat['ringan'] & panjang_kaliber['pendek'] & harga['murah'], mobilitas['tinggi'])
rule2 = ctrl.Rule(berat['sedang'] & panjang_kaliber['sedang'] & harga['sedang'], mobilitas['sedang'])
rule3 = ctrl.Rule(berat['berat'] & panjang_kaliber['panjang'] & harga['mahal'], mobilitas['rendah'])

# Control System
mobilitas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
mobilitas_output = ctrl.ControlSystemSimulation(mobilitas_ctrl)

# Evaluasi setiap senjata
list_layak_mobilitas = []
for index, row in data.iterrows():
    mobilitas_output.input['berat'] = row['berat']
    mobilitas_output.input['panjang_kaliber'] = row['panjang_kaliber']
    mobilitas_output.input['harga'] = row['harga']
    
    mobilitas_output.compute()
    
    mobilitas_val = mobilitas_output.output['mobilitas']
    list_layak_mobilitas.append('Layak' if mobilitas_val >= 50 else 'Tidak Layak')

# Output hasil
data['Layak_Mobilitas'] = list_layak_mobilitas
print(data[['id_serial', 'Layak_Mobilitas']])
