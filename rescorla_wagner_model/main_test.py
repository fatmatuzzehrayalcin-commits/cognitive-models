import os, sys

print("====== PYTHON ÇALIŞTI ======")
print("Çalıştırılan Python:", sys.executable)
print("Mevcut Dizin      :", os.getcwd())

print("\nmain.py dosyası var mı?:", os.path.exists("main.py"))

if os.path.exists("main.py"):
    print("\n--- main.py içeriği ---")
    with open("main.py", "r", encoding="utf-8") as f:
        print(f.read())
    print("-------- SON --------")
else:
    print("main.py bulunamadı!")