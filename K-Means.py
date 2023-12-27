import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def pilih_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        data = pd.read_csv(file_path)
        return data
    else:
        print("Pemilihan file dibatalkan.")

def jumlah_cluster():
    K=int(input("masukan jumlah cluseter : ") )
    return K

def hasil(data,K):
    features = data[['income', 'debtinc']]
    kmeans = KMeans(n_clusters=K)
    data['Cluster_KMeans'] = kmeans.fit_predict(features)

    plt.scatter(data['income'], data['debtinc'], c=data['Cluster_KMeans'], cmap='rainbow')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=30, c='black', label='Centroids')
    plt.xlabel('income')
    plt.ylabel('debtinc')
    plt.title(f'Cluster_KMeans Clustering')
    plt.legend()
    plt.show()

a=0
while a < 4 :
    print("1.Pilih Data CSV ")
    print("2.Masukan Jumlah Cluster ")
    print("3.Tampilkan Hasil ")
    print("4.Keluar")
    i = int(input("masukan pilihan : " ))
    if i == 1 :
        data = pilih_file()
    elif i == 2 :
        K = jumlah_cluster()
    elif i == 3 :
        hasil(data,K)
    else :
        break


