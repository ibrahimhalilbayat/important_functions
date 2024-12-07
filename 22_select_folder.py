import tkinter as tk
from tkinter import filedialog
from pandas import read_excel, read_csv


def select_file():
    '''
    Excell dosyasını bilgisayardan seçip, görselleştiren fonksiyon
    '''
    try:
        root = tk.Tk()
        root.withdraw() 

        print("\n\nDosya Seçimi Yapınız\n\n")
        file_path = filedialog.askopenfilename(title="Select a File",
                                               filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")])

        if file_path:
            print(f"Seçilen Dosya: {file_path}")
            return file_path
        else:
            print("Dosya Seçilmedi.")
            return None
    except Exception as e:
        print(f"Dosya seçiminde bir hata oluştu: {e}")



df_path = select_file()

while True:
    if df_path.endswith('.xlsx') or df_path.endswith('.xls'):
        df = read_excel(df_path)
        break
    elif df_path.endswith('.csv'):
        df = read_csv(df_path)
        break
    else:
        print("Lütfen xlsx, xls ya da csv uzantılı bir dosya seçin...")
        df_path = select_file()