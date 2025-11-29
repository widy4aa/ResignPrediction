<template>
  <div class="min-h-screen bg-background">
    <!-- Header -->
    <header class="border-b">
      <div class="container flex h-16 items-center justify-between">
        <router-link to="/" class="flex items-center space-x-2 hover:opacity-80 transition-opacity">
          <div class="flex h-9 w-9 items-center justify-center rounded-md bg-primary text-primary-foreground">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 3v18h18"/>
              <path d="m19 9-5 5-4-4-3 3"/>
            </svg>
          </div>
          <span class="text-lg font-semibold">Attrition Predictor</span>
        </router-link>
        <router-link to="/" class="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors flex items-center gap-2">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="m12 19-7-7 7-7"/>
            <path d="M19 12H5"/>
          </svg>
          Kembali
        </router-link>
      </div>
    </header>

    <div class="container py-8 max-w-4xl">
      <!-- Title -->
      <div class="mb-8">
        <h1 class="text-3xl font-bold tracking-tight mb-2">Prediksi Attrition</h1>
        <p class="text-muted-foreground">Model minimal dengan 7 fitur inti - Akurasi 84.01%</p>
      </div>

      <!-- Model Info -->
      <Card class="p-6 mb-8 bg-muted/50">
        <div class="grid gap-6 md:grid-cols-3">
          <div>
            <div class="text-sm text-muted-foreground mb-1">Fitur Required</div>
            <div class="text-2xl font-bold">7</div>
            <div class="text-xs text-muted-foreground">77% lebih sedikit</div>
          </div>
          <div>
            <div class="text-sm text-muted-foreground mb-1">Akurasi Model</div>
            <div class="text-2xl font-bold">84.01%</div>
            <div class="text-xs text-muted-foreground">Lebih baik dari full</div>
          </div>
          <div>
            <div class="text-sm text-muted-foreground mb-1">Waktu Input</div>
            <div class="text-2xl font-bold">~20 detik</div>
            <div class="text-xs text-muted-foreground">Vs 2-3 menit</div>
          </div>
        </div>
      </Card>

      <!-- Mode Tabs -->
      <div class="flex gap-2 mb-6">
        <Button 
          @click="mode = 'manual'" 
          :variant="mode === 'manual' ? 'default' : 'outline'"
          class="flex-1"
        >
          <svg class="mr-2 h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
          </svg>
          Input Manual
        </Button>
        <Button 
          @click="mode = 'csv'" 
          :variant="mode === 'csv' ? 'default' : 'outline'"
          class="flex-1"
        >
          <svg class="mr-2 h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
          </svg>
          Upload CSV
        </Button>
      </div>

      <!-- Manual Input Form -->
      <Card v-if="mode === 'manual'" class="p-6 mb-8">
        <h2 class="text-xl font-semibold mb-6">Input Data Karyawan</h2>
        <form @submit.prevent="predict" class="space-y-6">
          <div class="grid gap-6 md:grid-cols-2">
            <!-- OverTime -->
            <div class="space-y-2">
              <label class="text-sm font-medium">OverTime</label>
              <select v-model="formData.OverTime" required class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring">
                <option value="">Pilih...</option>
                <option value="Yes">Yes</option>
                <option value="No">No</option>
              </select>
            </div>

            <!-- MonthlyIncome -->
            <div class="space-y-2">
              <label class="text-sm font-medium">Monthly Income</label>
              <input v-model.number="formData.MonthlyIncome" type="number" required placeholder="e.g., 5000" class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring" />
            </div>

            <!-- Age -->
            <div class="space-y-2">
              <label class="text-sm font-medium">Age</label>
              <input v-model.number="formData.Age" type="number" required placeholder="e.g., 35" class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring" />
            </div>

            <!-- TotalWorkingYears -->
            <div class="space-y-2">
              <label class="text-sm font-medium">Total Working Years</label>
              <input v-model.number="formData.TotalWorkingYears" type="number" required placeholder="e.g., 10" class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring" />
            </div>

            <!-- StockOptionLevel -->
            <div class="space-y-2">
              <label class="text-sm font-medium">Stock Option Level</label>
              <select v-model.number="formData.StockOptionLevel" required class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring">
                <option value="">Pilih...</option>
                <option :value="0">0 - No Stock</option>
                <option :value="1">1 - Low</option>
                <option :value="2">2 - Medium</option>
                <option :value="3">3 - High</option>
              </select>
            </div>

            <!-- DistanceFromHome -->
            <div class="space-y-2">
              <label class="text-sm font-medium">Distance From Home (km)</label>
              <input v-model.number="formData.DistanceFromHome" type="number" required placeholder="e.g., 10" class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring" />
            </div>

            <!-- EnvironmentSatisfaction -->
            <div class="space-y-2">
              <label class="text-sm font-medium">Environment Satisfaction</label>
              <select v-model.number="formData.EnvironmentSatisfaction" required class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring">
                <option value="">Pilih...</option>
                <option :value="1">1 - Low</option>
                <option :value="2">2 - Medium</option>
                <option :value="3">3 - High</option>
                <option :value="4">4 - Very High</option>
              </select>
            </div>
          </div>

          <div class="flex gap-4">
            <Button type="submit" :disabled="loading" class="flex-1">
              <svg v-if="loading" class="mr-2 h-4 w-4 animate-spin" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              {{ loading ? 'Memprediksi...' : 'Prediksi Attrition' }}
            </Button>
            <Button type="button" variant="outline" @click="resetForm">Reset</Button>
          </div>
        </form>
      </Card>

      <!-- CSV Upload Form -->
      <Card v-if="mode === 'csv'" class="p-6 mb-8">
        <h2 class="text-xl font-semibold mb-6">Upload File CSV</h2>
        
        <div class="space-y-6">
          <!-- Info -->
          <div class="p-4 rounded-lg bg-blue-50 dark:bg-blue-950 border border-blue-200 dark:border-blue-800">
            <div class="flex gap-3">
              <svg class="h-5 w-5 text-blue-600 dark:text-blue-400 flex-shrink-0" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <div class="text-sm flex-1">
                <div class="font-medium text-blue-900 dark:text-blue-100 mb-1">Format CSV</div>
                <div class="text-blue-700 dark:text-blue-300 mb-2">
                  File harus memiliki kolom: <strong>OverTime, MonthlyIncome, Age, TotalWorkingYears, DistanceFromHome, StockOptionLevel, EnvironmentSatisfaction</strong>
                </div>
                <a href="/sample_prediction.csv" download class="inline-flex items-center gap-1 text-blue-600 dark:text-blue-400 hover:underline font-medium">
                  <svg class="h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                  </svg>
                  Download Sample CSV
                </a>
              </div>
            </div>
          </div>

          <!-- File Input -->
          <div class="border-2 border-dashed rounded-lg p-8 text-center hover:border-primary transition-colors" :class="csvFile ? 'border-primary bg-primary/5' : 'border-muted'">
            <input 
              ref="fileInput"
              type="file" 
              accept=".csv" 
              @change="handleFileUpload"
              class="hidden"
            />
            
            <div v-if="!csvFile">
              <svg class="mx-auto h-12 w-12 text-muted-foreground mb-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              <div class="mb-4">
                <div class="text-sm font-medium mb-1">Upload file CSV</div>
                <div class="text-xs text-muted-foreground">Drag & drop atau klik untuk browse</div>
              </div>
              <Button type="button" @click="$refs.fileInput.click()">
                Pilih File
              </Button>
            </div>

            <div v-else class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <svg class="h-8 w-8 text-primary" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                <div class="text-left">
                  <div class="font-medium">{{ csvFile.name }}</div>
                  <div class="text-xs text-muted-foreground">{{ formatFileSize(csvFile.size) }}</div>
                </div>
              </div>
              <Button type="button" variant="outline" @click="clearFile" size="sm">
                <svg class="h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </Button>
            </div>
          </div>

          <!-- Actions -->
          <div class="flex gap-4">
            <Button type="button" @click="predictCSV" :disabled="!csvFile || csvLoading" class="flex-1">
              <svg v-if="csvLoading" class="mr-2 h-4 w-4 animate-spin" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              {{ csvLoading ? 'Memproses...' : 'Prediksi Batch' }}
            </Button>
            <Button type="button" variant="outline" @click="clearFile">Reset</Button>
          </div>
        </div>
      </Card>

      <!-- CSV Results -->
      <Card v-if="csvResults && csvResults.length > 0" class="p-6 mb-8">
        <div class="flex items-center justify-between mb-6">
          <div>
            <h2 class="text-xl font-semibold">Hasil Prediksi Batch</h2>
            <p class="text-sm text-muted-foreground">Total: {{ csvResults.length }} karyawan</p>
          </div>
          <Button @click="downloadResults" variant="outline" size="sm">
            <svg class="mr-2 h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
            Download CSV
          </Button>
        </div>

        <!-- Summary Stats -->
        <div class="grid gap-4 md:grid-cols-3 mb-6">
          <div class="p-4 rounded-lg border">
            <div class="text-sm text-muted-foreground mb-1">Akan Resign</div>
            <div class="text-2xl font-bold text-destructive">{{ csvResults.filter(r => r.prediction === 'Yes').length }}</div>
            <div class="text-xs text-muted-foreground">{{ ((csvResults.filter(r => r.prediction === 'Yes').length / csvResults.length) * 100).toFixed(1) }}%</div>
          </div>
          <div class="p-4 rounded-lg border">
            <div class="text-sm text-muted-foreground mb-1">Akan Tetap</div>
            <div class="text-2xl font-bold text-green-600">{{ csvResults.filter(r => r.prediction === 'No').length }}</div>
            <div class="text-xs text-muted-foreground">{{ ((csvResults.filter(r => r.prediction === 'No').length / csvResults.length) * 100).toFixed(1) }}%</div>
          </div>
          <div class="p-4 rounded-lg border">
            <div class="text-sm text-muted-foreground mb-1">Avg Confidence</div>
            <div class="text-2xl font-bold">{{ (csvResults.reduce((sum, r) => sum + r.confidence, 0) / csvResults.length).toFixed(1) }}%</div>
          </div>
        </div>

        <!-- Results Table -->
        <div class="border rounded-lg overflow-hidden">
          <div class="overflow-x-auto max-h-96">
            <table class="w-full text-sm">
              <thead class="bg-muted sticky top-0">
                <tr>
                  <th class="text-left p-3 font-medium">#</th>
                  <th class="text-left p-3 font-medium">Prediksi</th>
                  <th class="text-left p-3 font-medium">Confidence</th>
                  <th class="text-left p-3 font-medium">OverTime</th>
                  <th class="text-left p-3 font-medium">Income</th>
                  <th class="text-left p-3 font-medium">Age</th>
                </tr>
              </thead>
              <tbody class="divide-y">
                <tr v-for="(row, index) in csvResults" :key="index" class="hover:bg-muted/50">
                  <td class="p-3 text-muted-foreground">{{ index + 1 }}</td>
                  <td class="p-3">
                    <Badge :variant="row.prediction === 'Yes' ? 'destructive' : 'default'">
                      {{ row.prediction === 'Yes' ? 'Resign' : 'Tetap' }}
                    </Badge>
                  </td>
                  <td class="p-3 font-medium">{{ row.confidence.toFixed(1) }}%</td>
                  <td class="p-3">{{ row.input.OverTime }}</td>
                  <td class="p-3">{{ row.input.MonthlyIncome.toLocaleString() }}</td>
                  <td class="p-3">{{ row.input.Age }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </Card>

      <!-- Result -->
      <Card v-if="result" class="p-6">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-xl font-semibold">Hasil Prediksi</h2>
          <Badge :variant="result.prediction === 'Yes' ? 'destructive' : 'default'">
            {{ result.prediction === 'Yes' ? 'Resign' : 'Tetap' }}
          </Badge>
        </div>
        
        <div class="space-y-4">
          <div class="p-4 rounded-lg border">
            <div class="text-sm text-muted-foreground mb-1">Confidence Score</div>
            <div class="text-2xl font-bold">{{ result.confidence ? result.confidence.toFixed(2) : 0 }}%</div>
            <div class="w-full bg-muted rounded-full h-2 mt-2">
              <div class="bg-primary h-2 rounded-full transition-all" :style="{ width: result.confidence + '%' }"></div>
            </div>
          </div>

          <div class="p-4 rounded-lg bg-muted/50">
            <div class="text-sm font-medium mb-2">Interpretasi:</div>
            <p class="text-sm text-muted-foreground">
              {{ result.prediction === 'Yes' 
                ? 'Karyawan ini memiliki risiko tinggi untuk resign. Pertimbangkan untuk melakukan retention interview dan mengevaluasi kompensasi serta work-life balance.' 
                : 'Karyawan ini cenderung tetap di perusahaan. Tetap monitor engagement dan career development untuk mempertahankan loyalitas.' 
              }}
            </p>
          </div>
        </div>
      </Card>

      <!-- Error -->
      <Card v-if="error" class="p-6 border-destructive">
        <div class="flex items-start gap-3">
          <svg class="h-5 w-5 text-destructive" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <div>
            <div class="font-semibold text-destructive">Error</div>
            <div class="text-sm text-muted-foreground">{{ error }}</div>
          </div>
        </div>
      </Card>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import Button from '../components/ui/Button.vue'
import Card from '../components/ui/Card.vue'
import Badge from '../components/ui/Badge.vue'
import { API_ENDPOINTS } from '../config/api'

const mode = ref('manual')
const fileInput = ref(null)

const formData = ref({
  OverTime: '',
  MonthlyIncome: null,
  Age: null,
  TotalWorkingYears: null,
  DistanceFromHome: null,
  StockOptionLevel: null,
  EnvironmentSatisfaction: null
})

const loading = ref(false)
const result = ref(null)
const error = ref(null)

// CSV state
const csvFile = ref(null)
const csvLoading = ref(false)
const csvResults = ref(null)

const predict = async () => {
  loading.value = true
  error.value = null
  result.value = null

  try {
    const response = await axios.post(API_ENDPOINTS.predict, formData.value)
    result.value = response.data
  } catch (err) {
    error.value = err.response?.data?.error || 'Terjadi kesalahan saat prediksi'
  } finally {
    loading.value = false
  }
}

const resetForm = () => {
  formData.value = {
    OverTime: '',
    MonthlyIncome: null,
    Age: null,
    TotalWorkingYears: null,
    DistanceFromHome: null,
    StockOptionLevel: null,
    EnvironmentSatisfaction: null
  }
  result.value = null
  error.value = null
}

// CSV Functions
const handleFileUpload = (event) => {
  const file = event.target.files[0]
  if (file && file.type === 'text/csv') {
    csvFile.value = file
    csvResults.value = null
    error.value = null
  } else {
    error.value = 'File harus berformat CSV'
    event.target.value = ''
  }
}

const clearFile = () => {
  csvFile.value = null
  csvResults.value = null
  error.value = null
  if (fileInput.value) {
    fileInput.value.value = ''
  }
}

const formatFileSize = (bytes) => {
  if (bytes < 1024) return bytes + ' B'
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB'
  return (bytes / (1024 * 1024)).toFixed(1) + ' MB'
}

const parseCSV = (text) => {
  const lines = text.trim().split('\n')
  const headers = lines[0].split(',').map(h => h.trim())
  
  const data = []
  for (let i = 1; i < lines.length; i++) {
    const values = lines[i].split(',').map(v => v.trim())
    const row = {}
    headers.forEach((header, index) => {
      const value = values[index]
      // Convert to number if possible
      if (!isNaN(value) && value !== '') {
        row[header] = Number(value)
      } else {
        row[header] = value
      }
    })
    data.push(row)
  }
  
  return data
}

const predictCSV = async () => {
  if (!csvFile.value) return

  csvLoading.value = true
  error.value = null
  csvResults.value = null

  try {
    const text = await csvFile.value.text()
    const data = parseCSV(text)
    
    // Validate required columns
    const requiredCols = ['OverTime', 'MonthlyIncome', 'Age', 'TotalWorkingYears', 
                          'DistanceFromHome', 'StockOptionLevel', 'EnvironmentSatisfaction']
    const missingCols = requiredCols.filter(col => !data[0].hasOwnProperty(col))
    
    if (missingCols.length > 0) {
      error.value = `Kolom tidak lengkap: ${missingCols.join(', ')}`
      csvLoading.value = false
      return
    }

    // Make predictions for each row
    const results = []
    for (const row of data) {
      try {
        const response = await axios.post(API_ENDPOINTS.predict, row)
        results.push({
          input: row,
          prediction: response.data.prediction,
          confidence: response.data.confidence,
          probabilities: response.data.probabilities
        })
      } catch (err) {
        results.push({
          input: row,
          error: err.response?.data?.error || 'Error'
        })
      }
    }

    csvResults.value = results
  } catch (err) {
    error.value = 'Gagal memproses file CSV: ' + err.message
  } finally {
    csvLoading.value = false
  }
}

const downloadResults = () => {
  if (!csvResults.value || csvResults.value.length === 0) return

  // Create CSV content
  const headers = ['No', 'Prediction', 'Confidence', 'OverTime', 'MonthlyIncome', 'Age', 
                   'TotalWorkingYears', 'DistanceFromHome', 'StockOptionLevel', 'EnvironmentSatisfaction']
  
  let csv = headers.join(',') + '\n'
  
  csvResults.value.forEach((row, index) => {
    const values = [
      index + 1,
      row.prediction || 'Error',
      row.confidence ? row.confidence.toFixed(2) : 'N/A',
      row.input.OverTime,
      row.input.MonthlyIncome,
      row.input.Age,
      row.input.TotalWorkingYears,
      row.input.DistanceFromHome,
      row.input.StockOptionLevel,
      row.input.EnvironmentSatisfaction
    ]
    csv += values.join(',') + '\n'
  })

  // Download
  const blob = new Blob([csv], { type: 'text/csv' })
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'prediction_results_' + new Date().getTime() + '.csv'
  a.click()
  window.URL.revokeObjectURL(url)
}
</script>
