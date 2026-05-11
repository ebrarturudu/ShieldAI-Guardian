import os
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

SISTEM_TALIMATI = """
Sen ShieldAI siber güvenlik uzmanısın. Analizlerini bir rapor formatında sunmalısın.
Lütfen şu yapıyı kullan:

# 🛡️ ShieldAI Güvenlik Analiz Raporu

## 📊 Genel Risk Özeti
**Risk Skoru:** [0-100 arası bir sayı] / 100
**Durum:** [Güvenli / Şüpheli / Tehlikeli]

## 🔍 Tespit Edilen Bulgular
| Kategori | Açıklama | Şüphe Düzeyi |
| :--- | :--- | :--- |
| Dark Pattern | [Bulunan teknik] | [Düşük/Orta/Yüksek] |
| DeepTrust | [Görsel/Satıcı analizi] | [Düşük/Orta/Yüksek] |

## 💡 Kullanıcıya Öneriler
- [Yapılması gereken ilk adım]
- [Dikkat edilmesi gereken detay]
"""

def analiz_et(gorsel_yolu):
    img = Image.open(gorsel_yolu)
    
    response = client.models.generate_content(
        model="gemini-flash-latest",
        config={'system_instruction': SISTEM_TALIMATI},
        contents=["Bu sayfayı analiz et.", img]
    )
    return response.text


if __name__ == "__main__":
    print("Analiz yapılıyor...")
    print(analiz_et("sahte_image.jpg"))

    def shield_ai_karar_merkezi(gorsel_yolu):
        print(f"\n--- {gorsel_yolu} İçin İşlem Başlatıldı ---")
        
        
        rapor = analiz_et(gorsel_yolu)
        
        
        try:
            skor_satiri = [s for s in rapor.split('\n') if "Risk Skoru" in s][0]
            skor = int(''.join(filter(str.isdigit, skor_satiri.split('/')[0])))
        except:
            skor = 0 
        print(f"Sistem Kararı: Risk Puanı {skor}")
        
        if skor >= 80:
            print("🚨 ACİL DURUM: Bu site kesinlikle dolandırıcı! Kullanıcı engelleniyor.")
        elif skor >= 40:
            print("⚠️ UYARI: Şüpheli durumlar var. Kullanıcıya dikkatli olması söyleniyor.")
        else:
            print("✅ GÜVENLİ: Belirgin bir tehdit bulunamadı.")
            
        return rapor

