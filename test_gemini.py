import os
from dotenv import load_dotenv
from google import genai
from PIL import Image # Resimleri açmak için lazım

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# 1. Resmi bilgisayardan oku
img = Image.open(r"C:/Users/ebrar/OneDrive/Desktop/ShieldAI-Guardian/test_image.png")

# 2. Gemini'ye hem yazı hem resim gönder
response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=["Bu bir e-ticaret sitesi ekran görüntüsü mü? Eğer öyleyse, güvenli görünüyor mu? Kısaca analiz et.", img]
)

print("--- ShieldAI İlk Analiz Sonucu ---")
print(response.text)