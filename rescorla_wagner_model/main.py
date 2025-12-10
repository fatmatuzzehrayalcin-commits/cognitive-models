# Rescorla-Wagner bilişsel öğrenme modeli
# ΔV = α * β * (λ - V)

import matplotlib
# PowerShell veya GUI olmayan ortamlarda bile çalışsın diye
matplotlib.use("Agg")
import matplotlib.pyplot as plt


class RescorlaWagner:
    def __init__(self, alpha=0.3, beta=0.5, initial_v=0.0):
        self.alpha = alpha
        self.beta = beta
        self.v = initial_v

    def update(self, lam):
        """Bir denemede V değerini güncelle."""
        delta_v = self.alpha * self.beta * (lam - self.v)
        self.v += delta_v
        return self.v


def simulate(lam_sequence, alpha=0.3, beta=0.5):
    """
    Verilen λ dizisiyle (US var/yok bilgisi) modeli çalıştır.
    lam_sequence: örneğin [1,1,1,...] veya [1,1,...,0,0,...]
    """
    model = RescorlaWagner(alpha=alpha, beta=beta)
    v_values = []

    for lam in lam_sequence:
        v = model.update(lam)
        v_values.append(v)

    return v_values


def main():
    print("Rescorla-Wagner modeli başlatılıyor...\n")

    # 1) Yalnızca edinim: 50 deneme boyunca λ = 1
    acq = simulate([1] * 50)

    # 2) Edinim + sönme: 30 deneme λ = 1, 20 deneme λ = 0
    acq_ext = simulate([1] * 30 + [0] * 20)

    print(f"Yalnız edinim - son deneme V: {acq[-1]:.3f}")
    print(f"Edinim + sönme - son deneme V: {acq_ext[-1]:.3f}\n")

    # Grafik çizimi
    plt.figure()
    plt.plot(acq, label="Yalnız Edinim")
    plt.plot(acq_ext, label="Edinim + Sönme")
    plt.axvline(30, linestyle="--", label="Sönmenin Başlangıcı")

    plt.xlabel("Deneme")
    plt.ylabel("İlişki Gücü (V)")
    plt.title("Rescorla-Wagner Öğrenme Modeli")
    plt.legend()
    plt.tight_layout()

    # Grafik dosyaya kaydediliyor
    output_file = "rescorla_wagner_plot.png"
    plt.savefig(output_file)

    print(f"Grafik '{output_file}' dosyasına kaydedildi.")
    print("Proje başarıyla çalıştı!")


if __name__ == "__main__":
    main()