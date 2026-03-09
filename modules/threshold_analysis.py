import numpy as np
import matplotlib.pyplot as plt

def compute_far_frr(genuine_scores, impostor_scores):

    thresholds = np.linspace(0,1,100)

    FAR = []
    FRR = []

    for t in thresholds:

        far = np.sum(impostor_scores >= t)/len(impostor_scores)
        frr = np.sum(genuine_scores < t)/len(genuine_scores)

        FAR.append(far)
        FRR.append(frr)

    return thresholds,FAR,FRR

def plot_roc(thresholds,FAR,FRR):

    plt.plot(thresholds,FAR,label="FAR")
    plt.plot(thresholds,FRR,label="FRR")

    plt.xlabel("Threshold")
    plt.ylabel("Error Rate")
    plt.legend()
    plt.title("Threshold Optimization")

    plt.show()