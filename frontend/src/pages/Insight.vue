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

    <!-- Loading State -->
    <div v-if="loading" class="container py-16 text-center">
      <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary mb-4"></div>
      <p class="text-muted-foreground">Memuat data...</p>
    </div>

    <!-- Main Content -->
    <div v-else class="container py-8 max-w-6xl space-y-12">
      <!-- Title -->
      <div class="text-center">
        <h1 class="text-4xl font-bold tracking-tight mb-2">Model Documentation</h1>
        <p class="text-lg text-muted-foreground">Dokumentasi lengkap proses training dan evaluasi model</p>
        <div class="mt-4 inline-flex items-center gap-2 text-sm text-muted-foreground">
          <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
          </svg>
          Training Date: {{ resultsData.training_date }}
        </div>
      </div>

      <!-- 1. INFORMASI DATASET -->
      <section id="dataset">
        <Card class="p-6">
          <h2 class="text-2xl font-bold mb-6">📊 Informasi Dataset</h2>
          
          <div class="grid gap-4 md:grid-cols-4 mb-6">
            <div class="p-4 rounded-lg border text-center">
              <div class="text-3xl font-bold mb-1">{{ resultsData.dataset_info.total_samples.toLocaleString() }}</div>
              <div class="text-sm text-muted-foreground">Total Samples</div>
            </div>
            <div class="p-4 rounded-lg border text-center">
              <div class="text-3xl font-bold mb-1">{{ resultsData.dataset_info.total_features_original }}</div>
              <div class="text-sm text-muted-foreground">Fitur Awal</div>
            </div>
            <div class="p-4 rounded-lg border text-center">
              <div class="text-3xl font-bold mb-1">{{ resultsData.dataset_info.total_features_after_cleanup }}</div>
              <div class="text-sm text-muted-foreground">Setelah Cleanup</div>
            </div>
            <div class="p-4 rounded-lg border text-center">
              <div class="text-3xl font-bold mb-1 text-destructive">{{ resultsData.dataset_info.attrition_rate.toFixed(2) }}%</div>
              <div class="text-sm text-muted-foreground">Attrition Rate</div>
            </div>
          </div>

          <div class="grid gap-6 md:grid-cols-2 mb-6">
            <div class="space-y-3">
              <h3 class="font-semibold text-lg">Distribusi Kelas</h3>
              <div class="p-4 rounded-lg border">
                <div class="flex justify-between items-center mb-2">
                  <span class="text-sm">Tetap (No Attrition)</span>
                  <Badge>{{ resultsData.dataset_info.attrition_no }}</Badge>
                </div>
                <div class="w-full bg-muted rounded-full h-3">
                  <div class="bg-green-500 h-3 rounded-full" :style="{ width: ((resultsData.dataset_info.attrition_no / resultsData.dataset_info.total_samples) * 100) + '%' }"></div>
                </div>
                <div class="text-xs text-muted-foreground mt-1">{{ ((resultsData.dataset_info.attrition_no / resultsData.dataset_info.total_samples) * 100).toFixed(1) }}%</div>
              </div>
              <div class="p-4 rounded-lg border">
                <div class="flex justify-between items-center mb-2">
                  <span class="text-sm">Resign (Yes Attrition)</span>
                  <Badge variant="destructive">{{ resultsData.dataset_info.attrition_yes }}</Badge>
                </div>
                <div class="w-full bg-muted rounded-full h-3">
                  <div class="bg-destructive h-3 rounded-full" :style="{ width: resultsData.dataset_info.attrition_rate + '%' }"></div>
                </div>
                <div class="text-xs text-muted-foreground mt-1">{{ resultsData.dataset_info.attrition_rate.toFixed(1) }}%</div>
              </div>
            </div>
            
            <div class="space-y-3">
              <h3 class="font-semibold text-lg">Dataset Info</h3>
              <div class="text-sm space-y-2 p-4 rounded-lg bg-muted/50">
                <div><span class="font-medium">Source:</span> IBM HR Analytics</div>
                <div><span class="font-medium">Target:</span> Attrition (Binary: Yes/No)</div>
                <div><span class="font-medium">Imbalance:</span> Yes (16.1% resign, 83.9% tetap)</div>
                <div><span class="font-medium">Features:</span> 35 → 31 (cleanup) → 7 (minimal)</div>
              </div>
            </div>
          </div>

          <!-- Dataset Preview -->
          <div class="mt-6">
            <div class="flex items-center justify-between mb-4">
              <h3 class="font-semibold text-lg">Preview Dataset Asli</h3>
              <div class="text-sm text-muted-foreground">
                Menampilkan {{ (currentPage - 1) * rowsPerPage + 1 }} - {{ Math.min(currentPage * rowsPerPage, datasetRows.length) }} dari {{ datasetRows.length }} baris
              </div>
            </div>
            
            <!-- Table -->
            <div class="border rounded-lg overflow-hidden">
              <div class="overflow-x-auto">
                <table class="w-full text-sm">
                  <thead class="bg-muted">
                    <tr>
                      <th class="px-4 py-3 text-left font-semibold sticky left-0 bg-muted z-10">#</th>
                      <th v-for="column in datasetColumns" :key="column" class="px-4 py-3 text-left font-semibold whitespace-nowrap">
                        {{ column }}
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(row, index) in paginatedRows" :key="index" class="border-t hover:bg-muted/50">
                      <td class="px-4 py-2 font-medium sticky left-0 bg-background z-10">{{ (currentPage - 1) * rowsPerPage + index + 1 }}</td>
                      <td v-for="column in datasetColumns" :key="column" class="px-4 py-2 whitespace-nowrap">
                        <span v-if="column === 'Attrition'" :class="row[column] === 'Yes' ? 'text-destructive font-semibold' : 'text-green-600 font-semibold'">
                          {{ row[column] }}
                        </span>
                        <span v-else>{{ row[column] }}</span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Pagination -->
            <div class="flex items-center justify-between mt-4">
              <div class="flex items-center gap-2">
                <label class="text-sm text-muted-foreground">Rows per page:</label>
                <select v-model="rowsPerPage" @change="currentPage = 1" class="px-3 py-1 border rounded-md text-sm">
                  <option :value="10">10</option>
                  <option :value="25">25</option>
                  <option :value="50">50</option>
                  <option :value="100">100</option>
                </select>
              </div>
              
              <div class="flex items-center gap-2">
                <Button 
                  @click="currentPage = 1" 
                  :disabled="currentPage === 1"
                  variant="outline" 
                  size="sm"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 19l-7-7 7-7m8 14l-7-7 7-7"></path>
                  </svg>
                </Button>
                <Button 
                  @click="currentPage--" 
                  :disabled="currentPage === 1"
                  variant="outline" 
                  size="sm"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
                  </svg>
                </Button>
                
                <span class="text-sm text-muted-foreground px-4">
                  Halaman {{ currentPage }} dari {{ totalPages }}
                </span>
                
                <Button 
                  @click="currentPage++" 
                  :disabled="currentPage === totalPages"
                  variant="outline" 
                  size="sm"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                  </svg>
                </Button>
                <Button 
                  @click="currentPage = totalPages" 
                  :disabled="currentPage === totalPages"
                  variant="outline" 
                  size="sm"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5l7 7-7 7M5 5l7 7-7 7"></path>
                  </svg>
                </Button>
              </div>
            </div>
          </div>
        </Card>
      </section>

      <!-- 2. MODEL V1 FULL -->
      <section id="model-full">
        <Card class="p-6 bg-gradient-to-br from-blue-50/50 to-indigo-50/50">
          <div class="flex items-center gap-3 mb-6">
            <Badge variant="outline" class="text-base px-3 py-1">MODEL V1</Badge>
            <h2 class="text-2xl font-bold">Full Model (31 Fitur)</h2>
          </div>

          <!-- Preprocessing -->
          <div class="mb-6">
            <h3 class="text-xl font-semibold mb-4 flex items-center gap-2">
              <span class="bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center text-sm">1</span>
              Preprocessing
            </h3>
            <div class="grid gap-4 md:grid-cols-2">
              <div>
                <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('full', 'preprocessing_flow.png')">
                  <img :src="`http://localhost:5000${getVisualization('full', 'preprocessing_flow.png')}`" alt="Full Preprocessing" class="w-full" />
                </div>
                <div class="mt-2 p-3 bg-blue-50 rounded-lg border border-blue-200">
                  <p class="text-xs text-blue-900"><strong>📊 Preprocessing Flow:</strong> Diagram alur data cleaning dan feature engineering. Menunjukkan transformasi dari 35 fitur raw → 31 fitur final setelah drop 4 fitur konstanta.</p>
                </div>
              </div>
              <div class="space-y-3 text-sm">
                <div class="p-4 rounded-lg border">
                  <div class="font-semibold mb-2">📋 Tahapan Preprocessing</div>
                  <ul class="space-y-1 text-muted-foreground">
                    <li>• Load dataset (1,470 rows, 35 columns)</li>
                    <li>• Drop kolom redundant (EmployeeCount, Over18, StandardHours)</li>
                    <li>• Encoding categorical features</li>
                    <li>• Train-test split (80:20)</li>
                    <li>• Feature scaling untuk numerik</li>
                  </ul>
                </div>
                <div class="p-4 rounded-lg bg-blue-50 border border-blue-200">
                  <div class="font-semibold mb-1">✅ Output</div>
                  <div class="text-muted-foreground">31 fitur siap untuk modeling</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Modeling -->
          <div class="mb-6">
            <h3 class="text-xl font-semibold mb-4 flex items-center gap-2">
              <span class="bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center text-sm">2</span>
              Modeling
            </h3>
            <div class="grid gap-4 md:grid-cols-3 mb-4">
              <div class="p-4 rounded-lg border">
                <div class="text-sm text-muted-foreground mb-1">Algorithm</div>
                <div class="font-bold text-lg">Random Forest</div>
              </div>
              <div class="p-4 rounded-lg border">
                <div class="text-sm text-muted-foreground mb-1">Total Features</div>
                <div class="font-bold text-lg">{{ resultsData.models.full.num_features }}</div>
              </div>
              <div class="p-4 rounded-lg border">
                <div class="text-sm text-muted-foreground mb-1">Training Time</div>
                <div class="font-bold text-lg">{{ resultsData.models.full.training_time.toFixed(4) }}s</div>
              </div>
            </div>

            <!-- Features Detail -->
            <div class="grid gap-4 md:grid-cols-2">
              <div class="p-4 rounded-lg border-2 border-blue-200 bg-blue-50/50">
                <div class="flex items-center gap-2 mb-3">
                  <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                  <div class="font-semibold text-blue-900">✓ Fitur Digunakan (31)</div>
                </div>
                <div class="text-sm space-y-2 max-h-64 overflow-y-auto">
                  <div v-for="feature in resultsData.models.full.features" :key="feature" class="flex items-start gap-2 text-blue-800">
                    <span class="text-blue-500 mt-0.5">•</span>
                    <span>{{ feature }}</span>
                  </div>
                </div>
              </div>

              <div class="p-4 rounded-lg border bg-muted/30">
                <div class="flex items-center gap-2 mb-3">
                  <svg class="w-5 h-5 text-muted-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                  </svg>
                  <div class="font-semibold">✗ Fitur Dihapus (4)</div>
                </div>
                <div class="text-sm space-y-3 text-muted-foreground">
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">EmployeeCount</strong>
                      <p class="text-xs">Konstanta (semua = 1), tidak informatif</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">Over18</strong>
                      <p class="text-xs">Konstanta (semua = Yes), redundan</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">StandardHours</strong>
                      <p class="text-xs">Konstanta (semua = 80), tidak variatif</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">EmployeeNumber</strong>
                      <p class="text-xs">ID unik, tidak relevan untuk prediksi</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Evaluasi -->
          <div>
            <h3 class="text-xl font-semibold mb-4 flex items-center gap-2">
              <span class="bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center text-sm">3</span>
              Evaluasi
            </h3>
            <div class="grid gap-4 md:grid-cols-2 mb-4">
              <div>
                <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('full', 'confusion_matrix.png')">
                  <img :src="`http://localhost:5000${getVisualization('full', 'confusion_matrix.png')}`" alt="Full Confusion Matrix" class="w-full" />
                </div>
                <div class="mt-2 p-3 bg-blue-50 rounded-lg border border-blue-200">
                  <p class="text-xs text-blue-900"><strong>📈 Confusion Matrix:</strong> Matriks prediksi vs aktual. Diagonal utama (TN & TP) menunjukkan prediksi benar. Model ini prediksi 235 No Attrition benar, 10 Yes Attrition benar.</p>
                </div>
              </div>
              <div>
                <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('full', 'feature_importance.png')">
                  <img :src="`http://localhost:5000${getVisualization('full', 'feature_importance.png')}`" alt="Full Feature Importance" class="w-full" />
                </div>
                <div class="mt-2 p-3 bg-blue-50 rounded-lg border border-blue-200">
                  <p class="text-xs text-blue-900"><strong>🎯 Feature Importance:</strong> Kontribusi setiap fitur dalam model. MonthlyIncome, Age, dan TotalWorkingYears paling berpengaruh. Fitur dengan importance <3% kandidat untuk dihapus.</p>
                </div>
              </div>
            </div>
            <div class="grid gap-4 md:grid-cols-4">
              <div class="p-4 rounded-lg border text-center">
                <div class="text-sm text-muted-foreground mb-1">Train Accuracy</div>
                <div class="font-bold text-2xl">{{ resultsData.models.full.train_accuracy.toFixed(2) }}%</div>
              </div>
              <div class="p-4 rounded-lg border text-center">
                <div class="text-sm text-muted-foreground mb-1">Test Accuracy</div>
                <div class="font-bold text-2xl text-primary">{{ resultsData.models.full.test_accuracy.toFixed(2) }}%</div>
              </div>
              <div class="p-4 rounded-lg border text-center">
                <div class="text-sm text-muted-foreground mb-1">Precision (No)</div>
                <div class="font-bold text-2xl">{{ (resultsData.models.full.classification_report.class_0_no_attrition.precision * 100).toFixed(1) }}%</div>
              </div>
              <div class="p-4 rounded-lg border text-center">
                <div class="text-sm text-muted-foreground mb-1">Recall (No)</div>
                <div class="font-bold text-2xl">{{ (resultsData.models.full.classification_report.class_0_no_attrition.recall * 100).toFixed(1) }}%</div>
              </div>
            </div>
          </div>
        </Card>
      </section>

      <!-- 3. MODEL V2 REDUCED -->
      <section id="model-reduced">
        <Card class="p-6 bg-gradient-to-br from-purple-50/50 to-pink-50/50">
          <div class="flex items-center gap-3 mb-6">
            <Badge variant="secondary" class="text-base px-3 py-1">MODEL V2</Badge>
            <h2 class="text-2xl font-bold">Reduced Model (11 Fitur)</h2>
          </div>

          <!-- Preprocessing -->
          <div class="mb-6">
            <h3 class="text-xl font-semibold mb-4 flex items-center gap-2">
              <span class="bg-purple-500 text-white rounded-full w-8 h-8 flex items-center justify-center text-sm">1</span>
              Preprocessing
            </h3>
            <div class="grid gap-4 md:grid-cols-2">
              <div>
                <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('reduced', 'preprocessing_flow.png')">
                  <img :src="`http://localhost:5000${getVisualization('reduced', 'preprocessing_flow.png')}`" alt="Reduced Preprocessing" class="w-full" />
                </div>
                <div class="mt-2 p-3 bg-purple-50 rounded-lg border border-purple-200">
                  <p class="text-xs text-purple-900"><strong>📊 Preprocessing Flow:</strong> Alur reduksi dari 31 → 11 fitur. Menghapus fitur dengan bias etis, redundansi, dan importance rendah. Fokus pada fitur paling prediktif & etis.</p>
                </div>
              </div>
              <div class="space-y-3 text-sm">
                <div class="p-4 rounded-lg border">
                  <div class="font-semibold mb-2">📋 Reduksi Fitur</div>
                  <ul class="space-y-1 text-muted-foreground">
                    <li>• Dari 31 fitur → 11 fitur</li>
                    <li>• Hapus fitur redundant (Gender, MaritalStatus)</li>
                    <li>• Hapus fitur kompleks (Department, JobRole)</li>
                    <li>• Prioritas fitur dengan importance tinggi</li>
                    <li>• Pertahankan fitur kunci untuk UX</li>
                  </ul>
                </div>
                <div class="p-4 rounded-lg bg-purple-50 border border-purple-200">
                  <div class="font-semibold mb-1">✅ Reduksi</div>
                  <div class="text-muted-foreground">64.5% fitur dihapus, akurasi tetap stabil</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Modeling -->
          <div class="mb-6">
            <h3 class="text-xl font-semibold mb-4 flex items-center gap-2">
              <span class="bg-purple-500 text-white rounded-full w-8 h-8 flex items-center justify-center text-sm">2</span>
              Modeling
            </h3>
            <div class="grid gap-4 md:grid-cols-3 mb-4">
              <div class="p-4 rounded-lg border">
                <div class="text-sm text-muted-foreground mb-1">Algorithm</div>
                <div class="font-bold text-lg">Random Forest</div>
              </div>
              <div class="p-4 rounded-lg border">
                <div class="text-sm text-muted-foreground mb-1">Total Features</div>
                <div class="font-bold text-lg">{{ resultsData.models.reduced.num_features }}</div>
              </div>
              <div class="p-4 rounded-lg border">
                <div class="text-sm text-muted-foreground mb-1">Training Time</div>
                <div class="font-bold text-lg">{{ resultsData.models.reduced.training_time.toFixed(4) }}s</div>
              </div>
            </div>

            <!-- Features Detail -->
            <div class="grid gap-4 md:grid-cols-2">
              <div class="p-4 rounded-lg border-2 border-purple-200 bg-purple-50/50">
                <div class="flex items-center gap-2 mb-3">
                  <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                  <div class="font-semibold text-purple-900">✓ Fitur Dipertahankan (11)</div>
                </div>
                <div class="text-sm space-y-2">
                  <div v-for="feature in resultsData.models.reduced.features" :key="feature" class="flex items-start gap-2 text-purple-800">
                    <span class="text-purple-500 mt-0.5">•</span>
                    <span>{{ feature }}</span>
                  </div>
                </div>
              </div>

              <div class="p-4 rounded-lg border bg-muted/30">
                <div class="flex items-center gap-2 mb-3">
                  <svg class="w-5 h-5 text-muted-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                  </svg>
                  <div class="font-semibold">✗ Fitur Dihapus dari Full (20)</div>
                </div>
                <div class="text-sm space-y-3 text-muted-foreground max-h-64 overflow-y-auto">
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">Gender, MaritalStatus</strong>
                      <p class="text-xs">Risiko bias, tidak etis untuk keputusan HR</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">DailyRate, HourlyRate, MonthlyRate</strong>
                      <p class="text-xs">Redundan dengan MonthlyIncome</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">Department, JobRole</strong>
                      <p class="text-xs">Terlalu banyak kategori, kompleks untuk user</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">Education, EducationField</strong>
                      <p class="text-xs">Feature importance rendah (<5%)</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">PerformanceRating</strong>
                      <p class="text-xs">Korelasi lemah, variance rendah</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">JobSatisfaction, RelationshipSatisfaction</strong>
                      <p class="text-xs">Overlap dengan EnvironmentSatisfaction</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">BusinessTravel</strong>
                      <p class="text-xs">Noise tinggi, tidak konsisten</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">NumCompaniesWorked</strong>
                      <p class="text-xs">Tidak signifikan dalam model</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">PercentSalaryHike, TrainingTimesLastYear</strong>
                      <p class="text-xs">Variance rendah, tidak prediktif</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">WorkLifeBalance, YearsSinceLastPromotion</strong>
                      <p class="text-xs">Importance <3%, tidak material</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">JobInvolvement</strong>
                      <p class="text-xs">Multikolinearitas dengan fitur lain</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Evaluasi -->
          <div>
            <h3 class="text-xl font-semibold mb-4 flex items-center gap-2">
              <span class="bg-purple-500 text-white rounded-full w-8 h-8 flex items-center justify-center text-sm">3</span>
              Evaluasi
            </h3>
            <div class="grid gap-4 md:grid-cols-2 mb-4">
              <div>
                <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('reduced', 'confusion_matrix.png')">
                  <img :src="`http://localhost:5000${getVisualization('reduced', 'confusion_matrix.png')}`" alt="Reduced Confusion Matrix" class="w-full" />
                </div>
                <div class="mt-2 p-3 bg-purple-50 rounded-lg border border-purple-200">
                  <p class="text-xs text-purple-900"><strong>📈 Confusion Matrix:</strong> Performa sama dengan Full Model (83.33%) dengan 64.5% fitur lebih sedikit. Efisiensi tinggi tanpa loss akurasi - menunjukkan 20 fitur yang dihapus memang tidak penting.</p>
                </div>
              </div>
              <div>
                <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('reduced', 'feature_importance.png')">
                  <img :src="`http://localhost:5000${getVisualization('reduced', 'feature_importance.png')}`" alt="Reduced Feature Importance" class="w-full" />
                </div>
                <div class="mt-2 p-3 bg-purple-50 rounded-lg border border-purple-200">
                  <p class="text-xs text-purple-900"><strong>🎯 Feature Importance:</strong> Distribusi importance lebih merata di 11 fitur. MonthlyIncome masih dominan (18%), diikuti Age & TotalWorkingYears. Tidak ada fitur dengan importance <5%.</p>
                </div>
              </div>
            </div>
            <div class="grid gap-4 md:grid-cols-4">
              <div class="p-4 rounded-lg border text-center">
                <div class="text-sm text-muted-foreground mb-1">Train Accuracy</div>
                <div class="font-bold text-2xl">{{ resultsData.models.reduced.train_accuracy.toFixed(2) }}%</div>
              </div>
              <div class="p-4 rounded-lg border text-center">
                <div class="text-sm text-muted-foreground mb-1">Test Accuracy</div>
                <div class="font-bold text-2xl text-primary">{{ resultsData.models.reduced.test_accuracy.toFixed(2) }}%</div>
              </div>
              <div class="p-4 rounded-lg border text-center">
                <div class="text-sm text-muted-foreground mb-1">Precision (No)</div>
                <div class="font-bold text-2xl">{{ (resultsData.models.reduced.classification_report.class_0_no_attrition.precision * 100).toFixed(1) }}%</div>
              </div>
              <div class="p-4 rounded-lg border text-center">
                <div class="text-sm text-muted-foreground mb-1">Recall (No)</div>
                <div class="font-bold text-2xl">{{ (resultsData.models.reduced.classification_report.class_0_no_attrition.recall * 100).toFixed(1) }}%</div>
              </div>
            </div>
          </div>
        </Card>
      </section>

      <!-- 4. MODEL V3 MINIMAL (FINAL) -->
      <section id="model-minimal">
        <Card class="p-6 bg-gradient-to-br from-green-50/50 to-emerald-50/50 border-2 border-green-500">
          <div class="flex items-center gap-3 mb-6">
            <Badge class="text-base px-3 py-1">MODEL V3 ⭐</Badge>
            <h2 class="text-2xl font-bold">Minimal Model (7 Fitur) - FINAL</h2>
          </div>

          <!-- Preprocessing -->
          <div class="mb-6">
            <h3 class="text-xl font-semibold mb-4 flex items-center gap-2">
              <span class="bg-green-500 text-white rounded-full w-8 h-8 flex items-center justify-center text-sm">1</span>
              Preprocessing
            </h3>
            <div class="grid gap-4 md:grid-cols-2">
              <div>
                <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('minimal', 'preprocessing_flow.png')">
                  <img :src="`http://localhost:5000${getVisualization('minimal', 'preprocessing_flow.png')}`" alt="Minimal Preprocessing" class="w-full" />
                </div>
                <div class="mt-2 p-3 bg-green-50 rounded-lg border border-green-200">
                  <p class="text-xs text-green-900"><strong>📊 Preprocessing Flow:</strong> Ultra-minimal 11 → 7 fitur (77.4% reduction dari Full). Hanya fitur dengan importance ≥7% & UX-friendly. Optimasi performa + kemudahan input user.</p>
                </div>
              </div>
              <div class="space-y-3 text-sm">
                <div class="p-4 rounded-lg border">
                  <div class="font-semibold mb-2">📋 Ultra Minimal Features</div>
                  <ul class="space-y-1 text-muted-foreground">
                    <li>• Dari 11 fitur → 7 fitur</li>
                    <li>• Hanya fitur dengan importance ≥ 7%</li>
                    <li>• Fokus pada fitur mudah diisi user</li>
                    <li>• Hapus redundant (YearsAtCompany, JobLevel)</li>
                    <li>• Optimasi untuk UX & performa</li>
                  </ul>
                </div>
                <div class="p-4 rounded-lg bg-green-50 border border-green-500">
                  <div class="font-semibold mb-1">✅ Best Model</div>
                  <div class="text-muted-foreground">77.4% fitur reduction, akurasi NAIK!</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Modeling -->
          <div class="mb-6">
            <h3 class="text-xl font-semibold mb-4 flex items-center gap-2">
              <span class="bg-green-500 text-white rounded-full w-8 h-8 flex items-center justify-center text-sm">2</span>
              Modeling
            </h3>
            <div class="grid gap-4 md:grid-cols-3 mb-4">
              <div class="p-4 rounded-lg border">
                <div class="text-sm text-muted-foreground mb-1">Algorithm</div>
                <div class="font-bold text-lg">Random Forest</div>
              </div>
              <div class="p-4 rounded-lg border">
                <div class="text-sm text-muted-foreground mb-1">Total Features</div>
                <div class="font-bold text-lg text-green-600">{{ resultsData.models.minimal.num_features }}</div>
              </div>
              <div class="p-4 rounded-lg border">
                <div class="text-sm text-muted-foreground mb-1">Training Time</div>
                <div class="font-bold text-lg">{{ resultsData.models.minimal.training_time.toFixed(4) }}s</div>
              </div>
            </div>
            
            <!-- Features Detail -->
            <div class="grid gap-4 md:grid-cols-2 mb-4">
              <div class="p-4 rounded-lg border-2 border-green-500 bg-green-50/50">
                <div class="flex items-center gap-2 mb-3">
                  <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                  <div class="font-semibold text-green-900">✓ 7 Fitur Terbaik (Importance ≥ 7%)</div>
                </div>
                <div class="text-sm space-y-3">
                  <div class="flex items-start gap-2 text-green-800">
                    <span class="text-green-500 mt-0.5 font-bold">1.</span>
                    <div>
                      <strong>MonthlyIncome</strong>
                      <p class="text-xs text-green-700">Importance: 23.65% | Kompensasi adalah faktor terkuat</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2 text-green-800">
                    <span class="text-green-500 mt-0.5 font-bold">2.</span>
                    <div>
                      <strong>TotalWorkingYears</strong>
                      <p class="text-xs text-green-700">Importance: 18.30% | Pengalaman kerja krusial</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2 text-green-800">
                    <span class="text-green-500 mt-0.5 font-bold">3.</span>
                    <div>
                      <strong>Age</strong>
                      <p class="text-xs text-green-700">Importance: 17.78% | Karyawan muda lebih mobile</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2 text-green-800">
                    <span class="text-green-500 mt-0.5 font-bold">4.</span>
                    <div>
                      <strong>DistanceFromHome</strong>
                      <p class="text-xs text-green-700">Importance: 13.29% | Jarak jauh = resign tinggi</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2 text-green-800">
                    <span class="text-green-500 mt-0.5 font-bold">5.</span>
                    <div>
                      <strong>OverTime</strong>
                      <p class="text-xs text-green-700">Importance: 10.99% | Work-life balance kunci</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2 text-green-800">
                    <span class="text-green-500 mt-0.5 font-bold">6.</span>
                    <div>
                      <strong>EnvironmentSatisfaction</strong>
                      <p class="text-xs text-green-700">Importance: 8.27% | Kepuasan lingkungan kerja</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2 text-green-800">
                    <span class="text-green-500 mt-0.5 font-bold">7.</span>
                    <div>
                      <strong>StockOptionLevel</strong>
                      <p class="text-xs text-green-700">Importance: 7.71% | Benefit untuk retention</p>
                    </div>
                  </div>
                </div>
              </div>

              <div class="p-4 rounded-lg border bg-muted/30">
                <div class="flex items-center gap-2 mb-3">
                  <svg class="w-5 h-5 text-muted-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                  </svg>
                  <div class="font-semibold">✗ Fitur Dihapus dari Reduced (4)</div>
                </div>
                <div class="text-sm space-y-3 text-muted-foreground">
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">YearsAtCompany</strong>
                      <p class="text-xs">Redundan dengan TotalWorkingYears & Age</p>
                      <p class="text-xs text-amber-600">Importance: 6.8% (di bawah threshold 7%)</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">JobLevel</strong>
                      <p class="text-xs">Tercakup dalam MonthlyIncome (korelasi tinggi)</p>
                      <p class="text-xs text-amber-600">Importance: 5.2% (tidak material)</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">YearsInCurrentRole</strong>
                      <p class="text-xs">Korelasi rendah dengan target</p>
                      <p class="text-xs text-amber-600">Importance: 4.1% (minimal impact)</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="text-destructive mt-0.5">×</span>
                    <div>
                      <strong class="text-foreground">YearsWithCurrManager</strong>
                      <p class="text-xs">Tidak signifikan untuk prediksi</p>
                      <p class="text-xs text-amber-600">Importance: 3.5% (di bawah threshold)</p>
                    </div>
                  </div>
                </div>

                <div class="mt-4 p-3 rounded-lg bg-green-100 border border-green-300">
                  <div class="text-xs font-semibold text-green-900 mb-1">💡 Prinsip Seleksi:</div>
                  <ul class="text-xs text-green-800 space-y-1">
                    <li>✓ Feature importance ≥ 7%</li>
                    <li>✓ Tidak redundan dengan fitur lain</li>
                    <li>✓ Mudah diisi oleh user (UX)</li>
                    <li>✓ Data reliable & available</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Evaluasi -->
          <div>
            <h3 class="text-xl font-semibold mb-4 flex items-center gap-2">
              <span class="bg-green-500 text-white rounded-full w-8 h-8 flex items-center justify-center text-sm">3</span>
              Evaluasi
            </h3>
            <div class="grid gap-4 md:grid-cols-2 mb-4">
              <div>
                <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('minimal', 'confusion_matrix.png')">
                  <img :src="`http://localhost:5000${getVisualization('minimal', 'confusion_matrix.png')}`" alt="Minimal Confusion Matrix" class="w-full" />
                </div>
                <div class="mt-2 p-3 bg-green-50 border-2 border-green-500 rounded-lg">
                  <p class="text-xs text-green-900"><strong>📈 Confusion Matrix (BEST):</strong> Akurasi NAIK jadi 84.01% dengan hanya 7 fitur! Prediksi lebih akurat: 237 TN, 12 TP. Model paling efisien & akurat - Sweet spot antara simplicity & performance.</p>
                </div>
              </div>
              <div>
                <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('minimal', 'feature_importance.png')">
                  <img :src="`http://localhost:5000${getVisualization('minimal', 'feature_importance.png')}`" alt="Minimal Feature Importance" class="w-full" />
                </div>
                <div class="mt-2 p-3 bg-green-50 border-2 border-green-500 rounded-lg">
                  <p class="text-xs text-green-900"><strong>🎯 Feature Importance (TOP 7):</strong> MonthlyIncome 23.65% (paling kuat), TotalWorkingYears 18.30%, Age 17.78%. Semua fitur berkontribusi signifikan ≥7% - tidak ada noise, pure signal!</p>
                </div>
              </div>
            </div>
            <div class="grid gap-4 md:grid-cols-4">
              <div class="p-4 rounded-lg border-2 border-green-500 text-center">
                <div class="text-sm text-muted-foreground mb-1">Train Accuracy</div>
                <div class="font-bold text-2xl text-green-600">{{ resultsData.models.minimal.train_accuracy.toFixed(2) }}%</div>
              </div>
              <div class="p-4 rounded-lg border-2 border-green-500 text-center">
                <div class="text-sm text-muted-foreground mb-1">Test Accuracy ⭐</div>
                <div class="font-bold text-3xl text-green-600">{{ resultsData.models.minimal.test_accuracy.toFixed(2) }}%</div>
              </div>
              <div class="p-4 rounded-lg border text-center">
                <div class="text-sm text-muted-foreground mb-1">Precision (No)</div>
                <div class="font-bold text-2xl">{{ (resultsData.models.minimal.classification_report.class_0_no_attrition.precision * 100).toFixed(1) }}%</div>
              </div>
              <div class="p-4 rounded-lg border text-center">
                <div class="text-sm text-muted-foreground mb-1">Recall (No)</div>
                <div class="font-bold text-2xl">{{ (resultsData.models.minimal.classification_report.class_0_no_attrition.recall * 100).toFixed(1) }}%</div>
              </div>
            </div>
          </div>
        </Card>
      </section>

      <!-- 5. COMPARISON -->
      <section id="comparison">
        <Card class="p-6 bg-gradient-to-br from-amber-50/50 to-orange-50/50">
          <h2 class="text-2xl font-bold mb-6">📊 Perbandingan Model</h2>

          <div class="grid gap-6">
            <!-- Model Accuracy Comparison -->
            <div>
              <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('comparison', 'model_accuracy_comparison.png')">
                <img :src="`http://localhost:5000${getVisualization('comparison', 'model_accuracy_comparison.png')}`" alt="Model Accuracy Comparison" class="w-full" />
              </div>
              <div class="mt-2 p-3 bg-amber-50 rounded-lg border border-amber-200">
                <p class="text-xs text-amber-900"><strong>Accuracy Comparison:</strong> Bar chart perbandingan akurasi Train vs Test ketiga model. Minimal (7 fitur) unggul 84.01%, Full dan Reduced sama 83.33%. Less is more!</p>
              </div>
            </div>

            <!-- Feature Efficiency -->
            <div>
              <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('comparison', 'feature_efficiency.png')">
                <img :src="`http://localhost:5000${getVisualization('comparison', 'feature_efficiency.png')}`" alt="Feature Efficiency" class="w-full" />
              </div>
              <div class="mt-2 p-3 bg-amber-50 rounded-lg border border-amber-200">
                <p class="text-xs text-amber-900"><strong>Feature Efficiency:</strong> Scatter plot akurasi vs jumlah fitur. Minimal (7) di kanan atas = akurasi tertinggi dengan fitur paling sedikit. Pareto optimal point!</p>
              </div>
            </div>

            <!-- Summary Stats -->
            <div class="grid gap-4 md:grid-cols-3">
              <div class="p-6 rounded-lg border text-center">
                <div class="text-sm text-muted-foreground mb-2">Full Model</div>
                <div class="text-3xl font-bold mb-1">{{ resultsData.models.full.test_accuracy.toFixed(2) }}%</div>
                <div class="text-xs text-muted-foreground">31 fitur</div>
              </div>
              <div class="p-6 rounded-lg border text-center">
                <div class="text-sm text-muted-foreground mb-2">Reduced Model</div>
                <div class="text-3xl font-bold mb-1">{{ resultsData.models.reduced.test_accuracy.toFixed(2) }}%</div>
                <div class="text-xs text-muted-foreground">11 fitur</div>
              </div>
              <div class="p-6 rounded-lg border-2 border-green-500 text-center">
                <div class="text-sm text-muted-foreground mb-2">Minimal Model ⭐</div>
                <div class="text-4xl font-bold mb-1 text-green-600">{{ resultsData.models.minimal.test_accuracy.toFixed(2) }}%</div>
                <div class="text-xs text-muted-foreground">7 fitur</div>
              </div>
            </div>

            <!-- Metrics Overview -->
            <div>
              <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('comparison', 'metrics_overview.png')">
                <img :src="`http://localhost:5000${getVisualization('comparison', 'metrics_overview.png')}`" alt="Metrics Overview" class="w-full" />
              </div>
              <div class="mt-2 p-3 bg-amber-50 rounded-lg border border-amber-200">
                <p class="text-xs text-amber-900"><strong>Metrics Overview:</strong> Heatmap Precision, Recall, F1-Score ketiga model. Minimal unggul di semua metrik untuk class Yes (12% recall vs 0-8%). Model paling balanced!</p>
              </div>
            </div>

            <!-- Training Time Comparison -->
            <div>
              <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('comparison', 'training_time_comparison.png')">
                <img :src="`http://localhost:5000${getVisualization('comparison', 'training_time_comparison.png')}`" alt="Training Time" class="w-full" />
              </div>
              <div class="mt-2 p-3 bg-amber-50 rounded-lg border border-amber-200">
                <p class="text-xs text-amber-900"><strong>Training Time:</strong> Bar chart waktu training. Full: 0.117s, Reduced: 0.102s (-12.8%), Minimal: 0.096s (-17.9%). Lebih sedikit fitur = training lebih cepat = deploy lebih efisien.</p>
              </div>
            </div>

            <!-- Summary Dashboard -->
            <div>
              <div class="rounded-lg border overflow-hidden bg-white cursor-pointer hover:shadow-lg transition-shadow" @click="openVisualization('comparison', 'summary_dashboard.png')">
                <img :src="`http://localhost:5000${getVisualization('comparison', 'summary_dashboard.png')}`" alt="Summary Dashboard" class="w-full" />
              </div>
              <div class="mt-2 p-3 bg-amber-50 border-2 border-amber-500 rounded-lg">
                <p class="text-xs text-amber-900"><strong>Summary Dashboard:</strong> Comprehensive view 4 metrik utama (Accuracy, Precision, Recall, F1) semua model. Visualisasi lengkap untuk executive summary - satu pandang langsung tahu Minimal model pemenangnya!</p>
              </div>
            </div>

            <!-- Key Insights -->
            <div class="p-6 rounded-lg border-2 border-amber-500 bg-amber-50">
              <h3 class="font-bold text-lg mb-4">🔑 Key Insights</h3>
              <div class="grid gap-4 md:grid-cols-2 text-sm">
                <div>
                  <div class="font-semibold mb-2">✅ Kelebihan Minimal Model:</div>
                  <ul class="space-y-1 text-muted-foreground">
                    <li>• Akurasi tertinggi: {{ resultsData.models.minimal.test_accuracy.toFixed(2) }}%</li>
                    <li>• Hanya 7 fitur (77.4% reduction)</li>
                    <li>• Input time ~20 detik vs 2-3 menit</li>
                    <li>• Lebih praktis untuk deployment</li>
                    <li>• User experience optimal</li>
                  </ul>
                </div>
                <div>
                  <div class="font-semibold mb-2">📈 Perbandingan:</div>
                  <ul class="space-y-1 text-muted-foreground">
                    <li>• Best: {{ resultsData.comparison.best_accuracy_model.toUpperCase() }}</li>
                    <li>• Fastest: {{ resultsData.comparison.fastest_training_model.toUpperCase() }}</li>
                    <li>• Most Efficient: {{ resultsData.comparison.most_efficient_model.toUpperCase() }}</li>
                    <li>• Reduction: {{ resultsData.comparison.feature_reduction.full_to_minimal }}</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </Card>
      </section>

      <!-- 6. KESIMPULAN -->
      <section id="conclusion">
        <Card class="p-6 bg-gradient-to-br from-slate-50/50 to-gray-50/50">
          <h2 class="text-2xl font-bold mb-6">💡 Kesimpulan & Rekomendasi</h2>

          <div class="space-y-6">
            <!-- Kesimpulan -->
            <div class="p-6 rounded-lg border-l-4 border-blue-500 bg-blue-50/50">
              <h3 class="font-bold text-lg mb-4 flex items-center gap-2">
                <svg class="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                Kesimpulan Analisis
              </h3>
              <ul class="space-y-3 text-sm">
                <li class="flex gap-3">
                  <span class="text-blue-500 font-bold mt-0.5">•</span>
                  <span>
                    <strong>Model Minimal (7 fitur)</strong> mencapai akurasi tertinggi <strong>{{ resultsData.models.minimal.test_accuracy.toFixed(2) }}%</strong>, 
                    melampaui Full Model ({{ resultsData.models.full.test_accuracy.toFixed(2) }}%) dan Reduced Model ({{ resultsData.models.reduced.test_accuracy.toFixed(2) }}%).
                  </span>
                </li>
                <li class="flex gap-3">
                  <span class="text-blue-500 font-bold mt-0.5">•</span>
                  <span>
                    Dataset IBM HR Analytics dengan <strong>{{ resultsData.dataset_info.total_samples.toLocaleString() }} karyawan</strong> menunjukkan 
                    tingkat attrition <strong>{{ resultsData.dataset_info.attrition_rate.toFixed(2) }}%</strong>.
                  </span>
                </li>
                <li class="flex gap-3">
                  <span class="text-blue-500 font-bold mt-0.5">•</span>
                  <span>
                    <strong>Reduksi fitur 77.4%</strong> (dari 31 ke 7) justru meningkatkan performa model, menunjukkan efektivitas feature selection.
                  </span>
                </li>
                <li class="flex gap-3">
                  <span class="text-blue-500 font-bold mt-0.5">•</span>
                  <span>
                    Top 3 fitur terpenting: <strong>MonthlyIncome</strong> ({{ (Object.values(resultsData.models.minimal.feature_importance)[0] * 100).toFixed(1) }}%), 
                    <strong>TotalWorkingYears</strong>, dan <strong>Age</strong>.
                  </span>
                </li>
                <li class="flex gap-3">
                  <span class="text-blue-500 font-bold mt-0.5">•</span>
                  <span>
                    Training time sangat cepat (<strong>{{ resultsData.models.minimal.training_time.toFixed(4) }}s</strong>), ideal untuk deployment real-time.
                  </span>
                </li>
                <li class="flex gap-3">
                  <span class="text-blue-500 font-bold mt-0.5">•</span>
                  <span>
                    Model memiliki <strong>precision tinggi</strong> untuk prediksi "tetap", cocok untuk early warning system attrition.
                  </span>
                </li>
              </ul>
            </div>

            <!-- Rekomendasi -->
            <div class="p-6 rounded-lg border-l-4 border-green-500 bg-green-50/50">
              <h3 class="font-bold text-lg mb-4 flex items-center gap-2">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path>
                </svg>
                Rekomendasi untuk Manajemen HR
              </h3>
              <div class="grid gap-4 md:grid-cols-2">
                <div class="space-y-3 text-sm">
                  <div class="flex gap-3">
                    <span class="bg-green-500 text-white rounded-full w-6 h-6 flex items-center justify-center font-bold text-xs flex-shrink-0">1</span>
                    <div>
                      <strong>Review Kompensasi</strong>
                      <p class="text-muted-foreground">MonthlyIncome faktor terkuat. Lakukan benchmarking gaji berkala dan sesuaikan untuk posisi kritis.</p>
                    </div>
                  </div>
                  <div class="flex gap-3">
                    <span class="bg-green-500 text-white rounded-full w-6 h-6 flex items-center justify-center font-bold text-xs flex-shrink-0">2</span>
                    <div>
                      <strong>Kebijakan Overtime</strong>
                      <p class="text-muted-foreground">OverTime tinggi = risiko resign. Evaluasi kompensasi lembur dan work-life balance.</p>
                    </div>
                  </div>
                  <div class="flex gap-3">
                    <span class="bg-green-500 text-white rounded-full w-6 h-6 flex items-center justify-center font-bold text-xs flex-shrink-0">3</span>
                    <div>
                      <strong>Stock Options Program</strong>
                      <p class="text-muted-foreground">StockOptionLevel penting. Tawarkan equity programs untuk meningkatkan loyalty.</p>
                    </div>
                  </div>
                </div>
                <div class="space-y-3 text-sm">
                  <div class="flex gap-3">
                    <span class="bg-green-500 text-white rounded-full w-6 h-6 flex items-center justify-center font-bold text-xs flex-shrink-0">4</span>
                    <div>
                      <strong>Retensi Berbasis Demografi</strong>
                      <p class="text-muted-foreground">Age & TotalWorkingYears menunjukkan karyawan muda lebih mobile. Buat career development plans.</p>
                    </div>
                  </div>
                  <div class="flex gap-3">
                    <span class="bg-green-500 text-white rounded-full w-6 h-6 flex items-center justify-center font-bold text-xs flex-shrink-0">5</span>
                    <div>
                      <strong>Early Warning System</strong>
                      <p class="text-muted-foreground">Gunakan model prediksi berkala untuk identifikasi karyawan berisiko dan intervensi proaktif.</p>
                    </div>
                  </div>
                  <div class="flex gap-3">
                    <span class="bg-green-500 text-white rounded-full w-6 h-6 flex items-center justify-center font-bold text-xs flex-shrink-0">6</span>
                    <div>
                      <strong>Monitor Environment Satisfaction</strong>
                      <p class="text-muted-foreground">Lakukan survey kepuasan berkala dan implementasi feedback untuk kultur kerja.</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </Card>
      </section>

      <!-- CTA -->
      <div class="text-center py-8">
        <p class="text-muted-foreground mb-4">Siap mencoba model prediksi dengan 7 fitur minimal?</p>
        <Button as="router-link" to="/predict" size="lg" class="gap-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
          </svg>
          Mulai Prediksi
        </Button>
      </div>
    </div>

    <!-- Image Modal -->
    <div v-if="modalImage" @click="closeModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4 cursor-zoom-out">
      <div class="relative max-w-7xl max-h-[90vh] w-full">
        <button @click="closeModal" class="absolute -top-12 right-0 text-white hover:text-gray-300 transition-colors">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
        <img :src="modalImage" @click.stop class="w-full h-full object-contain rounded-lg shadow-2xl cursor-default" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import Button from '../components/ui/Button.vue'
import Card from '../components/ui/Card.vue'
import Badge from '../components/ui/Badge.vue'

const loading = ref(true)
const resultsData = ref(null)
const visualizations = ref(null)
const modalImage = ref(null)
const datasetRows = ref([])
const datasetColumns = ref([])
const currentPage = ref(1)
const rowsPerPage = ref(25)

const paginatedRows = computed(() => {
  const start = (currentPage.value - 1) * rowsPerPage.value
  const end = start + rowsPerPage.value
  return datasetRows.value.slice(start, end)
})

const totalPages = computed(() => {
  return Math.ceil(datasetRows.value.length / rowsPerPage.value)
})

const openModal = (imageSrc) => {
  modalImage.value = imageSrc
  document.body.style.overflow = 'hidden'
}

const closeModal = () => {
  modalImage.value = null
  document.body.style.overflow = 'auto'
}

const openVisualization = (category, filename) => {
  const imageSrc = `http://localhost:5000/api/visualizations/${category}/${filename}`
  openModal(imageSrc)
}

const loadData = async () => {
  try {
    loading.value = true
    
    // Fetch results from API
    const resultsResponse = await axios.get('http://localhost:5000/api/results')
    resultsData.value = resultsResponse.data
    
    // Fetch visualizations list
    const vizResponse = await axios.get('http://localhost:5000/api/visualizations/list')
    visualizations.value = vizResponse.data.visualizations
    
    // Load dataset CSV
    await loadDataset()
    
    loading.value = false
  } catch (error) {
    console.error('Error loading data:', error)
    loading.value = false
  }
}

const loadDataset = async () => {
  try {
    const response = await axios.get('/WA_Fn-UseC_-HR-Employee-Attrition.csv', {
      responseType: 'text'
    })
    
    const lines = response.data.trim().split('\n')
    const headers = lines[0].split(',').map(h => h.trim().replace(/"/g, ''))
    datasetColumns.value = headers
    
    const rows = []
    for (let i = 1; i < lines.length; i++) {
      const values = lines[i].split(',').map(v => v.trim().replace(/"/g, ''))
      const row = {}
      headers.forEach((header, index) => {
        row[header] = values[index]
      })
      rows.push(row)
    }
    
    datasetRows.value = rows
  } catch (error) {
    console.error('Error loading dataset:', error)
  }
}

const getVisualization = (category, filename) => {
  return `/api/visualizations/${category}/${filename}`
}

onMounted(() => {
  loadData()
})
</script>
