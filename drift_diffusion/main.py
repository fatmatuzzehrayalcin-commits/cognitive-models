import pandas as pd
import matplotlib.pyplot as plt

def main():
    """
    Drift Diffusion Model (DDM) Veri Analizi:
    Katılımcı tepki sürelerinin (RT) temizlenmesi, betimsel istatistiklerin 
    hesaplanması ve koşullar arası karşılaştırmalı görselleştirme.
    """
    try:
        # I/O İşlemleri: Ham veri setinin içe aktarılması
        df = pd.read_csv("katilima_verisi.csv")
        
        # --- VERİ ÖN İŞLEME VE UÇ DEĞER FİLTRELEME (OUTLIER REMOVAL) ---
        ilk_sayi = len(df)
        # Bilişsel modelleme standartlarına göre makul olmayan (RT < 0.2s veya RT > 2.5s) 
        # tepki sürelerinin analiz dışı bırakılması
        df = df[(df['RT'] > 0.2) & (df['RT'] < 2.5)]
        son_sayi = len(df)
        print(f"Veri Temizleme Raporu: {ilk_sayi - son_sayi} adet uç değer (outlier) elendi.\n")
        
        # --- İSTATİSTİKSEL ANALİZ (BETİMSEL) ---
        print("--- DENEYSEL KOŞUL BAZLI ÖZET İSTATİSTİKLER ---")
        # Koşullara göre ortalama (mean) ve standart sapma (std) hesaplanması
        print(df.groupby('Condition')['RT'].describe()[['mean', 'std']])

        # --- BİLİMSEL GÖRSELLEŞTİRME ---
        plt.figure(figsize=(10,5))
        
        # 1. Grafik: Tepki Sürelerinin Frekans Dağılımı (Histogram)
        plt.subplot(1, 2, 1)
        plt.hist(df['RT'], bins=10, color="lightgreen", edgecolor='black', alpha=0.7)
        plt.title("Tepki Süresi Dağılım Analizi")
        plt.xlabel("Süre (sn)")
        plt.ylabel("Frekans")
        
        # 2. Grafik: Koşullar Arası Varyans ve Dağılım Kıyaslaması (Boxplot)
        plt.subplot(1, 2, 2)
        df.boxplot(column='RT', by='Condition', grid=False)
        plt.title("Koşul Bazlı Tepki Süresi Karşılaştırması")
        plt.xlabel("Deney Koşulu")
        plt.ylabel("Tepki Süresi (sn)")
        plt.suptitle("") # Pandas otomatik başlığının kaldırılması
        
        plt.tight_layout()
        plt.show() # Dinamik görselleştirme penceresini başlatır

    except Exception as e:
        print(f"Analiz Sırasında Bir Hata Oluştu: {e}")

if __name__ == "__main__":
    main()