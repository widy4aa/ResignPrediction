# 🚀 Employee Attrition Prediction System

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
data-mining/
│
├── backend/                        🔧 API Server (Flask MVC)
│   ├── app_mvc.py                 # Entry point
│   ├── config.py                  # Configuration
│   ├── models.py                  # Model layer (data access)
│   ├── controllers.py             # Controller layer (business logic)
│   ├── views.py                   # View layer (response formatting)
│   ├── routes.py                  # Route definitions
│   ├── requirements.txt           # Python dependencies
│   ├── .env.example               # Environment template
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

### 2️⃣ Backend Setup
```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Run server
python app_mvc.py
```
✅ Server running di `http://localhost:5000`

### 3️⃣ Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Run dev server
npm run dev
```
✅ App running di `http://localhost:5173`

### 4️⃣ Access Application
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
- Faster prediction: ~20s vs 2 minutes
- Well-balanced: No overfitting detected

---

## 🎯 7 Required Features

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
Frontend (Vue 3)
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
Request
  ↓
routes.py
  ↓
controllers.py
  ↓
models.py
  ↓
Response
```

---

## 📊 Visualizations (19 Graphs)

### Full Model (3)
- Preprocessing flow
- Confusion matrix
- Feature importance

### Reduced Model (3)
- Preprocessing flow
- Confusion matrix
- Feature importance

### Minimal Model (3)
- Preprocessing flow
- Confusion matrix
- Feature importance

### Comparison (5)
- Accuracy comparison
- Feature efficiency
- Metrics overview
- Training time
- Summary dashboard

**Total: 14 visualization graphs** (dapat diakses di Insight page)

---

## 🔄 Features Overview

### Landing Page
- ✅ Dynamic statistics dari API
- ✅ Model accuracy (84.01%)
- ✅ Dataset info (1,470 samples)
- ✅ Call-to-action buttons
- ✅ Responsive design

### Predict Page
**Manual Mode:**
- ✅ Form dengan 7 input fields
- ✅ Real-time validation
- ✅ Instant prediction
- ✅ Confidence score display

**CSV Mode:**
- ✅ File upload
- ✅ CSV parsing & validation
- ✅ Batch prediction
- ✅ Download results
- ✅ Preview data

### Insight Page
- ✅ Dataset preview (1,470 rows × 35 columns)
- ✅ Pagination dengan controls
- ✅ Model analysis (3 versions)
- ✅ Feature comparison
- ✅ 14 visualization graphs
- ✅ Graph explanations
- ✅ Model comparison
- ✅ Insights & recommendations

---

## 📡 API Endpoints

### Health & Features
```bash
GET /health                    # Server status
GET /features                  # Required features list
```

### Predictions
```bash
POST /predict                  # Single prediction
```
**Input:** 7 features (JSON)
**Output:** Prediction + confidence

### Model Results
```bash
GET /api/results               # All models results
GET /api/results/summary       # Models summary
GET /api/results/model/<type>  # Specific model
```

### Visualizations
```bash
GET /api/visualizations/list                # List all graphs
GET /api/visualizations/<category>/<file>   # Serve image
```

---

## 🧪 Testing

### Backend Health Check
```bash
curl http://localhost:5000/health
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

### Frontend Tests
- ✅ Landing page loads correctly
- ✅ Predict form validation works
- ✅ CSV upload & parsing works
- ✅ Batch prediction succeeds
- ✅ Insight page displays all data
- ✅ Pagination works properly
- ✅ Graph modal popups work
- ✅ Responsive on mobile/tablet/desktop

---

## 🚀 Deployment

### Production Build
```bash
# Frontend
cd frontend
npm run build
# Output: dist/ folder

# Backend
cd backend
python app_mvc.py  # Production mode
```

### Environment Variables
Create `.env` files:

**Backend (.env):**
```
DEBUG=False
FLASK_ENV=production
PORT=5000
```

**Frontend (.env):**
```
VITE_API_URL=http://your-backend-url
```

---

## 🐛 Troubleshooting

### Issue: Backend won't start
```bash
# Check Python version
python --version  # Should be 3.8+

# Check dependencies
pip list | grep Flask

# Try reinstall
pip install -r requirements.txt --force-reinstall
```

### Issue: Frontend won't load
```bash
# Check Node version
node --version  # Should be 16+

# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules
npm install
```

### Issue: API connection error
```bash
# Check backend is running
curl http://localhost:5000/health

# Check frontend proxy config
# Edit: vite.config.js

# Check CORS settings
# Backend: Check app_mvc.py for CORS setup
```

### Issue: CSV prediction fails
```
- Verify CSV has 7 columns
- Check column names match (case-sensitive)
- Ensure data types are correct
- Sample: backend/example.csv
```

---

## 📈 Performance Metrics

| Metric | Value |
|--------|-------|
| **Model Accuracy** | 84.01% |
| **Precision** | 86% |
| **Recall** | 96% |
| **F1-Score** | 91% |
| **Training Time** | ~2-3 sec |
| **Prediction Time** | ~20ms/sample |
| **Batch Prediction (100 rows)** | ~2-3 sec |

---

## 📝 Notes

### What's Included
✅ Production-ready code  
✅ Comprehensive documentation  
✅ Clean MVC architecture  
✅ Responsive UI  
✅ Error handling  
✅ API validation  
✅ 19 visualization graphs  
✅ Dataset explorer  
✅ CSV batch processing  

### Best Practices Applied
✅ Separation of concerns (MVC)  
✅ RESTful API design  
✅ Reactive state management (Vue)  
✅ CORS enabled for development  
✅ Input validation & sanitization  
✅ Error handling & logging  
✅ Modular components  
✅ Responsive design  

---

## 🔗 Quick Links

- **GitHub:** (Not available)
- **API Documentation:** See `backend/README.md`
- **Frontend Documentation:** See `frontend/README.md`
- **Model Documentation:** See `model/README.md`
- **Dataset Source:** IBM HR Analytics (Kaggle)

---

## 👤 Author

Developed: November 2025

---

## 📄 License

This project is provided as-is for educational purposes.

---

## 🤝 Support

For issues or questions:
1. Check respective README files (backend/frontend/model)
2. Review troubleshooting section above
3. Check console logs for error details

---

**Last Updated:** November 28, 2025  
**Version:** 1.0.0  
**Status:** Production Ready ✅
#   R e s i g n P r e d i c t i o n  
 