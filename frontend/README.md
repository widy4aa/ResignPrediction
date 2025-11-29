# 🎨 Frontend - Employee Attrition Prediction UI

Frontend aplikasi Employee Attrition Prediction dibangun dengan **Vue.js 3**, **Vite**, dan **Tailwind CSS**.

## 🏗️ Struktur Project

```
frontend/
├── src/
│   ├── App.vue                 # Root component
│   ├── main.js                 # Entry point
│   ├── style.css               # Global styles
│   ├── pages/
│   │   ├── Landing.vue         # Home page (hero + stats)
│   │   ├── Predict.vue         # Prediction page (form + results)
│   │   └── Insight.vue         # Insight page (dataset + visualizations)
│   ├── components/
│   │   └── ui/
│   │       ├── Badge.vue       # Badge component
│   │       ├── Button.vue      # Button component
│   │       └── Card.vue        # Card component
│   └── lib/
│       └── utils.js            # Utility functions
├── public/
│   ├── sample_prediction.csv   # Contoh file CSV
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv  # Dataset asli
├── index.html                  # HTML template
├── package.json                # Dependencies
├── vite.config.js              # Vite configuration
├── tailwind.config.js          # Tailwind CSS config
├── postcss.config.js           # PostCSS config
└── .gitignore
```

## 🎯 Pages Overview

### 1. Landing Page (`Landing.vue`)
**URL:** `/`

**Fitur:**
- Hero section dengan project title
- Dynamic statistics dari API:
  - Model accuracy (84.01%)
  - Dataset samples (1,470)
  - Features used (7)
- Call-to-action buttons ke Predict & Insight pages
- Responsive design untuk mobile

**Key Functions:**
```javascript
loadStats()        // Fetch stats dari /api/results/summary
formatNumber()     // Format angka dengan comma separator
```

**Dependencies:**
- axios (API calls)
- Tailwind CSS (styling)

---

### 2. Predict Page (`Predict.vue`)
**URL:** `/predict`

**Fitur:**
- **Manual Input Mode:**
  - Form dengan 7 input fields
  - Real-time validation
  - Submit button untuk prediksi
  
- **CSV Upload Mode:**
  - File input untuk CSV
  - Preview data yang di-upload
  - Batch prediksi semua rows
  - Download hasil prediksi

**Input Fields (7 fitur):**
1. **OverTime** - Dropdown (Yes/No)
2. **MonthlyIncome** - Number input
3. **Age** - Number input
4. **TotalWorkingYears** - Number input
5. **DistanceFromHome** - Number input
6. **StockOptionLevel** - Number input (0-3)
7. **EnvironmentSatisfaction** - Number input (1-4)

**Key Functions:**
```javascript
predictSingle()      // POST /predict dengan manual input
handleCSVUpload()    // Parse dan validasi CSV file
predictBatch()       // Prediksi semua rows dari CSV
downloadResults()    // Download hasil prediksi sebagai CSV
parseCSV()          // Parse CSV string ke array objects
validateInput()      // Validasi 7 required fields
```

**CSV Format:**
```csv
OverTime,MonthlyIncome,Age,TotalWorkingYears,DistanceFromHome,StockOptionLevel,EnvironmentSatisfaction
No,5000,35,10,5,1,3
Yes,4000,28,5,15,0,2
```

**Response Handling:**
```javascript
{
  prediction: "No",
  confidence: 95.53,
  probabilities: {
    "No": 95.53,
    "Yes": 4.47
  }
}
```

---

### 3. Insight Page (`Insight.vue`)
**URL:** `/insight`

**Fitur:**

#### A. Dataset Overview
- Total samples & features
- Class distribution (Attrition Yes/No)
- Dataset preview table dengan pagination:
  - Tampilkan all 1,470 rows
  - 35 columns dari dataset asli
  - Pagination controls (First/Prev/Next/Last)
  - Rows per page selector (10/25/50/100)
  - Color-coded Attrition column
  - Sticky first column (row number)

#### B. Model Sections (3 model versions)
1. **Full Model (31 features)**
   - Feature cards (fitur yang digunakan + yang dihapus)
   - 3 visualisasi graphs
   - Penjelasan setiap graph

2. **Reduced Model (11 features)**
   - Feature cards dengan detail
   - 3 visualisasi graphs
   - Graph explanations

3. **Minimal Model (7 features)**
   - Feature ranking dengan importance %
   - 3 visualisasi graphs
   - Detailed explanations

#### C. Comparison Section
- 5 comparison graphs antar model
- Graph explanations
- Summary insights & recommendations

#### D. Interactive Features
- Clickable graphs → popup modal
- Pagination untuk dataset table
- Hover effects pada cards
- Color-coded information

**Key Functions:**
```javascript
loadData()               // Load API results & dataset
loadDataset()           // Fetch dan parse CSV dataset
openModal()             // Buka image modal untuk graphs
openVisualization()     // Helper untuk open modal
```

**State Management:**
```javascript
// API Data
modelResults = ref({})
datasetRows = ref([])
datasetColumns = ref([])

// Pagination
currentPage = ref(1)
rowsPerPage = ref(25)
paginatedRows = computed()
totalPages = computed()
```

---

## 🎨 Components

### Badge Component
Menampilkan label/status dengan styling.

```vue
<Badge :text="label" :variant="success|warning|error" />
```

### Button Component
Reusable button dengan berbagai varian.

```vue
<Button @click="action" :disabled="false" variant="primary">Click me</Button>
```

### Card Component
Container untuk content dengan border & shadow.

```vue
<Card>
  <div>Content here</div>
</Card>
```

---

## 🚀 Setup & Development

### 1. Install Dependencies
```bash
cd frontend
npm install
```

### 2. Start Development Server
```bash
npm run dev
```

Server akan berjalan di `http://localhost:5173`

### 3. Build for Production
```bash
npm run build
```

Output di folder `dist/`

### 4. Preview Production Build
```bash
npm run preview
```

---

## 🔧 Configuration

### Vite Config (`vite.config.js`)
```javascript
import vue from '@vitejs/plugin-vue'

export default {
  plugins: [vue()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true
      }
    }
  }
}
```

### Tailwind Config (`tailwind.config.js`)
```javascript
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js}"
  ],
  theme: {
    extend: {}
  }
}
```

---

## 📡 API Integration

### Base URL
Development: `http://localhost:5000`

### Endpoints Used

**Landing Page:**
- `GET /api/results/summary` - Fetch model stats

**Predict Page:**
- `GET /features` - Get required features
- `POST /predict` - Single prediction
- `POST /predict` - Batch prediction dari CSV

**Insight Page:**
- `GET /api/results` - Get all model results
- `GET /api/results/model/<type>` - Get specific model
- `GET /api/visualizations/list` - Get visualizations list
- `GET /api/visualizations/<category>/<file>` - Get image

---

## 🎨 Styling

### Framework
- **Tailwind CSS** - Utility-first CSS
- **Custom CSS** - Additional custom styles di `style.css`

### Color Scheme
- **Primary:** Blue (#3B82F6)
- **Success:** Green (#10B981)
- **Warning:** Yellow (#F59E0B)
- **Error:** Red (#EF4444)
- **Destructive:** #DC2626

### Responsive Breakpoints
- **Mobile:** < 640px
- **Tablet:** 640px - 1024px
- **Desktop:** > 1024px

---

## 🔄 Data Flow

```
User Action
    ↓
Vue Component (handleEvent)
    ↓
API Call (axios)
    ↓
Backend Process
    ↓
API Response (JSON)
    ↓
Reactive State Update
    ↓
Template Re-render
    ↓
UI Update
```

---

## 🧪 Testing

### Manual Testing Checklist

**Landing Page:**
- [ ] Page loads dengan stats dari API
- [ ] Stats menampilkan nilai yang benar
- [ ] Buttons navigasi ke halaman yang tepat
- [ ] Responsive di mobile/tablet/desktop

**Predict Page:**
- [ ] Form validation bekerja
- [ ] Manual prediction berhasil
- [ ] CSV upload & parsing bekerja
- [ ] Batch prediction berhasil
- [ ] Download hasil CSV bekerja
- [ ] Error messages tampil dengan jelas

**Insight Page:**
- [ ] Dataset table load dengan benar
- [ ] Pagination bekerja (First/Prev/Next/Last)
- [ ] Rows per page selector bekerja
- [ ] Graphs load dari API
- [ ] Modal popup buka saat graph diklik
- [ ] Color coding Attrition bekerja
- [ ] Sticky column tetap terlihat saat scroll

---

## 🐛 Troubleshooting

### Issue: API connection error
**Solution:**
- Pastikan backend running di `http://localhost:5000`
- Check CORS configuration di backend
- Cek browser console untuk error details

### Issue: Images not loading
**Solution:**
- Pastikan file ada di `backend/visualizations/`
- Check `/api/visualizations/list` endpoint
- Verify path di image URL

### Issue: CSV parsing error
**Solution:**
- Pastikan CSV format sesuai (7 columns)
- Check console untuk parsing error
- Validate data types sesuai requirement

### Issue: Pagination tidak bekerja
**Solution:**
- Clear browser cache
- Restart dev server
- Check `paginatedRows` computed property

---

## 📦 Dependencies

```json
{
  "dependencies": {
    "vue": "^3.x",
    "axios": "^1.x"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^4.x",
    "vite": "^4.x",
    "tailwindcss": "^3.x",
    "postcss": "^8.x"
  }
}
```

---

## 🚀 Deployment

### Development Build
```bash
npm run dev
```

### Production Build
```bash
npm run build
npm run preview
```

### Environment Variables
Buat file `.env` jika diperlukan:
```
VITE_API_URL=http://localhost:5000
VITE_APP_TITLE=Attrition Prediction System
```

---

## 📝 Notes

- ✅ Fully responsive design
- ✅ Real-time data dari API
- ✅ Client-side CSV parsing
- ✅ Modal popups untuk images
- ✅ Pagination untuk large datasets
- ✅ Color-coded information
- ✅ Comprehensive error handling

---

## 🔗 Related Files

- **Backend API:** `../backend/app_mvc.py`
- **Dataset:** `../model/WA_Fn-UseC_-HR-Employee-Attrition.csv`
- **Visualizations:** Backend serve dari `/api/visualizations/`
