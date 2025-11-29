# 🔧 Backend API - Employee Attrition Prediction

## Arsitektur MVC (Model-View-Controller)

Backend ini dibangun menggunakan **Flask** dengan pola **MVC** untuk memisahkan logika bisnis, akses data, dan respons API.

## 📁 Struktur File

```
backend/
├── app_mvc.py          # Entry point aplikasi
├── config.py           # Konfigurasi aplikasi
├── models.py           # Layer akses data (Model)
├── controllers.py      # Layer logika bisnis (Controller)
├── views.py            # Layer respons API (View)
├── routes.py           # Definisi endpoint
├── requirements.txt    # Dependencies Python
└── .env.example        # Template environment variables
```

## 🎯 Alur Request MVC

```
Client Request
    ↓
routes.py (mapping URL ke controller)
    ↓
controllers.py (validasi & logika bisnis)
    ↓
models.py (akses model ML & data)
    ↓
views.py (format respons JSON)
    ↓
Client Response
```

## 🚀 API Endpoints

### 1. Health Check
**GET** `/health`

Mengecek status server dan model.

**Response:**
```json
{
  "status": "healthy",
  "message": "Server is running",
  "model": {
    "loaded": true,
    "type": "Random Forest",
    "features": 7,
    "accuracy": 84.01
  }
}
```

---

### 2. Get Features List
**GET** `/features`

Mendapatkan list 7 fitur yang diperlukan untuk prediksi.

**Response:**
```json
{
  "required_features": [
    "OverTime",
    "MonthlyIncome",
    "Age",
    "TotalWorkingYears",
    "DistanceFromHome",
    "StockOptionLevel",
    "EnvironmentSatisfaction"
  ],
  "total": 7
}
```

---

### 3. Predict Attrition
**POST** `/predict`

Melakukan prediksi attrition karyawan.

**Request Body:**
```json
{
  "OverTime": "No",
  "MonthlyIncome": 5000,
  "Age": 35,
  "TotalWorkingYears": 10,
  "DistanceFromHome": 5,
  "StockOptionLevel": 1,
  "EnvironmentSatisfaction": 3
}
```

**Response:**
```json
{
  "prediction": "No",
  "confidence": 95.53,
  "probabilities": {
    "No": 95.53,
    "Yes": 4.47
  },
  "model_info": {
    "accuracy": 84.01,
    "features_used": 7
  }
}
```

---

### 4. Get Training Results
**GET** `/api/results`

Mendapatkan hasil training lengkap dari 3 model.

**Response:**
```json
{
  "full": {
    "accuracy": 83.33,
    "features_count": 31,
    "train_accuracy": 87.12,
    "test_accuracy": 83.33
  },
  "reduced": {
    "accuracy": 83.33,
    "features_count": 11,
    "train_accuracy": 85.67,
    "test_accuracy": 83.33
  },
  "minimal": {
    "accuracy": 84.01,
    "features_count": 7,
    "train_accuracy": 89.29,
    "test_accuracy": 84.01
  }
}
```

---

### 5. Get Results Summary
**GET** `/api/results/summary`

Mendapatkan ringkasan perbandingan 3 model.

**Response:**
```json
{
  "total_models": 3,
  "dataset_info": {
    "total_samples": 1470,
    "features": 35,
    "target": "Attrition"
  },
  "models": [...]
}
```

---

### 6. Get Model Details
**GET** `/api/results/model/<type>`

Mendapatkan detail model spesifik (`full`, `reduced`, atau `minimal`).

**Response:**
```json
{
  "model_type": "minimal",
  "accuracy": 84.01,
  "features_count": 7,
  "features": [...],
  "metrics": {...}
}
```

---

### 7. List Visualizations
**GET** `/api/visualizations/list`

Mendapatkan daftar semua visualisasi yang tersedia.

**Response:**
```json
{
  "categories": {
    "full": ["preprocessing_flow.png", "confusion_matrix.png", ...],
    "reduced": [...],
    "minimal": [...],
    "comparison": [...]
  },
  "total": 19
}
```

---

### 8. Get Visualization Image
**GET** `/api/visualizations/<category>/<filename>`

Menampilkan file gambar visualisasi.

**Example:**
- `/api/visualizations/full/confusion_matrix.png`
- `/api/visualizations/minimal/feature_importance.png`
- `/api/visualizations/comparison/accuracy_comparison.png`

---

## 🔧 Setup & Installation

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Konfigurasi Environment (Optional)
```bash
cp .env.example .env
# Edit .env sesuai kebutuhan
```

### 3. Jalankan Server
```bash
python app_mvc.py
```

Server akan berjalan di `http://127.0.0.1:5000`

---

## 📦 Dependencies

```
Flask==3.0.0
flask-cors==4.0.0
pandas==2.1.3
scikit-learn==1.3.2
numpy==1.26.2
```

---

## 🧪 Testing API

### Manual Test dengan Python:
```python
import requests

# Health check
response = requests.get('http://localhost:5000/health')
print(response.json())

# Predict
data = {
    "OverTime": "No",
    "MonthlyIncome": 5000,
    "Age": 35,
    "TotalWorkingYears": 10,
    "DistanceFromHome": 5,
    "StockOptionLevel": 1,
    "EnvironmentSatisfaction": 3
}
response = requests.post('http://localhost:5000/predict', json=data)
print(response.json())
```

### Manual Test dengan PowerShell:
```powershell
# Health check
Invoke-RestMethod -Uri http://localhost:5000/health

# Predict
$body = @{
    OverTime = 'No'
    MonthlyIncome = 5000
    Age = 35
    TotalWorkingYears = 10
    DistanceFromHome = 5
    StockOptionLevel = 1
    EnvironmentSatisfaction = 3
} | ConvertTo-Json

Invoke-RestMethod -Uri http://localhost:5000/predict -Method Post -Body $body -ContentType 'application/json'
```

---

## 🎯 Model Details

- **Type**: Random Forest Classifier
- **Features**: 7 (minimal model)
- **Accuracy**: 84.01%
- **Training Accuracy**: 89.29%
- **Testing Accuracy**: 84.01%

### 7 Features Used:
1. **OverTime** - Yes/No
2. **MonthlyIncome** - Gaji bulanan
3. **Age** - Umur karyawan
4. **TotalWorkingYears** - Total pengalaman kerja
5. **DistanceFromHome** - Jarak rumah ke kantor
6. **StockOptionLevel** - Level stock option (0-3)
7. **EnvironmentSatisfaction** - Kepuasan lingkungan (1-4)

---

## ⚠️ Error Handling

### Missing Features
```json
{
  "error": "Missing required features",
  "missing": ["Age", "MonthlyIncome"],
  "required": [...]
}
```

### Invalid Data Type
```json
{
  "error": "Invalid data type",
  "field": "Age",
  "expected": "number",
  "received": "string"
}
```

### Server Error
```json
{
  "error": "Prediction failed",
  "message": "Internal server error"
}
```

---

## 📝 Notes

- CORS sudah di-enable untuk frontend development
- Model di-load saat server startup
- Semua endpoint menggunakan JSON format
- Error handling untuk semua edge cases
- Validasi input ketat untuk 7 fitur

---

## 🔗 Related Files

- **Model Training**: `../model/generate_graphs.py`
- **Frontend**: `../frontend/src/pages/Predict.vue`
- **Dataset**: `../model/WA_Fn-UseC_-HR-Employee-Attrition.csv`
