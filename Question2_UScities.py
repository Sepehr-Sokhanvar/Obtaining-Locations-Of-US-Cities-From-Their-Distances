import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics as metrics


def loadData():
    D = np.zeros((20, 20))
    with open("UScities.txt") as file:
        for index, line in enumerate(file):
            numbers_in_line = []
            words_in_line = line.split()
            for word in words_in_line:
                if(word.isnumeric()):
                    numbers_in_line.append(word)
            D[index, :] = numbers_in_line

    # heat map of distance matrix
    plt.imshow(D)
    plt.title("Heatmap")
    plt.show()

    return D


def gramMatrix():
    D = loadData()
    D = D*D
    gram1 = np.zeros((20, 20))
    term4 = (1/(20*20))*np.sum(D)
    for i in range(20):
        term2 = (-1/20)*np.sum(D[i, :])
        for j in range(20):
            term1 = D[i, j]
            term3 = (-1/20)*np.sum(D[:, j])
            gram1[i, j] = -0.5*(term1+term2+term3+term4)
    return gram1


def PCA():
    grammatrix1 = gramMatrix()
    eigenvalues1, eigenvectors1 = np.linalg.eigh(grammatrix1)
    return np.flip(eigenvalues1), np.flip(eigenvectors1)


def matrix_P():
    eigenValues1, eigenVectors1 = PCA()
    singularValues = np.sqrt(eigenValues1)
    P = eigenVectors1[:, :2] @ np.diag(singularValues[:2])
    c = list(range(1, 21))
    cities = ["Boston", "Buffalo", "Chicago", "Dallas", "Denver", "Houston", "Los Angeles", "Memphis", "Miami", "Minneapolis", "New York",
              "Omaha", "Philadelphia", "Phoenix", "Pittsburgh", "Saint Louis", "Salt Lake City", "San Francisco", "Seattle", "Washington D.C"]
    cities.reverse()
    fig, ax = plt.subplots()
    ax.scatter(x=P[:, 0], y=P[:, 1], c=c, cmap="Set1")
    for i, txt in enumerate(cities):
        ax.annotate(txt, (P[i, 0], P[i, 1]))
    plt.xlabel('First Component')
    plt.ylabel('Second Component')
    plt.title('Dataset projection on the first and second pricipal components')
    plt.show()
    return P


def checkCorrect(P):
    print(metrics.pairwise_distances(P))
    return 0


P = matrix_P()
checkCorrect(P)
