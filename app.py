# modul utama dari aplikasi
import os
from flask import redirect
import config

app = config.connex_app

# membaca swagger.yml untuk konfigurasi endpoint
app.add_api("swagger.yml")

# membuat route URL untuk aplikasi "/"
@app.route("/")
def home():
    return redirect("/api/ui")


# jika kita menggunakan mode stanc alone, aplikasi akan dijalankan
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", default="5000")))


