# 🚀 ResignPrediction - Employee Attrition Prediction System

Sistem prediksi attrition karyawan menggunakan **Machine Learning** (Random Forest) dengan **7 features optimal** yang menghasilkan accuracy **84.01%** - lebih tinggi dari model full (82.99%).

## 📊 Project Overview

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Employee Attrition Prediction System                       │
│  ────────────────────────────────────────────────────────  │
│                                                             │
│  Backend (Flask MVC)          Frontend (Vue 3 + Vite)      │
│  ├─ 8 API Endpoints           ├─ Landing Page             │
│  ├─ Model Serving             ├─ Predict Page             │
│  └─ Visualization Server      └─ Insight Page             │
│                                                             │
│  Model (Random Forest)                                     │
│  ├─ 7 Features (Ultra-Minimal)                            │
│  ├─ 300 Decision Trees                                     │
│  └─ 84.01% Accuracy                                        │
│                                                             │
│  Dataset (IBM HR Analytics)                                │
│  ├─ 1,470 Samples                                         │
│  └─ 35 Original Features                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 🎯 Key Metrics

| Metric | Value |
|--------|-------|
| **Model Type** | Random Forest |
| **Features** | 7 (77% reduction from 35) |
| **Accuracy** | 84.01% ✅ |
| **Training Accuracy** | 89.29% |
| **Dataset Size** | 1,470 samples |
| **Framework Backend** | Flask 3.0.0 |
| **Framework Frontend** | Vue.js 3 + Vite |
| **UI Framework** | Tailwind CSS |

## 📁 Folder Structure

```
ResignPrediction/
│
├── backend/                        🔧 API Server (Flask MVC)
│   ├── app_mvc.py                 # Entry point
│   ├── config.py                  # Configuration
│   ├── models.py                  # Model layer (data access)
│   ├── controllers.py             # Controller layer (business logic)
│   ├── views.py                   # View layer (response formatting)
│   ├── routes.py                  # Route definitions
│   ├── requirements.txt           # Python dependencies
│   └── README.md                  # Backend documentation
│
├── frontend/                       🎨 Web Application (Vue 3)
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Landing.vue       # Home page
│   │   │   ├── Predict.vue       # Prediction form
│   │   │   └── Insight.vue       # Model analysis
│   │   ├── components/           # Reusable UI components
│   │   ├── lib/                  # Utility functions
│   │   ├── App.vue               # Root component
│   │   ├── main.js               # Entry point
│   │   └── style.css             # Global styles
│   ├── public/
│   │   ├── WA_Fn-UseC_-HR-Employee-Attrition.csv  # Dataset
│   │   └── sample_prediction.csv # CSV template
│   ├── package.json              # Dependencies
│   ├── vite.config.js            # Vite configuration
│   ├── tailwind.config.js        # Tailwind config
│   └── README.md                 # Frontend documentation
│
├── model/                          🤖 Machine Learning
│   ├── generate_graphs.py         # Visualization script
│   ├── feature_importance_minimal.csv  # Feature ranking
│   ├── minimal_features.txt       # Features list
│   ├── WA_Fn-UseC_-HR-Employee-Attrition.csv  # Dataset
│   ├── attrition_pipeline_minimal.pkl  # Trained model
│   ├── hasil.json                 # Training results
│   ├── img/                       # 19 visualization graphs
│   │   ├── full/                 # Full model graphs
│   │   ├── reduced/              # Reduced model graphs
│   │   ├── minimal/              # Minimal model graphs
│   │   └── comparison/           # Comparison graphs
│   └── README.md                 # Model documentation
│
└── README.md                       📖 This file
```

## 🏃 Quick Start

### 1️⃣ Prerequisites
- Python 3.8+
- Node.js 16+
- pip & npm
- Git

### 2️⃣ Clone Repository
```bash
git clone https://github.com/widy4aa/ResignPrediction.git
cd ResignPrediction
```

### 3️⃣ Backend Setup
```bash
cd backend

# Create .env file (or copy from .env.example)
cp .env.example .env

# Install dependencies
pip install -r requirements.txt

# Run server
python app_mvc.py
```
✅ Server running di `http://localhost:5000`

### 4️⃣ Frontend Setup
```bash
cd frontend

# Create .env file (or copy from .env.example)
cp .env.example .env

# Install dependencies
npm install

# Run dev server
npm run dev
```
✅ App running di `http://localhost:5173`

### 5️⃣ Access Application
- **Home:** `http://localhost:5173/`
- **Predict:** `http://localhost:5173/predict`
- **Insight:** `http://localhost:5173/insight`

---

## 📚 Documentation

### Backend Documentation
📖 **File:** `backend/README.md`

Dokumentasi lengkap untuk:
- Arsitektur MVC
- 8 API endpoints lengkap
- Model handling
- Error handling
- Setup & testing

**Key Endpoints:**
- `GET /health` - Health check
- `GET /features` - Required features
- `POST /predict` - Single prediction
- `GET /api/results` - Model training results
- `GET /api/visualizations/list` - List visualizations
- `GET /api/visualizations/<category>/<file>` - Serve images

---

### Frontend Documentation
📖 **File:** `frontend/README.md`

Dokumentasi lengkap untuk:
- Vue 3 architecture
- 3 pages (Landing, Predict, Insight)
- Components & utilities
- Styling (Tailwind CSS)
- API integration
- CSV batch prediction

**Pages:**
- **Landing:** Home page dengan dynamic stats
- **Predict:** Manual input + CSV batch prediction
- **Insight:** Dataset explorer + model analysis

---

### Model Documentation
📖 **File:** `model/README.md`

Dokumentasi lengkap untuk:
- Dataset information
- Model training process
- 7 optimal features
- 19 visualizations
- Feature importance
- Model comparison

**Key Insights:**
- Ultra-minimal: 7 features (77% reduction)
- Better accuracy: 84.01% vs 82.99% (full model)
- Faster prediction: ~20ms/sample
- Well-balanced: No overfitting detected

---

## 🎯 7 Required Features for Prediction

| # | Feature | Category | Importance | Type |
|---|---------|----------|------------|------|
| 1 | **OverTime** | Work-Life | 10.99% | Categorical |
| 2 | **MonthlyIncome** | Compensation | 23.65% | Numeric |
| 3 | **Age** | Experience | 17.78% | Numeric |
| 4 | **TotalWorkingYears** | Experience | 18.30% | Numeric |
| 5 | **DistanceFromHome** | Work-Life | 13.29% | Numeric |
| 6 | **StockOptionLevel** | Compensation | 7.71% | Numeric |
| 7 | **EnvironmentSatisfaction** | Satisfaction | 8.27% | Numeric |

---

## 🛠️ Architecture

### System Architecture
```
User Browser
    ↓
Frontend (Vue 3 + Vite)
    ↓ HTTP/REST
Backend API (Flask MVC)
    ├─ Controllers (Business Logic)
    ├─ Models (ML Model + Data)
    └─ Views (Response Formatting)
    ↓
ML Model (Random Forest)
```

### MVC Flow
```
HTTP Request
    ↓
routes.py
    ↓
controllers.py
    ↓
models.py
    ↓
HTTP Response (JSON)
```

---

## 📊 Visualizations (19 Graphs)

Available in the Insight page with full explanations:

### Full Model (3 graphs)
- Preprocessing pipeline flow
- Confusion matrix
- Feature importance ranking

### Reduced Model (3 graphs)
- Preprocessing pipeline flow
- Confusion matrix
- Feature importance ranking

### Minimal Model (3 graphs)
- Preprocessing pipeline flow
- Confusion matrix
- Feature importance ranking

### Comparison (5+ graphs)
- Accuracy comparison
- Feature efficiency
- Performance metrics
- Training efficiency
- Model comparison dashboard

---

## 🔄 Features Overview

### Landing Page ✨
- ✅ Dynamic statistics from API
- ✅ Model accuracy display (84.01%)
- ✅ Dataset information (1,470 samples)
- ✅ Feature highlights (7 key features)
- ✅ Call-to-action buttons
- ✅ Responsive mobile design

### Predict Page 🔮
**Manual Prediction Mode:**
- ✅ Form dengan 7 input fields
- ✅ Real-time input validation
- ✅ Instant prediction response
- ✅ Confidence score display
- ✅ Result interpretation

**CSV Batch Mode:**
- ✅ File upload dengan drag & drop
- ✅ CSV parsing & validation
- ✅ Batch prediction (100+ rows)
- ✅ Download results as CSV
- ✅ Data preview before prediction

### Insight Page 📈
- ✅ Dataset preview (1,470 rows × 35 columns)
- ✅ Advanced pagination
- ✅ Model analysis dashboard
- ✅ Feature comparison tools
- ✅ 19 visualization graphs with explanations
- ✅ Model performance comparison
- ✅ Key insights & recommendations

---

## 📡 API Endpoints Complete List

### Health & Features
```
GET /health
GET /features
```

### Predictions
```
POST /predict
```
**Request Body:** 7 features (JSON)
**Response:** Prediction + confidence score

### Model Results
```
GET /api/results
GET /api/results/summary
GET /api/results/model/<type>
```

### Visualizations
```
GET /api/visualizations/list
GET /api/visualizations/<category>/<filename>
```

---

## 🧪 Testing

### Backend Health Check
```bash
curl http://localhost:5000/health
```

### Get Required Features
```bash
curl http://localhost:5000/features
```

### Prediction Test
```bash
curl -X POST http://localhost:5000/predict \
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

### Frontend Manual Tests
- ✅ Landing page loads with dynamic data
- ✅ Predict form validation works correctly
- ✅ CSV upload & parsing functionality
- ✅ Batch prediction processing
- ✅ Insight page displays all data
- ✅ Pagination controls work properly
- ✅ Graph modal popups display correctly
- ✅ Responsive on mobile/tablet/desktop

---

## 🚀 Deployment Guide

### Railway Deployment (Recommended)

**Backend:**
1. Login ke [Railway](https://railway.app)
2. New Project → Deploy from GitHub → Pilih `ResignPrediction`
3. Settings → Root Directory → `backend`
4. Variables → Set environment variables:
   ```
   FLASK_DEBUG=false
   CORS_ORIGINS=*
   MODEL_PATH=./public/attrition_pipeline_minimal.pkl
   RESULTS_PATH=./public/hasil.json
   IMG_BASE_PATH=./public/img
   ```
5. Deploy selesai! Dapatkan URL backend

**Frontend:**
1. Update `.env` dengan URL backend Railway:
   ```
   VITE_API_URL=https://your-backend.up.railway.app
   ```
2. Build: `npm run build`
3. Deploy `dist/` folder ke hosting (Vercel/Netlify/Railway)

📖 **Panduan lengkap:** `backend/DEPLOY_RAILWAY.md`

### Production Build
```bash
# Frontend
cd frontend
npm run build
# Output: dist/ folder (ready for serving)

# Backend
cd backend
python app_mvc.py
# Set FLASK_DEBUG=false in .env for production
```

### Environment Variables

**Backend (.env in backend/ folder):**
```env
FLASK_DEBUG=false
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
CORS_ORIGINS=*
MODEL_PATH=./public/attrition_pipeline_minimal.pkl
RESULTS_PATH=./public/hasil.json
IMG_BASE_PATH=./public/img
```

**Frontend (.env in frontend/ folder):**
```env
VITE_API_URL=http://localhost:5000
# For production: https://your-backend-url.com
```

---

## 🐛 Troubleshooting

### Backend Issues

**Issue: Backend won't start**
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install -r requirements.txt

# Check if model files exist
ls public/attrition_pipeline_minimal.pkl
ls public/hasil.json
```

**Issue: Model not found**
```bash
# Verify paths in .env
cat .env  # Check MODEL_PATH and RESULTS_PATH

# Copy model files if missing
cp ../model/attrition_pipeline_minimal.pkl public/
cp ../model/hasil.json public/
cp -r ../model/img public/
```

**Issue: CORS errors**
```bash
# Update CORS_ORIGINS in .env
# For development: CORS_ORIGINS=*
# For production: CORS_ORIGINS=https://your-frontend-url.com
```

### Frontend Issues

**Issue: API calls fail**
```bash
# Check .env file exists
cat .env

# Verify VITE_API_URL
# Should match backend URL (e.g., http://localhost:5000)

# Restart dev server after changing .env
npm run dev
```

**Issue: Build fails**
```bash
# Clear node_modules and reinstall
rm -rf node_modules
npm install

# Clear cache and rebuild
npm run build
```

**Issue: Images not loading in Insight page**
- Ensure backend is running
- Check browser console for CORS errors
- Verify API_URL in `src/config/api.js`

### Model Training Issues

**Issue: Want to retrain model**
```bash
cd model
python model.py  # Trains all 3 models
python generate_graphs.py  # Generates visualizations
```

---

## 📖 Additional Resources

- **Backend API Docs:** `backend/README.md`
- **Frontend Guide:** `frontend/README.md`
- **Model Details:** `model/README.md`
- **Deployment Guide:** `backend/DEPLOY_RAILWAY.md`
- **Jupyter Notebook:** `model/attrition_models.ipynb`

---

## 👨‍💻 Tech Stack

**Backend:**
- Flask 3.0.0 (Python web framework)
- Scikit-learn 1.6.1 (ML library)
- Pandas 2.2.0+ (Data processing)
- Flask-CORS 4.0.0 (CORS handling)
- Gunicorn 21.2.0 (WSGI server)
- Python-dotenv 1.0.0 (Environment variables)

**Frontend:**
- Vue.js 3 (Progressive framework)
- Vite (Build tool)
- Tailwind CSS (Utility-first CSS)
- Axios (HTTP client)
- Vue Router (Routing)

**ML Model:**
- Random Forest Classifier
- Scikit-learn Pipeline
- One-Hot Encoding
- 300 estimators, max_depth=15

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

**widy4aa**
- GitHub: [@widy4aa](https://github.com/widy4aa)
- Repository: [ResignPrediction](https://github.com/widy4aa/ResignPrediction)

---

## 🙏 Acknowledgments

- IBM HR Analytics Dataset
- Scikit-learn Documentation
- Vue.js Community
- Flask Documentation

---

**⭐ If you find this project useful, please give it a star!**
python --version  # Should be 3.8+

# Verify dependencies
pip list | grep Flask

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

**Issue: Model file not found**
```bash
# Check model path in config.py
# Verify: model/attrition_pipeline_minimal.pkl exists
# Verify: model/hasil.json exists
```

**Issue: CORS errors**
```bash
# Already enabled in app_mvc.py
# Check CORS_ORIGINS in config.py
```

### Frontend Issues

**Issue: npm dependencies error**
```bash
# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

**Issue: API connection error**
```bash
# Verify backend is running
curl http://localhost:5000/health

# Check CORS headers
# Check frontend proxy in vite.config.js
```

**Issue: CSV prediction fails**
```
✓ Verify CSV has 7 columns
✓ Check column names match exactly (case-sensitive)
✓ Ensure data types are correct
✓ Use sample_prediction.csv as template
```

---

## 📈 Performance Metrics

| Metric | Value |
|--------|-------|
| **Model Accuracy** | 84.01% |
| **Model Precision** | 86% |
| **Model Recall** | 96% |
| **F1-Score** | 91% |
| **Training Time** | ~2-3 seconds |
| **Single Prediction** | ~20ms |
| **Batch Prediction (100 rows)** | ~2-3 seconds |
| **Dataset Size** | 1,470 employees |

---

## 📋 Checklist Features

### What's Included ✅
- ✅ Production-ready code (MVC architecture)
- ✅ Comprehensive documentation (3 README files)
- ✅ Clean, modular codebase
- ✅ Responsive UI design
- ✅ Comprehensive error handling
- ✅ API input validation
- ✅ 19 visualization graphs
- ✅ Dataset explorer with pagination
- ✅ CSV batch processing
- ✅ Health check monitoring

### Best Practices Applied ✅
- ✅ Separation of concerns (MVC pattern)
- ✅ RESTful API design
- ✅ Reactive state management (Vue 3 Composition API)
- ✅ CORS enabled for development
- ✅ Input validation & sanitization
- ✅ Error handling & logging
- ✅ Modular, reusable components
- ✅ Mobile-responsive design
- ✅ Performance optimized
- ✅ Security best practices

---

## 🔗 Useful Links

- **GitHub Repository:** https://github.com/widy4aa/ResignPrediction
- **Dataset Source:** IBM HR Analytics (Kaggle)
- **Backend Docs:** See `backend/README.md`
- **Frontend Docs:** See `frontend/README.md`
- **Model Docs:** See `model/README.md`

---

## 👤 Author

**Created:** November 2025  
**Version:** 1.0.0  
**Status:** ✅ Production Ready

---

## 📄 License

This project is provided for educational and learning purposes.

---

## 💬 Support & Questions

For issues, questions, or feedback:

1. **Check Documentation:**
   - `backend/README.md` - API & backend setup
   - `frontend/README.md` - UI & frontend setup
   - `model/README.md` - ML model details

2. **Review Troubleshooting Section** above

3. **Check Console Logs:**
   - Backend: Terminal output
   - Frontend: Browser Developer Tools (F12)

4. **GitHub Issues:** Create an issue on the GitHub repository

---

**Last Updated:** November 29, 2025  
**Repository:** https://github.com/widy4aa/ResignPrediction  
**Status:** Active & Maintained ✅
