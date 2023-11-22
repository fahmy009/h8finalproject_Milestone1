# modul utama dari aplikasi

from flask import render_template
import connexion

# membuat inisiasi instance aplikasi
app = connexion.App(__name__, specification_dir="./")

# membaca swagger.yml untuk konfigurasi endpoint
app.add_api("swagger.yml")


# membuat route URL untuk aplikasi "/"
@app.route("/")
def home():
    """
    Fungsi ini akan menjalankan aplikasi di lokal dengan URL

    localhost:5000

    dan akan di return hasilnya dengan menggunakan rendered template 'home.html'
    """

    return render_template("home.html")


# jika kita menggunakan mode stanc alone, aplikasi akan dijalankan
if __name__ == "__main__":
    app.run()
