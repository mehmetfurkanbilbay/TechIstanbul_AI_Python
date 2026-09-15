# ÖDEV SORULARI

---

## Yapay Zeka(AI) Nedir?

**Yapay Zeka** insana zekasına özgü bilişsel fonksiyonları sergileyen yapay bir işletim sistemidir.
Özellikle algılama, öğrenme, düşünme, problem çözme, karar verme ve iletişim kurma gibi yeteneklere sahiptir.
Yapay Zeka tek bir teknolojiden ibaret değildir. Makine Öğrenimi, Derin Öğrenme ve Doğal Dil İşleme gibi alt dallarla çalışır.


## Makine Öğrenmesi(ML) Nedir?

**Makine Öğrenmesi**, bilgisayarların insanlar tarafından açıkça programlanmaya ihtiyaç duymadan, verilerden öğrenmesini, kalıpları (örüntüleri) keşfetmesini ve bu sayede kararlar veya tahminler yapmasını sağlayan bir yapay zeka alt kümesidir.

## Derin Öğrenme (DL) Nedir?

**Derin öğrenme (Deep Learning)**,bilgisayarlara verileri insan beyninden esinlenen yapay sinir ağları vasıtasıyla işlemeyi öğreten bir yapay zeka (AI) ve makine öğrenimi (ML) alt kümesidir. İnsan beynindeki nöronların çalışma şeklini taklit eden çok katmanlı yapay sinir ağlarını kullanarak, bilgisayarların büyük ve karmaşık veri kümelerinden kendi kendilerine anlam çıkarmasını sağlar.

## Büyük Dil Modeli(LLM) Nedir?

**LLM**,insan dilini anlamak, işlemek ve yeni metinler üretmek için milyarlarca kelimelik devasa veri setleriyle eğitilmiş bir yapay zeka teknolojisidir.

## Günlük Hayattan Örnekler
>Otonom Sürüş (Sürücüsüz Araçlar): Çevredeki yayaları, araçları ve trafik ışıklarını anlık tespit ederek kazaları önleme ve insan müdahalesi olmadan güvenli seyahat etme problemini çözer.

>Akıllı Çeviri Sistemleri: Farklı dilleri konuşan insanların birbirleriyle hiç yabancı dil bilmeseler bile anında ve akıcı bir şekilde anlaşabilmesi problemini çözer.

>Hastalık Erken Teşhisi: Doktorların gözden kaçırabileceği tıbbi görüntüleri (röntgen, MR) inceleyerek kanser gibi ciddi hastalıkları çok erken evrede yakalama problemini çözer.

>Kredi Kartı Dolandırıcılık Tespiti: Banka hesaplarındaki normal dışı ve şüpheli harcamaları anında fark edip kartı bloke ederek hırsızlık problemini çözer.

>Tarımda Akıllı Sulama ve İlaçlama: Tarlalardaki ürünlerin hangilerinin hasta veya susuz olduğunu kameralarla anlayıp sadece ihtiyacı olan bölgeye müdahale ederek su ve ilaç israfı problemini çözer.

## Supervised Learning (Gözetimli Öğrenme)

Bilgisayara verileri hem soruları hem de doğru cevapları birlikte vererek eğitme yöntemidir.
Örneğin, bir bilgisayara binlerce kedi ve köpek fotoğrafını altlarında "Kedi" veya "Köpek" yazısıyla göstererek hayvanları ayırt etmeyi öğretmek.

## Unsupervised Learning (Gözetimsiz Öğrenme)

Bilgisayara sadece ham verileri verip, doğru cevapları söylemeden verinin içindeki benzerlikleri ve gizli kalıpları kendisinin bulmasını istemektir.
Örneğin, Bir alışveriş sitesinin müşteri harcamalarını inceleyerek insanları "az harcayanlar" ve "çok harcayanlar" diye etiket olmadan gruplara ayırması.

## Reinforcement Learning (Takviyeli Öğrenme)

Bilgisayarın bir ortamda deneme-yanılma yaparak, doğru hamlelerinde ödül, yanlış hamlelerinde ise ceza alarak en iyi stratejiyi kendi kendine öğrenmesidir.
Örneğin, Bir yapay zeka robotunun satranç oynarken maç kazandıkça puan alması ve bu sayede yenilmez bir strateji geliştirmeyi öğrenmesi.

---

## Classification mı, Regression mı?

- Classification (Sınıflandırma): Verileri "Evet/Hayır", "Kedi/Köpek/Kuş" gibi net ve birbirinden ayrı kategorilere (gruplara) ayırmak için kullanılır.
- Regression (Regresyon): Fiyat, sıcaklık veya puan gibi sürekli ve sayısal bir değeri tahmin etmek için kullanılır.


|**Örnek Senaryo**   |**Türü** |**Nedeni**   |
|---|---|---|
|**Ev fiyatı tahmini**   |**Regression**   |Çıktı olarak 1.250.000 TL gibi sürekli bir sayı tahmin edilir.   |
|**E-posta spam tespiti**   |**Classification**   |E-postayı "Spam" veya "Güvenli" şeklinde iki gruba ayırır.   |
|**Sınav puanı tahmini**   |**Regression**   |Öğrencinin alacağı 85 veya 92 gibi sayısal bir notu hedefler.   |
|**Müşteri terk eder/etmez tahmini**   |**Classification**   |Sonuç "Ayrılacak" veya "Kalacak" şeklinde kategoriktir.   |

## Feature ve Label

* Feature (Özellik): Yapay zekanın tahmin yaparken ipucu olarak kullandığı, girdi olarak verdiğimiz tüm bilgilere denir.
* Label (Etiket): Yapay zekanın bulmaya çalıştığı, verinin nihai doğru cevabı veya hedef çıktısıdır.
>**“Ders çalışma saati sınavı geçti/geçmedi”** örneğinde:
* Feature (Özellik): Ders çalışma saati 
  * Çünkü tahmini bu sayıya bakarak yapacağız.
* Label (Etiket): Sınavı geçti/geçmedi sonucu 
  * Çünkü öğrenmek istediğimiz ana hedef budur.

## Training ve Inference

* **Training (Eğitim)**: Modelin eldeki geçmiş verileri ve doğru cevapları inceleyerek konunun mantığını kavradığı ve matematiksel kurallar geliştirdiği öğrenme aşamasıdır.
  * Örnek Cümle: "Model, geçmiş yıllardaki binlerce öğrencinin devamsızlık ve not verilerini günlerce inceleyerek başarıyı nelerin etkilediğini öğrendi.
* **Inference (Çıkarım/Tahmin)**: Eğitimi bitmiş olan hazır modelin önüne ilk defa gelen yepyeni bir veriyi koyup ondan bir tahminde bulunmasını isteme aşamasıdır.
    *"Sisteme bu yıl yeni kayıt olan Ahmet'in verilerini girdiğimizde, model onun yıl sonunda başarılı olacağını tahmin etti."

## Python AI Araçları

* **NumPy:** Yapay zekanın ihtiyaç duyduğu büyük sayı listelerini ve çok boyutlu matematiksel tabloları (matrisleri) bilgisayar hafızasında çok hızlı işlememizi sağlayan kütüphanedir.
* **Pandas:** Excel tablolarına benzeyen satır ve sütunlardan oluşan verileri kolayca yüklememizi, temizlememizi ve düzenlememizi sağlayan bir veri analizi aracıdır.
* **Matplotlib:** Eldeki karmaşık verileri veya yapay zeka sonuçlarını çizgiler, barlar ve grafikler yardımıyla görselleştirerek anlaşılır hale getiren çizim kütüphanesidir.
* **Scikit-learn:** İçinde hazır makine öğrenmesi algoritmaları barındıran; model kurmayı, eğitmeyi ve test etmeyi sadece birkaç satır kodla yapmamızı sağlayan temel kütüphanedir.

```python
# Gerekli kütüphaneleri çağırıyoruz
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Veriyi hazırlıyoruz (Feature: Evin metrekaresi)
ev_boyutu = np.array([[50], [80], [100], [120]])

# 2. Doğru cevapları giriyoruz (Label: Evin fiyatı - Bin TL cinsinden)
ev_fiyati = np.array([500, 800, 1000, 1200])

# 3. Boş bir makine öğrenmesi modeli oluşturuyoruz
model = LinearRegression()

# 4. Modeli verilerle eğitiyoruz (Training)
model.fit(ev_boyutu, ev_fiyati)

# 5. Yeni bir evin fiyatını tahmin ediyoruz (Inference)
yeni_ev = np.array([[90]])  # 90 metrekarelik yeni bir ev
tahmin = model.predict(yeni_ev)

print(f"90 metrekarelik evin tahmini fiyatı: {tahmin[0]} Bin TL")

```
>Hazırlanan bu küçük program girdi (Feature) olarak daha önce satılmış evlerin metrekare büyüklüklerini almaktadır. Model, bu evlerin gerçek satış fiyatlarını (Label) inceleyerek metrekare ile fiyat arasındaki doğru orantıyı keşfeder. Eğitim bittikten sonra modelden, geçmişte hiç görmediği 90 metrekarelik yepyeni bir evin değerini tahmin etmesi istenir. Model arka planda öğrendiği matematiksel kuralı çalıştırarak bu eve karşılık gelen tahmini piyasa değerini hesaplar. Programın nihai çıktısı ise ekrana yazdırılan "90 metrekarelik evin tahmini fiyatı: 900.0 Bin TL" şeklindeki sayısal tahmindir.



[1][Yapay Zeka Nedir?](https://tr.wikipedia.org/wiki/Yapay_zek%C3%A2)

[2][Yapay Zeka(YZ) Nedir?](https://www-ibm-com.translate.goog/think/topics/artificial-intelligence?_x_tr_sl=en&_x_tr_tl=tr&_x_tr_hl=tr&_x_tr_pto=sge)

[3][Makine ogrenimi nedir ve nasil calisir?](https://azure.microsoft.com/tr-tr/resources/cloud-computing-dictionary/what-is-machine-learning-platform)

[4][Makine Öğrenimi Nedir?](https://www.oracle.com/tr/artificial-intelligence/machine-learning/what-is-machine-learning/)

[5][Derin öğrenme nedir?](https://azure.microsoft.com/tr-tr/resources/cloud-computing-dictionary/what-is-deep-learning)

[6][Yapay zekada derin öğrenme nedir?](https://aws.amazon.com/tr/what-is/deep-learning/)

[7][LLM'ler: Büyük dil modeli nedir?](https://developers.google.com/machine-learning/crash-course/llm/transformers?hl=tr)

[8][LLM Nedir?](https://www.patika.dev/blog/llm-nedir-yapay-zeka-mucizesi-llmler-hakkinda-sik-sorulan-7-soru)

