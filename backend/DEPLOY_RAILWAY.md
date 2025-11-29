# 🚀 Deploy Backend ke Railway

## Prerequisites
- Akun Railway (https://railway.app)
- Git repository sudah di-push ke GitHub

---

## 📋 Step-by-Step Deployment

### 1. Login ke Railway
1. Buka https://railway.app
2. Login dengan GitHub

### 2. Buat New Project
1. Klik **"New Project"**
2. Pilih **"Deploy from GitHub repo"**
3. Pilih repository **ResignPrediction**

### 3. Configure Root Directory
Karena backend ada di subfolder:
1. Klik pada service yang dibuat
2. Buka tab **Settings**
3. Scroll ke **Root Directory**
4. Isi dengan: `backend`
5. Klik **Apply**

### 4. Set Environment Variables
Buka tab **Variables** dan tambahkan:

```env
# Wajib
FLASK_DEBUG=false
CORS_ORIGINS=*

# Path untuk model (sudah ada di public folder)
MODEL_PATH=./public/attrition_pipeline_minimal.pkl
RESULTS_PATH=./public/hasil.json
IMG_BASE_PATH=./public/img
```

> **Note:** Railway otomatis set `PORT`, jadi tidak perlu set manual.

### 5. Deploy
1. Railway akan auto-detect Python project
2. Tunggu build selesai (2-5 menit)
3. Setelah selesai, Railway akan generate URL seperti:
   `https://resignprediction-production.up.railway.app`

### 6. Test API
Buka browser dan akses:
```
https://YOUR-RAILWAY-URL/api/health
```

Harusnya response:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_type": "Random Forest"
}
```

---

## 🔧 Troubleshooting

### Build Failed
1. Cek **Build Logs** di Railway Dashboard
2. Pastikan `requirements.txt` ada di folder `backend/`
3. Pastikan Python version compatible

### Model Not Found
1. Pastikan folder `backend/public/` ada dan berisi:
   - `attrition_pipeline_minimal.pkl`
   - `hasil.json`
   - `img/` folder dengan visualizations

2. Cek environment variables sudah benar:
   ```
   MODEL_PATH=./public/attrition_pipeline_minimal.pkl
   ```

### CORS Error
1. Set `CORS_ORIGINS` ke URL frontend kamu:
   ```
   CORS_ORIGINS=https://your-frontend.up.railway.app
   ```
   
2. Atau gunakan `*` untuk allow semua (development only)

### Port Error
Railway otomatis set `PORT` environment variable. Jangan hardcode port di code.

---

## 📁 File Structure untuk Deployment

```
backend/
├── app_mvc.py          # Main Flask app
├── config.py           # Configuration
├── models.py           # Data models
├── routes.py           # API routes
├── gunicorn.conf.py    # Gunicorn config ✨
├── Procfile            # Start command ✨
├── railway.toml        # Railway config ✨
├── requirements.txt    # Dependencies
├── .env.example        # Environment template
└── public/             # Static files
    ├── attrition_pipeline_minimal.pkl
    ├── hasil.json
    └── img/
        ├── full/
        ├── reduced/
        ├── minimal/
        └── comparison/
```

---

## 🔄 Update Deployment

Setiap kali push ke `main` branch, Railway akan auto-deploy:

```bash
git add .
git commit -m "Update backend"
git push origin main
```

---

## 💡 Tips

1. **Custom Domain**: Di Settings > Domains, bisa tambah custom domain
2. **Scaling**: Railway auto-scale, tapi bisa set di Settings
3. **Logs**: Realtime logs tersedia di tab Deployments
4. **Monitoring**: Railway punya built-in metrics

---

## 📱 Setelah Backend Live

Update frontend `.env` dengan URL backend Railway:

```env
VITE_API_URL=https://your-backend.up.railway.app
```

Lalu rebuild dan deploy frontend.
