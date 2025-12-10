import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def forgetting_curve(time_points, k=0.2):
    """
    Ebbinghaus Forgetting Curve:
    R(t) = exp(-k * t)
    """
    return np.exp(-k * time_points)

def main():
    print("Ebbinghaus Forgetting Curve model çalışıyor...\n")

    # Zaman noktaları (0'dan 10'a kadar)
    t = np.linspace(0, 10, 200)

    # Hatırlama seviyeleri
    R = forgetting_curve(t, k=0.25)

    # Grafik çizimi
    plt.figure()
    plt.plot(t, R, label="Unutma Eğrisi (k=0.25)")
    plt.xlabel("Zaman")
    plt.ylabel("Hatırlama (R)")
    plt.title("Ebbinghaus Unutma Eğrisi Modeli")
    plt.legend()
    plt.tight_layout()

    output_file = "forgetting_curve_plot.png"
    plt.savefig(output_file)

    print(f"Grafik '{output_file}' dosyasına kaydedildi.")

if __name__ == "__main__":
    main()