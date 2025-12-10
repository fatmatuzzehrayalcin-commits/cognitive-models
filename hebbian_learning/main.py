import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def hebbian_learning(n_steps=200, eta=0.05):
    """
    Basit Hebbian öğrenme simülasyonu.
    x = presinaptik aktivasyon (0 veya 1)
    y = postsinaptik aktivasyon (0 veya 1)
    w = sinaptik ağırlık
    """
    w = 0.1  # başlangıç ağırlığı
    weights = []

    for _ in range(n_steps):
        # Rasgele aktivasyon (birlikte ateşleme olasılığı %30)
        x = np.random.rand() < 0.4
        y = np.random.rand() < 0.4

        # Hebbian kuralı
        if x and y:
            w += eta * 1  # birlikte ateşlerse güçlenir
        else:
            w -= eta * 0.01  # birlikte ateşlemezlerse hafif zayıflama

        # Ağırlığı sınırlayalım (0 ile 1 arasında)
        w = np.clip(w, 0, 1)
        weights.append(w)

    return np.array(weights)

def main():
    print("Hebbian Learning modeli çalışıyor...\n")

    weights = hebbian_learning(n_steps=300, eta=0.05)

    print(f"Son sinaptik ağırlık: {weights[-1]:.3f}")

    # Grafik çizimi
    plt.figure()
    plt.plot(weights, label="Sinaptik Ağırlık (w)")
    plt.xlabel("Zaman (adım)")
    plt.ylabel("Ağırlık (w)")
    plt.title("Hebbian Learning — Sinaptik Güçlenme")
    plt.legend()
    plt.tight_layout()

    output_file = "hebbian_learning_plot.png"
    plt.savefig(output_file)

    print(f"Grafik '{output_file}' dosyasına kaydedildi.")

if __name__ == "__main__":
    main()