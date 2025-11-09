import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tabulate

data = pd.read_csv('nilai_siswa.csv', sep=';')

data.info()
data.head()
data.describe()

print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0]) 

# MTK
matematika = data[data['Matpel'] == 'Matematika']
print("\n Nilai Matematika:")
print(matematika)

# B. INGGRIS
bahasa_inggris = data[data['Matpel'] == 'Bahasa Inggris']
print("\n Nilai B. Inggris:")
print(bahasa_inggris)

# B. INDONESIA
bahasa_indonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print("\n Nilai B. Indonesia:")
print(bahasa_indonesia)

# PRODUKTIF
produktif = data[data['Matpel'] == 'Produktif']
print("\n Nilai Produktif:")
print(produktif)



rata = data.groupby("Matpel")["Nilai"].mean()
rata.plot(kind='bar')
plt.title('Rata-rata Nilai Siswa per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Rata-rata Nilai')
plt.show()


sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai Siswa per Mata Pelajaran')
plt.show()


sns.boxplot(x="Matpel", y="Nilai", data=data)
plt.title("Sebaran Nilai per Mata Pelajaran")
plt.show()



# ANALISIS & PERTANYAAN

#1. Mata pelajaran mana yang memiliki rata-rata nilai tertinggi?
 # = Matpel dengan rata rata tertinggi adalah Fisika, yaitu 90.22

#2. Mapel mana yang memiliki nilai terendah?
 # = Matpel dengan nilai terendah adalah B. Indonesia, yaitu 60

#3. Bagaimana visualisasi membantu dalam memahami data?
 # = - Grafik batang (bar chart) memudahkan kita membandingkan rata-rata nilai antar mapel.
 # = - Boxplot memperlihatkan sebaran nilai tiap mapel (mana yang stabil, mana yang bervariasi).
 # = - Dengan visualisasi, kita bisa lebih cepat mengenali pola dan perbedaan tanpa harus membaca angka satu   per satu.


# REFLEKSI

# saya belajar cara mengolah data dengan pyhton, menghitung nilai statistik dasar, serta menampilkan hasil analisis dalam bentuk grafik visual yang mudah di pahami.

# tantangan yang saya hadapi mungkin hanya memastikan tidak ada typo

# ya, AI dapat membantu dalam menganalisi data