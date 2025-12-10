import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def drift_diffusion_simulation(
    drift=0.3,
    noise=1.0,
    boundary=1.0,
    dt=0.01,
    max_time=3.0,
    n_trials=500
):
    """
    Basit Drift Diffusion Modeli (DDM) simülasyonu.
    Her denemede karar sinyali 0'dan başlar.
    Zaman içinde drift + noise ile yükselir veya düşer.
    Üst sınır (doğru) veya alt sınır (yanlış) karar üretir.
    """
    reaction_times = []
    choices = []  # 1 = doğru sınır, 0 = yanlış sınır

    for _ in range(n_trials):
        x = 0  # karar sinyali başlangıcı
        t = 0

        while abs(x) < boundary and t < max_time:
            dx = drift * dt + noise * np.sqrt(dt) * np.random.randn()
            x += dx
            t += dt

        reaction_times.append(t)
        choices.append(1 if x >= boundary else 0)

    return np.array(reaction_times), np.array(choices)

def main():
    print("Drift Diffusion Model çalışıyor...\n")

    rt, choices = drift_diffusion_simulation(
        drift=0.3,
        noise=1.0,
        boundary=1.0,
        n_trials=1000
    )

    accuracy = np.mean(choices)
    mean_rt = np.mean(rt)

    print(f"Doğruluk: {accuracy:.3f}")
    print(f"Ortalama Tepki Süresi: {mean_rt:.3f} sn\n")

    # Grafik çizimi
    plt.figure(figsize=(10,4))

    # Tepki süresi histogramı
    plt.subplot(1,2,1)
    plt.hist(rt, bins=30, color="blue", alpha=0.7)
    plt.title("Tepki Süresi Dağılımı")
    plt.xlabel("Tepki Süresi (s)")
    plt.ylabel("Frekans")

    # Doğru/yanlış oranları
    plt.subplot(1,2,2)
    plt.bar(["Doğru", "Yanlış"], [accuracy, 1-accuracy], color=["green", "red"])
    plt.title("Karar Sonuçları")
    plt.ylim(0,1)

    plt.tight_layout()

    output_file = "drift_diffusion_plot.png"
    plt.savefig(output_file)

    print(f"Grafik '{output_file}' dosyasına kaydedildi.")


if __name__ == "__main__":
    main()