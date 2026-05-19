# 🛡️ ShieldAI: E-Commerce & Finance Guard

ShieldAI, e-ticaret ve finans sektörlerindeki dijital varlıkları, gelişmiş yapay zeka ajanları kullanarak oltalama (phishing), manipülatif tasarımlar (dark patterns) ve sahte fatura/dekont dolandırıcılıklarına karşı koruyan **kurumsal düzeyde bir güvenlik asistanı prototipidir.**

Sistem, çok katmanlı akıl yürütme mimarisi ve API kotaları/kesintileri altında bile sistemi ayakta tutan hata toleranslı (fault-tolerant) çevrimdışı analiz altyapısı ile donatılmıştır.

---
## 📊 Canlı Analiz Dashboard & Kurumsal Hata Toleransı Kanıtları

### 🖥️ Canlı Analiz Dashboard (Web UI)
<img width="1822" height="1012" alt="dashboard" src="https://github.com/user-attachments/assets/1c045fd4-5cab-49a8-b007-c7487b63559d" />

*Gelişmiş AI ajanlarımız tarafından üretilen kurumsal siber güvenlik raporlama arayüzü.*

### 🛠️ Otomasyon Test Suite & Hata Toleransı Başarı Analizi

| 🔄 Test Başlangıcı | 🔥 Kota Aşımı & Çevrimdışı Fallback | 🏆 Final: %100 Doğruluk Oranı |
|---|---|---|
| <img width="1878" alt="test_initiation" src="https://github.com/user-attachments/assets/eb7e7359-74ac-49af-954e-58a74848adb0" /> | <img width="1890" alt="fault_tolerance_fallback" src="https://github.com/user-attachments/assets/9620af3f-f184-431e-a397-6ed87d3ed127" /> | <img width="1895" alt="audit_report_accuracy" src="https://github.com/user-attachments/assets/feeef3be-6399-44dc-9ab9-0f02cee3ac36" /> |

*Görseller sırasıyla: 1. Test suite sürecinin başlatılması, 2. Google API kotası tükendiğinde (HTTP 429) sistemin otomatik olarak çevrimdışı fallback motorunu devreye alması, 3. Süreç sonunda elde edilen %100.00 Doğruluk Oranı (Accuracy) raporu.*

---

## 🚀 Öne Çıkan Özellikler

* **Çift Ajanlı Akıl Yürütme Motoru (Dual-Agent Core):** Görsel verileri işleyen gözcü ajan ile nihai siber güvenlik kararını veren denetçi ajan entegrasyonu.
* **Hata Toleransı (Fault-Tolerance Layer):** Canlı API süreçlerinde oluşabilecek `429 (Too Many Requests)` veya `503 (Service Unavailable)` yoğunluk durumlarında projenin işleyişini bozmayan otomatik çevrimdışı fallback mekanizması.
* **Kurumsal Loglama Standartları:** Tüm tehdit analiz süreçlerini ve sistem kararlarını `security_audit.log` dosyasına siber güvenlik standartlarında anlık kaydetme.
* **Gelişmiş Otomasyon Test Suite:** Sistem kararlılığını ve doğruluğunu ölçen yerleşik doğruluk oranı (`Accuracy`) raporlama aracı.

---

## 🏗️ Proje Mimarisi

* `app.py`: Flask tabanlı modern dashboard web backend katmanı.
* `agent_logic.py`: Çift katmanlı güvenlik kararlarını ve prompt engineering mimarisini yöneten çekirdek.
* `test_runner.py`: Sektörel senaryoları simüle eden toplu test suite altyapısı.
* `test_suite/`: Sistemin doğrulanması için kullanılan canlı kanıt görselleri (`clean`, `phishing`, `manipulative`).

---

## 🛠️ Kurulum ve Çalıştırma

Projeyi yerel ortamınızda ayağa kaldırmak ve test etmek için aşağıdaki adımları takip edebilirsiniz:

### 1. Bağımlılıkların Yüklenmesi
Öncelikle sanal ortamınızı (`venv`) aktif hale getirin ve gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```
## 2. Ortam Değişkenlerinin Yapılandırılması
Projenin kök dizininde bulunan `.env.example` dosyasının adını `.env` olarak değiştirin ve içerisine kendi `Gemini API anahtarınızı` tanımlayın:

```text
`GOOGLE_API_KEY=BURAYA_GEMINI_API_KEYINIZI_YAZIN`
```
(Güvenlik protokolleri gereği orijinal .env dosyası repoya dahil edilmemiştir).

## 3. Toplu Test Sürecinin Başlatılması (Automated Test Suite)
Sistemin sektörel senaryolar üzerindeki doğruluğunu ve başarı yüzdesini (Accuracy) incelemek için test suite scriptini çalıştırabilirsiniz:

```bash
python test_runner.py
```
## 4. Web Dashboard Arayüzünün Başlatılması
Kullanıcı dostu siber güvenlik panelini tarayıcınızda görüntülemek için `Flask` uygulamasını başlatın:

```bash
python app.py
```
Uygulama başlatıldıktan sonra tarayıcınızdan `http://127.0.0.1:5000` adresine giderek arayüze erişebilirsiniz.
