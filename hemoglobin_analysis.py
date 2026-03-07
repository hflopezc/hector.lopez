"""
hemoglobin_analysis.py

Script para analizar la proteína hemoglobina beta humana.

Este programa:
- Lee una secuencia de aminoácidos desde un archivo
- Calcula la longitud de la secuencia
- Cuenta la frecuencia de cada aminoácido
- Calcula el peso molecular aproximado
- Calcula el porcentaje de aminoácidos hidrofóbicos
- Guarda los resultados en un archivo JSON
"""

# Importamos la librería json para guardar resultados
import json

# Abrimos el archivo que contiene la secuencia limpia
with open("hemoglobin_clean.txt", "r") as f:
    # Leemos la secuencia y eliminamos espacios o saltos de línea
    sequence = f.read().strip()

# Mostrar información básica de la proteína
print("Proteína: Subunidad beta de la hemoglobina")
print("Longitud de la secuencia:", len(sequence))
print("Primeros 20 aminoácidos:", sequence[:20])

# Lista de los 20 aminoácidos estándar
amino_acids = list("ACDEFGHIKLMNPQRSTVWY")

# Diccionario para guardar el conteo de aminoácidos
aa_counts = {}

# Contar cuántas veces aparece cada aminoácido en la secuencia
for aa in amino_acids:
    aa_counts[aa] = sequence.count(aa)

print("\nComposición de aminoácidos:")
for aa, count in aa_counts.items():
    print(aa, count)

# Diccionario con pesos moleculares aproximados de cada aminoácido
aa_weights = {
"A":89.09,"C":121.15,"D":133.10,"E":147.13,"F":165.19,
"G":75.07,"H":155.16,"I":131.17,"K":146.19,"L":131.17,
"M":149.21,"N":132.12,"P":115.13,"Q":146.15,"R":174.20,
"S":105.09,"T":119.12,"V":117.15,"W":204.23,"Y":181.19
}

# Función para calcular el peso molecular de una secuencia
def calcular_peso_molecular(seq):

    peso_total = 0

    # Sumar el peso de cada aminoácido
    for aa in seq:
        if aa in aa_weights:
            peso_total += aa_weights[aa]

    return peso_total

# Llamar la función para calcular el peso molecular
peso_molecular = calcular_peso_molecular(sequence)

print("\nPeso molecular aproximado:", peso_molecular)

# Lista de aminoácidos hidrofóbicos
hidrofobicos = ["A","V","I","L","M","F","W","Y"]

conteo_hidro = 0

# Contar cuántos aminoácidos hidrofóbicos hay
for aa in sequence:
    if aa in hidrofobicos:
        conteo_hidro += 1

# Calcular porcentaje hidrofóbico
porcentaje_hidro = (conteo_hidro / len(sequence)) * 100

print("Porcentaje de aminoácidos hidrofóbicos:", porcentaje_hidro)

# Crear diccionario con resultados
resultados = {
"nombre_proteina": "Hemoglobina beta humana",
"longitud_secuencia": len(sequence),
"conteo_aminoacidos": aa_counts,
"peso_molecular": peso_molecular,
"porcentaje_hidrofobico": porcentaje_hidro
}

# Guardar resultados en archivo JSON
with open("hemoglobin_results.json","w") as f:
    json.dump(resultados,f,indent=4)

print("\nResultados guardados en hemoglobin_results.json")
