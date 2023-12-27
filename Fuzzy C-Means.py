
#pip install scikit-learn
#pip install scikit-fuzzy
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import skfuzzy as fuzz
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
    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(features.T, K, 2, error=0.005, maxiter=1000)
    cluster_membership = np.argmax(u, axis=0)

    # Plotting the results
    fig, ax = plt.subplots()
    colors = ['g', 'b', 'c', 'm', 'y', 'k']
    for j in range(K):
        ax.scatter(data[cluster_membership == j]['income'], data[cluster_membership == j]['debtinc'],
                c=colors[j], label=f'Cluster {j + 1}', marker='o')
        
    # Plot centroids
    for i in range(K):
        ax.scatter(cntr[i, 0], cntr[i, 1], marker='o', s=20, linewidths=3, color='red', label=f'Centroid {i + 1}')

    ax.legend()
    plt.xlabel('income')
    plt.ylabel('debtinc')
    plt.title('Fuzzy C-Means Clustering on Bank Loans')
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




