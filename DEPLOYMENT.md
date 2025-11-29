# Railway Deployment Guide - ResignPrediction

## 📋 Prerequisites

- Docker installed locally
- Docker Hub account (for pushing images)
- Railway account (https://railway.app)
- Git configured

---

## 🚀 Step 1: Build Docker Images Locally

### Build Backend Image
```bash
cd backend
docker build -t widy4aa/resignprediction-backend:latest .
```

### Build Frontend Image
```bash
cd ../frontend
docker build -t widy4aa/resignprediction-frontend:latest .
```

### Verify Images
```bash
docker images | grep resignprediction
```

---

## 📤 Step 2: Push Images to Docker Hub

### Login to Docker Hub
```bash
docker login
# Enter your Docker Hub credentials
```

### Push Backend Image
```bash
docker push widy4aa/resignprediction-backend:latest
```

### Push Frontend Image
```bash
docker push widy4aa/resignprediction-frontend:latest
```

### Verify on Docker Hub
Visit: https://hub.docker.com/r/widy4aa/

---

## 🚆 Step 3: Deploy to Railway

### A. Create Railway Account
1. Go to https://railway.app
2. Sign up with GitHub account
3. Create new project

### B. Deploy Backend
1. In Railway dashboard, click "New Service"
2. Select "Docker Image"
3. Enter image: `widy4aa/resignprediction-backend:latest`
4. Add environment variables:
   - `FLASK_APP` = `app_mvc.py`
   - `FLASK_ENV` = `production`
   - `DEBUG` = `False`
5. Port: `5000`
6. Deploy

### C. Deploy Frontend
1. Click "New Service" again
2. Select "Docker Image"
3. Enter image: `widy4aa/resignprediction-frontend:latest`
4. Add environment variable:
   - `VITE_API_URL` = `http://your-backend-railway-url:5000`
5. Port: `80`
6. Deploy

### D. Configure Backend URL
1. Get backend service URL from Railway
2. Update frontend environment variable `VITE_API_URL` with backend URL
3. Redeploy frontend

---

## 🧪 Step 4: Test Deployment

### Test Backend Health
```bash
curl https://your-backend-url.railway.app/health
```

### Test Frontend
Open in browser: `https://your-frontend-url.railway.app`

### Test Prediction
```bash
curl -X POST https://your-backend-url.railway.app/predict \
  -H "Content-Type: application/json" \
  -d '{
    "OverTime": "No",
    "MonthlyIncome": 5000,
    "Age": 35,
    "TotalWorkingYears": 10,
    "DistanceFromHome": 5,
    "StockOptionLevel": 1,
    "EnvironmentSatisfaction": 3
  }'
```

---

## 📝 Docker Compose Local Testing

### Build and run locally
```bash
docker-compose up --build
```

### Access locally
- Frontend: http://localhost:80
- Backend: http://localhost:5000
- Backend Health: http://localhost:5000/health

### Stop containers
```bash
docker-compose down
```

---

## 🔧 Troubleshooting

### Image build fails
```bash
# Clear Docker cache
docker system prune -a

# Rebuild
docker build -t widy4aa/resignprediction-backend:latest ./backend
```

### Push fails
```bash
# Check Docker Hub credentials
docker login

# Verify image exists
docker images | grep resignprediction
```

### Railway deployment fails
1. Check logs in Railway dashboard
2. Verify environment variables
3. Check port configuration
4. Ensure image is public on Docker Hub

### CORS issues on Railway
Update frontend environment variable with correct backend URL

---

## 📊 Directory Structure After Setup

```
ResignPrediction/
├── backend/
│   ├── Dockerfile          # ← Backend image definition
│   ├── app_mvc.py
│   ├── config.py
│   ├── controllers.py
│   ├── models.py
│   ├── routes.py
│   ├── views.py
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── Dockerfile          # ← Frontend image definition
│   ├── package.json
│   ├── src/
│   ├── public/
│   └── README.md
├── model/
│   ├── attrition_pipeline_minimal.pkl
│   ├── hasil.json
│   ├── img/
│   └── README.md
├── docker-compose.yml       # ← Local orchestration
├── DEPLOYMENT.md            # ← This file
└── README.md
```

---

## 🎯 Quick Reference

| Task | Command |
|------|---------|
| Build images | `docker build -t widy4aa/resignprediction-backend:latest ./backend` |
| Build frontend | `docker build -t widy4aa/resignprediction-frontend:latest ./frontend` |
| Push backend | `docker push widy4aa/resignprediction-backend:latest` |
| Push frontend | `docker push widy4aa/resignprediction-frontend:latest` |
| Run locally | `docker-compose up --build` |
| Stop locally | `docker-compose down` |
| View logs | `docker logs <container-id>` |

---

## 📚 Useful Links

- **Railway Dashboard:** https://railway.app/dashboard
- **Docker Hub:** https://hub.docker.com
- **Docker Docs:** https://docs.docker.com
- **Railway Docs:** https://docs.railway.app
- **GitHub Repository:** https://github.com/widy4aa/ResignPrediction

---

**Last Updated:** November 29, 2025
