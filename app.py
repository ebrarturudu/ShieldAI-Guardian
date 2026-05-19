import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from google import genai
from PIL import Image
import agent_logic

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def tam_analiz_baslat(gorsel_yolu):
    try:
        img = Image.open(gorsel_yolu)
    except FileNotFoundError:
        return "Hata: Görsel dosyası bulunamadı."

    try:
        gözcü_cevabı = client.models.generate_content(
            model="gemini-flash-latest",
            contents=["""Bu bir e-ticaret sitesi veya ilan görseli. 
            Görseldeki tüm metinleri, logoları, fiyatları ve tasarım hatalarını ham veri olarak listele.""", img]
        )
        ham_veri = gözcü_cevabı.text
    except Exception as e:
        return "⚠️ Şu anda Google sunucuları aşırı yoğun olduğu için Gözcü Ajan yanıt veremedi. Lütfen birkaç saniye sonra tekrar deneyin."

    nihai_rapor = agent_logic.guvenlik_karari_ver(ham_veri)
    return nihai_rapor

@app.route("/", methods=["GET", "POST"])
def index():
    rapor = None
    gorsel_url = None
    
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
            
        if file:
         
            dosya_yolu = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(dosya_yolu)
            
            gorsel_url = url_for('static', filename=f'uploads/{file.filename}')
            
            rapor = tam_analiz_baslat(dosya_yolu)
            
    return render_template("index.html", rapor=rapor, gorsel=gorsel_url)

if __name__ == "__main__":
    
    app.run(debug=True)