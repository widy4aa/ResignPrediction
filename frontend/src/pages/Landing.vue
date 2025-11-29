<template>
  <div class="min-h-screen bg-background">
    <!-- Minimal Header -->
    <header class="border-b">
      <div class="container flex h-16 items-center justify-between">
        <div class="flex items-center space-x-2">
          <div class="flex h-9 w-9 items-center justify-center rounded-md bg-primary text-primary-foreground">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 3v18h18"/>
              <path d="m19 9-5 5-4-4-3 3"/>
            </svg>
          </div>
          <span class="text-lg font-semibold">Attrition Predictor</span>
        </div>
        <nav class="flex items-center space-x-6">
        </nav>
      </div>
    </header>

    <!-- Hero Section -->
    <section class="container py-24 md:py-32">
      <div class="mx-auto max-w-3xl text-center">
        <div class="mb-6 inline-flex items-center rounded-full border px-3 py-1 text-sm">
          <span class="h-1.5 w-1.5 rounded-full bg-green-500 mr-2"></span>
          Model Accuracy: 84.01%
        </div>
        
        <h1 class="text-4xl font-bold tracking-tight sm:text-6xl mb-6">
          Employee Attrition
          <span class="block text-muted-foreground">Prediction System</span>
        </h1>
        
        <p class="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto">
          Machine learning model untuk memprediksi kemungkinan karyawan resign menggunakan IBM HR Analytics Dataset
        </p>
        
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <Button as="router-link" to="/predict" size="lg" class="gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"/>
              <polygon points="10 8 16 12 10 16 10 8"/>
            </svg>
            Mulai Prediksi
          </Button>
          <Button as="router-link" to="/insight" variant="outline" size="lg" class="gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" x2="12" y1="20" y2="10"/>
              <line x1="18" x2="18" y1="20" y2="4"/>
              <line x1="6" x2="6" y1="20" y2="16"/>
            </svg>
            Lihat Insight
          </Button>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="border-y bg-muted/50">
      <div class="container py-12">
        <div class="grid gap-8 md:grid-cols-3">
          <div class="text-center">
            <div class="text-3xl font-bold mb-2">{{ stats.accuracy }}%</div>
            <div class="text-sm text-muted-foreground">Model Accuracy</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold mb-2">{{ stats.samples }}</div>
            <div class="text-sm text-muted-foreground">Dataset Samples</div>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold mb-2">{{ stats.features }}</div>
            <div class="text-sm text-muted-foreground">Minimal Features</div>
          </div>
        </div>
      </div>
    </section>
  
    <!-- Footer -->
    <footer class="border-t">
      <div class="container py-8">
        <div class="text-center text-sm text-muted-foreground">
          <p class="mb-1">IBM HR Analytics - Employee Attrition Prediction</p>
          <p>Powered by Random Forest Classifier & Vue.js</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Button from '../components/ui/Button.vue'
import Card from '../components/ui/Card.vue'
import { API_ENDPOINTS } from '../config/api.js'

const featuresSection = ref(null)
const stats = ref({
  accuracy: '84.01',
  samples: '1470',
  features: '7'
})

const scrollToFeatures = () => {
  featuresSection.value?.scrollIntoView({ behavior: 'smooth' })
}

const fetchStats = async () => {
  try {
    const response = await axios.get(API_ENDPOINTS.summary)
    const data = response.data
    
    stats.value = {
      accuracy: data.models_summary.minimal.test_accuracy.toFixed(2),
      samples: data.dataset_info.total_samples,
      features: data.models_summary.minimal.features
    }
  } catch (error) {
    console.error('Error fetching stats:', error)
    // Keep default values
  }
}

onMounted(() => {
  fetchStats()
})
</script>
