# Ozel-Ucgenler-Special-Triangles-2024

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
     git clone https://github.com/Mefamex/Ozel-Ucgenler-Special-Triangles-2024.git
     ```

2. **Proje Dizinine Girme:**
   - İndirilen projenin dizinine gitmek için terminal veya komut istemcisine şu komutu yazın:
     ```bash
     cd SpeTriFinder
     ```

3. **Script'i Çalıştırma:**
   - Script'i çalıştırmak için terminal veya komut istemcisine şu komutu yazın:
     ```bash
     python spe_tri_finder.py
     ```
     veya
     ```bash
     python3 spe_tri_finder.py
     ```
     - `spe_tri_finder.py` dosyasının adı script'in adına göre değişebilir.

## Nasıl Kullanılır

Projenin içindeki `spe_tri_finder.py` dosyasını kullanarak `SpeTriFinder` sınıfını aşağıdaki gibi kullanabilirsiniz.

```python
# Örnek Kullanım
from spe_tri_finder import SpeTriFinder

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
max values and side: 10, 10, 100
Running...  X: 9  
8 special triangles found
[1, 1, 1]
[3, 4, 5]
[5, 12, 13]
[7, 24, 25]
[9, 40, 41]
[11, 60, 61]
[13, 84, 85]
[15, 112, 113]
Done!  ---------------
```
### Örnek 2:
```plaintext
max values and side: 5, 5, 25
Running...  X: 4  
3 special triangles found
[1, 1, 1]
[3, 4, 5]
[5, 12, 13]
Done!  ---------------
```
