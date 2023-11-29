# Milestone API

## Overview

Aplikasi ini adalah aplikasi milestone yang dibuat untuk menyelesaikan final project dari talent class batch 11 tentang backend developtment menggunakan Python dan dalam aplikasi ini terdapat CRUD (Create, Read, Update, dan Delete)

## Library yang digunakan 

- Flask
- Swagger
- SQLAlchemy
- MySQL (as an example database)

## Instalasi Aplikasi

### Persiapan

Sebelum Menjalankan aplikasi, dipastikan requierement di bawah telah terinstall:

- Python 3
- pip (Python package installer)
- MySQL (or any other database of your choice)

### Instalasi

1. **Clone Aplikasi dar github:**

    ```bash
    git clone https://github.com/fahmy009/h8finalproject_Milestone1.git
    cd h8finalproject_Milestone1
    ```

2. **Instalasi venv:**

    ```bash
    python3 -m venv venv
    ```

    actived venv

    ```bash
    source venv/bin/activate    // linux or mac os
    .\venv\Scripts\activate     // windows
    ```

    deadactived venv
    ```bash
    deactivate  
    ```

3. **Instalasi requirement yang wajib:**

    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the application:

python3 app.py

# Milestone API

## Overview

Setelah aplikasi berjalan, silahkan akses lama berikut ini: 

[http://localhost:5000/api/ui/](http://localhost:5000/api/ui/) 

## API Endpoints

### Ambil Semua Data Milestone

**Endpoint:**

- `GET /api/milestone`

**Deskripsi:**

Mengambil semua data milestone 

### Membuat data milestone

**Endpoint:**

- `POST /api/milestone`

**Deskripsi:**

Membuat data milestone

### Mengambil data milestone berdasarkan ID

**Endpoint:**

- `GET /api/milestone/{Id}`

**Deskripsi:**

Mengambil data Milestone berdasarkan ID

### Merubah data Milestone berdasarkan ID

**Endpoint:**

- `PUT /api/milestone/{Id}`

**Deskripsi:**

Merubah data milestone berdasarkan ID

### Menghapus data milestone berdasarkan ID

**Endpoint:**

- `DELETE /api/milestone/{Id}`

**Deskripsi:**

Menghapus data milestone berdasarkan ID

## Dokumentasi Swagger

Ekplorasi dokumentasi swagger yang bisa dilihat di laman berikut:

[http://localhost:5000/api/ui/](http://localhost:5000/api/ui/)

## Kontribusi

Kontribusi bersifat Gratis.. :-D [CONTRIBUTING.md](CONTRIBUTING.md).

## Lisensi

Project ini terlisensi oleh Muhammad Fahmy :-D