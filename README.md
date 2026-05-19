# 🛡️ ShieldAI: E-Commerce & Finance Guard

ShieldAI, e-ticaret ve finans sektörlerindeki dijital varlıkları, gelişmiş yapay zeka ajanları kullanarak oltalama (phishing), manipülatif tasarımlar (dark patterns) ve sahte fatura/dekont dolandırıcılıklarına karşı koruyan **kurumsal düzeyde bir güvenlik asistanı prototipidir.**

Sistem, çok katmanlı akıl yürütme mimarisi ve API kotaları/kesintileri altında bile sistemi ayakta tutan hata toleranslı (fault-tolerant) çevrimdışı analiz altyapısı ile donatılmıştır.

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

2. Ortam Değişkenlerinin Yapılandırılması
Projenin kök dizininde bulunan .env.example dosyasının adını .env olarak değiştirin ve içerisine kendi Gemini API anahtarınızı tanımlayın:

Plaintext
GOOGLE_API_KEY=BURAYA_GEMINI_API_KEYINIZI_YAZIN
(Güvenlik protokolleri gereği orijinal .env dosyası repoya dahil edilmemiştir).

3. Toplu Test Sürecinin Başlatılması (Automated Test Suite)
Sistemin sektörel senaryolar üzerindeki doğruluğunu ve başarı yüzdesini (Accuracy) incelemek için test suite scriptini çalıştırabilirsiniz:

Bash
python test_runner.py
4. Web Dashboard Arayüzünün Başlatılması
Kullanıcı dostu siber güvenlik panelini tarayıcınızda görüntülemek için Flask uygulamasını başlatın:

Bash
python app.py
Uygulama başlatıldıktan sonra tarayıcınızdan http://127.0.0.1:5000 adresine giderek arayüze erişebilirsiniz.