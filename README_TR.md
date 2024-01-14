# Special-Triangles-Finder

Bu Python script'i, kullanıcının sağladığı X ve Y değerlerine dayalı özel üçgenleri bulan bir sınıf içerir.
formül: Pisagor Teoremi:`|x² - y²|` ve `2xy` ve `x² + y²`

## Açıklama

Bu projede, kullanıcı tarafından belirlenen X ve Y değerlerine bağlı olarak özel üçgenleri bulan bir Python sınıfı (`SpeTriFinder`) bulunmaktadır. Üçgenler, Pythagorean teoremi kullanılarak hesaplanmakta ve en küçük hallerine indirgenmektedir.


## Gereksinimler

Projeyi çalıştırmak için aşağıdaki bağımlılıklar gereklidir:

- Python 3.x

## Kurulum

1. **Projeyi İndirme:**
   - Projeyi indirmek için terminal veya komut istemcisine şu komutu yazın:
     ```bash
     git clone https://github.com/Mefamex/Special-Triangles-Finder.git
     ```

2. **Proje Dizinine Girme:**
   - İndirilen projenin dizinine gitmek için terminal veya komut istemcisine şu komutu yazın:
     ```bash
     cd Special-Triangles-Finder
     ```

3. **Script'i Çalıştırma:**
   - Script'i çalıştırmak için terminal veya komut istemcisine şu komutu yazın:
     ```bash
     python main.py
     ```

## Nasıl Kullanılır

Projenin içindeki `main.py` dosyasını kullanarak `SpeTriFinder` sınıfını aşağıdaki gibi kullanabilirsiniz.

```python
# Örnek Kullanım
from main import SpeTriFinder

# Kullanıcı tarafından belirlenen X ve Y değerleri
user_X = 10
user_Y = 10

# SpeTriFinder sınıfını oluştur
finder = SpeTriFinder(user_X, user_Y)

# veya
finder.run_finder(5, 5, show=False)

# veya 
SpeTriFinder(3, 3)

# veya
big = SpeTriFinder(100, 100, False)
print(big.spec_tri[-1])
```


## Örnek Sonuçlar

### Örnek 1:
```plaintext
max values and side: 10, 10, 200
18 special triangles found
[3, 4, 5]
[5, 12, 13]
[7, 24, 25]
[8, 15, 17]
[9, 40, 41]
[11, 60, 61]
[12, 35, 37]
[13, 84, 85]
[15, 112, 113]
[16, 63, 65]
[17, 144, 145]
[20, 21, 29]
[28, 45, 53]
[33, 56, 65]
[36, 77, 85]
[39, 80, 89]
[48, 55, 73]
[65, 72, 97]
Done!  ---------------
```

### Örnek 2:
```plaintext
max values and side: 5, 5, 50
4 special triangles found
[3, 4, 5]
[5, 12, 13]
[7, 24, 25]
[8, 15, 17]
Done!  ---------------
```
