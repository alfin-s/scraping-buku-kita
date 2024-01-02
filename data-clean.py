import pandas as pd
import re

# Baca file data-buku.csv
data = pd.read_csv('bukukita/data-buku.csv', encoding='utf-8')

# Hapus karakter khusus dari kolom 'Penerbit'
data['Penerbit'] = data['Penerbit'].apply(lambda x: re.sub(r"[^\w\s]", "", str(x)))

# Hapus karakter khusus dari kolom 'Text Bahasa'
data['Text Bahasa'] = data['Text Bahasa'].apply(lambda x: re.sub(r"[^\w\s]", "", str(x)))

# Simpan ke file Excel
data.to_excel('data-buku.xlsx', index=False)