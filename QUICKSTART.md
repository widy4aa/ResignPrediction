# 🚀 QUICK START - Deploy ke Railway

## 📋 Yang Sudah Disiapkan

✅ `backend/Dockerfile` - Flask API container  
✅ `frontend/Dockerfile` - Vue 3 + Nginx container  
✅ `docker-compose.yml` - Local orchestration  
✅ `DEPLOYMENT.md` - Detailed guide  

---

## 🎯 Langkah Cepat (5 Menit)

### 1. Setup Docker Hub
```bash
# Login ke Docker
docker login

# Jika belum punya account: https://hub.docker.com
```

### 2. Build Backend
```bash
cd backend
docker build -t YOUR_USERNAME/resignprediction-backend:latest .
docker push YOUR_USERNAME/resignprediction-backend:latest
```

### 3. Build Frontend  
```bash
cd ../frontend
docker build -t YOUR_USERNAME/resignprediction-frontend:latest .
docker push YOUR_USERNAME/resignprediction-frontend:latest
```

### 4. Deploy ke Railway
1. Buka https://railway.app/dashboard
2. Click "New Project"
3. Select "Docker Image"
4. Masukkan: `YOUR_USERNAME/resignprediction-backend:latest`
5. Set Port: `5000`
6. Add Env Vars:
   - `FLASK_APP=app_mvc.py`
   - `FLASK_ENV=production`
   - `DEBUG=False`
7. Deploy

8. Repeat untuk Frontend dengan:
   - Image: `YOUR_USERNAME/resignprediction-frontend:latest`
   - Port: `80`
   - Env: `VITE_API_URL=http://BACKEND_URL:5000`

### 5. Test
- Backend: `https://your-backend-url/health`
- Frontend: `https://your-frontend-url`

---

## 🧪 Test Lokal (Optional)

```bash
docker-compose up --build

# Akses:
# Frontend: http://localhost:80
# Backend: http://localhost:5000
# Health: http://localhost:5000/health
```

---

## 📚 Dokumen Lengkap

Lihat `DEPLOYMENT.md` untuk panduan step-by-step yang detail.

---

## ⚠️ Important

- Replace `YOUR_USERNAME` dengan Docker Hub username Anda
- Jangan lupa set backend URL di frontend env var
- Railway akan auto-generate domain untuk setiap service

Happy Deploying! 🎉
