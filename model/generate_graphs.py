"""
Generate visualization graphs from hasil.json
Creates comparison charts for Full, Reduced, and Minimal models
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

# Create img folders if not exists
for folder in ['img', 'img/full', 'img/reduced', 'img/minimal', 'img/comparison']:
    if not os.path.exists(folder):
        os.makedirs(folder)

print("="*80)
print("GENERATING VISUALIZATION GRAPHS")
print("="*80)

# Load hasil.json
print("\n📂 Loading hasil.json...")
with open('hasil.json', 'r', encoding='utf-8') as f:
    results = json.load(f)

print("✅ Data loaded successfully")

# Extract data
models = results['models']
model_names = ['Full', 'Reduced', 'Minimal']
num_features = [models['full']['num_features'], 
                models['reduced']['num_features'], 
                models['minimal']['num_features']]
test_accuracy = [models['full']['test_accuracy'], 
                 models['reduced']['test_accuracy'], 
                 models['minimal']['test_accuracy']]
train_accuracy = [models['full']['train_accuracy'], 
                  models['reduced']['train_accuracy'], 
                  models['minimal']['train_accuracy']]
training_time = [models['full']['training_time'], 
                 models['reduced']['training_time'], 
                 models['minimal']['training_time']]

# ============================================================================
# GRAPH 1: Model Comparison - Accuracy
# ============================================================================
print("\n🎨 Creating Graph 1: Perbandingan Akurasi Model...")
fig, ax = plt.subplots(figsize=(12, 7))

x = np.arange(len(model_names))
width = 0.35

bars1 = ax.bar(x - width/2, train_accuracy, width, label='Akurasi Training', 
               color='#4ECDC4', edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x + width/2, test_accuracy, width, label='Akurasi Testing', 
               color='#FF6B6B', edgecolor='black', linewidth=1.5)

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}%',
                ha='center', va='bottom', fontweight='bold', fontsize=10)

ax.set_xlabel('Versi Model', fontsize=13, fontweight='bold')
ax.set_ylabel('Akurasi (%)', fontsize=13, fontweight='bold')
ax.set_title('Perbandingan Performa Model\nAkurasi Training vs Testing', 
             fontsize=15, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels([f'{name}\n({feat} fitur)' for name, feat in zip(model_names, num_features)])
ax.legend(fontsize=11, loc='lower right')
ax.set_ylim(75, 95)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('img/comparison/model_accuracy_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: img/comparison/model_accuracy_comparison.png")

# ============================================================================
# GRAPH 2: Feature Count vs Accuracy
# ============================================================================
print("\n🎨 Creating Graph 2: Efisiensi Fitur...")
fig, ax = plt.subplots(figsize=(12, 7))

colors = ['#FF6B6B', '#FFA500', '#4ECDC4']
scatter = ax.scatter(num_features, test_accuracy, s=500, c=colors, 
                     alpha=0.6, edgecolors='black', linewidth=2)

# Add labels for each point
for i, (x, y, name) in enumerate(zip(num_features, test_accuracy, model_names)):
    ax.annotate(f'{name}\n{y:.2f}%', 
                xy=(x, y), 
                xytext=(0, 15 if i != 1 else -25),
                textcoords='offset points',
                ha='center',
                fontsize=11,
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor=colors[i], alpha=0.3))

ax.plot(num_features, test_accuracy, 'k--', alpha=0.3, linewidth=2)

ax.set_xlabel('Jumlah Fitur', fontsize=13, fontweight='bold')
ax.set_ylabel('Akurasi Testing (%)', fontsize=13, fontweight='bold')
ax.set_title('Analisis Efisiensi Fitur\nAkurasi vs Jumlah Fitur', 
             fontsize=15, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3)
ax.set_ylim(82, 85)

# Add annotation for best model
best_idx = test_accuracy.index(max(test_accuracy))
ax.annotate('Performa Terbaik', 
            xy=(num_features[best_idx], test_accuracy[best_idx]),
            xytext=(15, -30),
            textcoords='offset points',
            fontsize=10,
            color='green',
            fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='green', lw=2))

plt.tight_layout()
plt.savefig('img/comparison/feature_efficiency.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: img/comparison/feature_efficiency.png")

# ============================================================================
# GRAPH 3: Training Time Comparison
# ============================================================================
print("\n🎨 Creating Graph 3: Perbandingan Waktu Training...")
fig, ax = plt.subplots(figsize=(10, 7))

bars = ax.barh(model_names, training_time, color=colors, 
               edgecolor='black', linewidth=2)

# Add value labels
for i, (bar, time) in enumerate(zip(bars, training_time)):
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height()/2,
            f' {time:.4f} detik',
            ha='left', va='center', fontweight='bold', fontsize=11)

ax.set_xlabel('Waktu Training (detik)', fontsize=13, fontweight='bold')
ax.set_ylabel('Versi Model', fontsize=13, fontweight='bold')
ax.set_title('Perbandingan Waktu Training Model', 
             fontsize=15, fontweight='bold', pad=20)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('img/comparison/training_time_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: img/comparison/training_time_comparison.png")

# ============================================================================
# GRAPH 4: Confusion Matrix Comparison
# ============================================================================
print("\n🎨 Creating Graph 4: Perbandingan Confusion Matrix...")
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

for idx, (model_name, ax) in enumerate(zip(['full', 'reduced', 'minimal'], axes)):
    cm = models[model_name]['confusion_matrix']
    cm_matrix = np.array([
        [cm['true_negative'], cm['false_positive']],
        [cm['false_negative'], cm['true_positive']]
    ])
    
    sns.heatmap(cm_matrix, annot=True, fmt='d', cmap='Blues', 
                cbar=True, ax=ax, linewidths=2, linecolor='black',
                annot_kws={'fontsize': 14, 'fontweight': 'bold'})
    
    ax.set_title(f'Model {model_names[idx]}\n({num_features[idx]} fitur)', 
                 fontsize=13, fontweight='bold', pad=10)
    ax.set_xlabel('Prediksi', fontsize=11, fontweight='bold')
    ax.set_ylabel('Aktual', fontsize=11, fontweight='bold')
    ax.set_xticklabels(['Tidak Resign', 'Resign'])
    ax.set_yticklabels(['Tidak Resign', 'Resign'])

plt.suptitle('Perbandingan Confusion Matrix - Semua Model', 
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('img/comparison/confusion_matrix_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: img/comparison/confusion_matrix_comparison.png")

# Also save individual confusion matrices
print("\n🎨 Creating individual Confusion Matrix for each model...")
for idx, model_name in enumerate(['full', 'reduced', 'minimal']):
    fig, ax = plt.subplots(figsize=(8, 6))
    cm = models[model_name]['confusion_matrix']
    cm_matrix = np.array([
        [cm['true_negative'], cm['false_positive']],
        [cm['false_negative'], cm['true_positive']]
    ])
    
    sns.heatmap(cm_matrix, annot=True, fmt='d', cmap='Blues', 
                cbar=True, ax=ax, linewidths=2, linecolor='black',
                annot_kws={'fontsize': 16, 'fontweight': 'bold'})
    
    ax.set_title(f'Confusion Matrix - Model {model_names[idx]}\n({num_features[idx]} fitur)', 
                 fontsize=14, fontweight='bold', pad=10)
    ax.set_xlabel('Prediksi', fontsize=12, fontweight='bold')
    ax.set_ylabel('Aktual', fontsize=12, fontweight='bold')
    ax.set_xticklabels(['Tidak Resign', 'Resign'])
    ax.set_yticklabels(['Tidak Resign', 'Resign'])
    
    plt.tight_layout()
    plt.savefig(f'img/{model_name}/confusion_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Saved: img/{model_name}/confusion_matrix.png")

# ============================================================================
# GRAPH 5: Metrics Overview (Precision, Recall, F1-Score)
# ============================================================================
print("\n🎨 Creating Graph 5: Ringkasan Metrik...")
fig, axes = plt.subplots(1, 3, figsize=(16, 6))

metrics_names = ['Precision', 'Recall', 'F1-Score']
class_0_metrics = [
    [models[m]['classification_report']['class_0_no_attrition']['precision'] for m in ['full', 'reduced', 'minimal']],
    [models[m]['classification_report']['class_0_no_attrition']['recall'] for m in ['full', 'reduced', 'minimal']],
    [models[m]['classification_report']['class_0_no_attrition']['f1_score'] for m in ['full', 'reduced', 'minimal']]
]
class_1_metrics = [
    [models[m]['classification_report']['class_1_yes_attrition']['precision'] for m in ['full', 'reduced', 'minimal']],
    [models[m]['classification_report']['class_1_yes_attrition']['recall'] for m in ['full', 'reduced', 'minimal']],
    [models[m]['classification_report']['class_1_yes_attrition']['f1_score'] for m in ['full', 'reduced', 'minimal']]
]

x = np.arange(len(model_names))
width = 0.35

for idx, (ax, metric_name) in enumerate(zip(axes, metrics_names)):
    bars1 = ax.bar(x - width/2, class_0_metrics[idx], width, 
                   label='Tidak Resign', color='#4ECDC4', 
                   edgecolor='black', linewidth=1.5)
    bars2 = ax.bar(x + width/2, class_1_metrics[idx], width, 
                   label='Resign', color='#FF6B6B', 
                   edgecolor='black', linewidth=1.5)
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    ax.set_ylabel(metric_name, fontsize=11, fontweight='bold')
    ax.set_title(f'Perbandingan {metric_name}', fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(model_names)
    ax.legend(fontsize=9)
    ax.set_ylim(0, 1.1)
    ax.grid(axis='y', alpha=0.3)

plt.suptitle('Perbandingan Metrik Klasifikasi - Semua Model', 
             fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('img/comparison/metrics_overview.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: img/comparison/metrics_overview.png")

# Also save individual metrics for each model
print("\n🎨 Creating individual Metrics for each model...")
for model_idx, model_key in enumerate(['full', 'reduced', 'minimal']):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    metrics = ['Precision', 'Recall', 'F1-Score']
    class_0 = [
        models[model_key]['classification_report']['class_0_no_attrition']['precision'],
        models[model_key]['classification_report']['class_0_no_attrition']['recall'],
        models[model_key]['classification_report']['class_0_no_attrition']['f1_score']
    ]
    class_1 = [
        models[model_key]['classification_report']['class_1_yes_attrition']['precision'],
        models[model_key]['classification_report']['class_1_yes_attrition']['recall'],
        models[model_key]['classification_report']['class_1_yes_attrition']['f1_score']
    ]
    
    x = np.arange(len(metrics))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, class_0, width, label='Tidak Resign', 
                   color='#4ECDC4', edgecolor='black', linewidth=1.5)
    bars2 = ax.bar(x + width/2, class_1, width, label='Resign', 
                   color='#FF6B6B', edgecolor='black', linewidth=1.5)
    
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    ax.set_ylabel('Nilai', fontsize=12, fontweight='bold')
    ax.set_title(f'Metrik Klasifikasi - Model {model_names[model_idx]}\nAkurasi: {models[model_key]["test_accuracy"]:.2f}%', 
                 fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend(fontsize=10)
    ax.set_ylim(0, 1.1)
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'img/{model_key}/classification_metrics.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Saved: img/{model_key}/classification_metrics.png")

# ============================================================================
# GRAPH 6: Overall Summary Dashboard
# ============================================================================
print("\n🎨 Creating Graph 6: Dashboard Ringkasan...")
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Top: Accuracy comparison
ax1 = fig.add_subplot(gs[0, :])
x = np.arange(len(model_names))
width = 0.25
bars1 = ax1.bar(x - width, train_accuracy, width, label='Akurasi Training', 
                color='#4ECDC4', edgecolor='black', linewidth=1.5)
bars2 = ax1.bar(x, test_accuracy, width, label='Akurasi Testing', 
                color='#FF6B6B', edgecolor='black', linewidth=1.5)
bars3 = ax1.bar(x + width, [t-te for t, te in zip(train_accuracy, test_accuracy)], 
                width, label='Overfitting', color='#FFA500', 
                edgecolor='black', linewidth=1.5)

for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom', fontweight='bold', fontsize=9)

ax1.set_title('Ringkasan Performa Model', fontsize=14, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels([f'{name}\n({feat} fitur)' for name, feat in zip(model_names, num_features)])
ax1.legend(fontsize=10)
ax1.grid(axis='y', alpha=0.3)

# Middle left: Feature count
ax2 = fig.add_subplot(gs[1, 0])
bars = ax2.bar(model_names, num_features, color=colors, 
               edgecolor='black', linewidth=2)
for bar, feat in zip(bars, num_features):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{feat}',
            ha='center', va='bottom', fontweight='bold', fontsize=11)
ax2.set_title('Jumlah Fitur', fontsize=12, fontweight='bold')
ax2.set_ylabel('Jumlah Fitur', fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

# Middle center: Training time
ax3 = fig.add_subplot(gs[1, 1])
bars = ax3.bar(model_names, training_time, color=colors, 
               edgecolor='black', linewidth=2)
for bar, time in zip(bars, training_time):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
            f'{time:.3f}s',
            ha='center', va='bottom', fontweight='bold', fontsize=9)
ax3.set_title('Waktu Training', fontsize=12, fontweight='bold')
ax3.set_ylabel('Detik', fontweight='bold')
ax3.grid(axis='y', alpha=0.3)

# Middle right: Efficiency score (accuracy / features)
ax4 = fig.add_subplot(gs[1, 2])
efficiency = [acc / feat for acc, feat in zip(test_accuracy, num_features)]
bars = ax4.bar(model_names, efficiency, color=colors, 
               edgecolor='black', linewidth=2)
for bar, eff in zip(bars, efficiency):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
            f'{eff:.2f}',
            ha='center', va='bottom', fontweight='bold', fontsize=10)
ax4.set_title('Skor Efisiensi\n(Akurasi/Fitur)', fontsize=12, fontweight='bold')
ax4.set_ylabel('Skor', fontweight='bold')
ax4.grid(axis='y', alpha=0.3)

# Bottom: Dataset info
ax5 = fig.add_subplot(gs[2, :])
ax5.axis('off')
info_text = f"""
INFORMASI DATASET
─────────────────────────────────────────────────────────────────────────────────
Total Sampel: {results['dataset_info']['total_samples']}  |  Tingkat Attrition: {results['dataset_info']['attrition_rate']:.2f}%  |  Tanggal Training: {results['training_date']}

MODEL TERBAIK: {results['comparison']['best_accuracy_model'].upper()}
• Akurasi: {max(test_accuracy):.2f}%  •  Fitur: {num_features[test_accuracy.index(max(test_accuracy))]}  •  Waktu Training: {training_time[test_accuracy.index(max(test_accuracy))]:.4f}s
"""
ax5.text(0.5, 0.5, info_text, ha='center', va='center', 
         fontsize=11, fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.suptitle('Dashboard Ringkasan Training Model', 
             fontsize=16, fontweight='bold', y=0.98)
plt.savefig('img/comparison/summary_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: img/comparison/summary_dashboard.png")

# ============================================================================
# GRAPH 7: Feature Importance for Minimal Model
# ============================================================================
print("\n🎨 Creating Graph 7: Feature Importance Model Minimal...")
fig, ax = plt.subplots(figsize=(12, 8))

# Get feature importance for minimal model
feat_imp = models['minimal']['feature_importance']
features = list(feat_imp.keys())
importances = list(feat_imp.values())

# Sort by importance
sorted_idx = np.argsort(importances)
features = [features[i] for i in sorted_idx]
importances = [importances[i] for i in sorted_idx]

# Create color gradient
colors_gradient = plt.cm.viridis(np.linspace(0.3, 0.9, len(features)))

bars = ax.barh(features, importances, color=colors_gradient, 
               edgecolor='black', linewidth=1.5)

# Add percentage labels
for bar, imp in zip(bars, importances):
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height()/2,
            f' {imp*100:.2f}%',
            ha='left', va='center', fontweight='bold', fontsize=10)

ax.set_xlabel('Tingkat Kepentingan', fontsize=13, fontweight='bold')
ax.set_title('Kepentingan Fitur - Model Minimal (7 Fitur)\nRandom Forest Classifier', 
             fontsize=15, fontweight='bold', pad=20)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('img/minimal/feature_importance.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: img/minimal/feature_importance.png")

# Also create feature importance for Full and Reduced models
print("\n🎨 Creating Feature Importance for Full and Reduced models...")
for model_key in ['full', 'reduced']:
    fig, ax = plt.subplots(figsize=(12, 8))
    
    feat_imp = models[model_key]['feature_importance']
    features = list(feat_imp.keys())
    importances = list(feat_imp.values())
    
    # Sort by importance and take top 15
    sorted_pairs = sorted(zip(features, importances), key=lambda x: x[1], reverse=True)[:15]
    features_top = [p[0] for p in sorted_pairs]
    importances_top = [p[1] for p in sorted_pairs]
    
    # Reverse for horizontal bar chart
    features_top = features_top[::-1]
    importances_top = importances_top[::-1]
    
    colors_gradient = plt.cm.viridis(np.linspace(0.3, 0.9, len(features_top)))
    
    bars = ax.barh(features_top, importances_top, color=colors_gradient, 
                   edgecolor='black', linewidth=1.5)
    
    for bar, imp in zip(bars, importances_top):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2,
                f' {imp*100:.2f}%',
                ha='left', va='center', fontweight='bold', fontsize=9)
    
    model_name_cap = 'Full' if model_key == 'full' else 'Reduced'
    ax.set_xlabel('Tingkat Kepentingan', fontsize=13, fontweight='bold')
    ax.set_title(f'Top 15 Kepentingan Fitur - Model {model_name_cap}\nRandom Forest Classifier', 
                 fontsize=15, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'img/{model_key}/feature_importance.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Saved: img/{model_key}/feature_importance.png")

# ============================================================================
# GRAPH 8-10: Preprocessing Flow for Each Model
# ============================================================================
print("\n🎨 Creating Graph 8-10: Alur Preprocessing per Model...")

for model_idx, model_key in enumerate(['full', 'reduced', 'minimal']):
    model_data = models[model_key]
    model_name = model_names[model_idx]
    
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis('off')
    
    # Title
    fig.suptitle(f'Alur Preprocessing - Model {model_name}', 
                 fontsize=18, fontweight='bold', y=0.95)
    
    # Stage 1: Raw Dataset
    stage1_y = 0.75
    ax.add_patch(plt.Rectangle((0.05, stage1_y), 0.9, 0.12, 
                                facecolor='#FFE5E5', edgecolor='black', linewidth=2))
    ax.text(0.5, stage1_y + 0.09, 'STAGE 1: Dataset Asli', 
            ha='center', fontsize=14, fontweight='bold')
    ax.text(0.5, stage1_y + 0.05, f'Total: {results["dataset_info"]["total_features_original"]} fitur', 
            ha='center', fontsize=11)
    ax.text(0.5, stage1_y + 0.02, f'Sampel: {results["dataset_info"]["total_samples"]} baris', 
            ha='center', fontsize=11)
    
    # Arrow 1
    ax.annotate('', xy=(0.5, stage1_y - 0.02), xytext=(0.5, stage1_y),
                arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    
    # Stage 2: Cleanup
    stage2_y = 0.55
    ax.add_patch(plt.Rectangle((0.05, stage2_y), 0.9, 0.12, 
                                facecolor='#FFF4E5', edgecolor='black', linewidth=2))
    ax.text(0.5, stage2_y + 0.09, 'STAGE 2: Data Cleanup', 
            ha='center', fontsize=14, fontweight='bold')
    ax.text(0.5, stage2_y + 0.05, f'Hapus: Over18, EmployeeCount, StandardHours', 
            ha='center', fontsize=10)
    ax.text(0.5, stage2_y + 0.02, f'Hasil: {results["dataset_info"]["total_features_after_cleanup"]} fitur', 
            ha='center', fontsize=11, color='green', fontweight='bold')
    
    # Arrow 2
    ax.annotate('', xy=(0.5, stage2_y - 0.02), xytext=(0.5, stage2_y),
                arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    
    # Stage 3: Feature Selection
    stage3_y = 0.35
    ax.add_patch(plt.Rectangle((0.05, stage3_y), 0.9, 0.12, 
                                facecolor='#E5F4FF', edgecolor='black', linewidth=2))
    ax.text(0.5, stage3_y + 0.09, 'STAGE 3: Seleksi Fitur', 
            ha='center', fontsize=14, fontweight='bold')
    ax.text(0.5, stage3_y + 0.05, f'Model: {model_name}', 
            ha='center', fontsize=11)
    ax.text(0.5, stage3_y + 0.02, f'Fitur dipilih: {model_data["num_features"]} dari 31', 
            ha='center', fontsize=11, color='blue', fontweight='bold')
    
    # Arrow 3
    ax.annotate('', xy=(0.5, stage3_y - 0.02), xytext=(0.5, stage3_y),
                arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    
    # Stage 4: Preprocessing
    stage4_y = 0.15
    ax.add_patch(plt.Rectangle((0.05, stage4_y), 0.9, 0.12, 
                                facecolor='#F0E5FF', edgecolor='black', linewidth=2))
    ax.text(0.5, stage4_y + 0.09, 'STAGE 4: Preprocessing Pipeline', 
            ha='center', fontsize=14, fontweight='bold')
    ax.text(0.5, stage4_y + 0.05, 
            f'Categorical: {len(model_data["categorical_features"])} fitur (OneHotEncoder)', 
            ha='center', fontsize=10)
    ax.text(0.5, stage4_y + 0.02, 
            f'Numeric: {len(model_data["numeric_features"])} fitur (Passthrough)', 
            ha='center', fontsize=10)
    
    # Summary box
    ax.add_patch(plt.Rectangle((0.1, 0.01), 0.8, 0.09, 
                                facecolor='#E5FFE5', edgecolor='green', linewidth=3))
    ax.text(0.5, 0.07, f'HASIL AKHIR: Akurasi Testing = {model_data["test_accuracy"]:.2f}%', 
            ha='center', fontsize=13, fontweight='bold', color='green')
    ax.text(0.5, 0.03, 
            f'Reduksi: {results["dataset_info"]["total_features_original"]} → {model_data["num_features"]} fitur ({(1 - model_data["num_features"]/results["dataset_info"]["total_features_original"])*100:.1f}% pengurangan)', 
            ha='center', fontsize=11)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    plt.tight_layout()
    plt.savefig(f'img/{model_key}/preprocessing_flow.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Saved: img/{model_key}/preprocessing_flow.png")

# ============================================================================
# GRAPH 11: Combined Preprocessing Comparison
# ============================================================================
print("\n🎨 Creating Graph 11: Perbandingan Preprocessing Semua Model...")
fig, axes = plt.subplots(1, 3, figsize=(18, 8))

for idx, (model_key, ax) in enumerate(zip(['full', 'reduced', 'minimal'], axes)):
    model_data = models[model_key]
    model_name = model_names[idx]
    
    # Stages data
    stages = ['Dataset\nAsli', 'Setelah\nCleanup', 'Seleksi\nFitur', 'Setelah\nEncoding']
    feature_counts = [
        results["dataset_info"]["total_features_original"],
        results["dataset_info"]["total_features_after_cleanup"],
        model_data["num_features"],
        model_data["num_features"] - len(model_data["categorical_features"]) + 
        len([f for cat_feat in model_data["categorical_features"] 
             for f in model_data["feature_importance"].keys() if cat_feat in f])
    ]
    
    colors_stage = ['#FF6B6B', '#FFA500', '#4ECDC4', '#45B7D1']
    bars = ax.bar(stages, feature_counts, color=colors_stage, 
                   edgecolor='black', linewidth=2)
    
    # Add value labels
    for bar, count in zip(bars, feature_counts):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{count}',
                ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    ax.set_title(f'Model {model_name}\nAkurasi: {model_data["test_accuracy"]:.2f}%', 
                 fontsize=13, fontweight='bold', pad=10)
    ax.set_ylabel('Jumlah Fitur', fontsize=11, fontweight='bold')
    ax.set_ylim(0, max(feature_counts) * 1.2)
    ax.grid(axis='y', alpha=0.3)

plt.suptitle('Perbandingan Alur Preprocessing - Semua Model', 
             fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig('img/comparison/preprocessing_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: img/comparison/preprocessing_comparison.png")

print("\n" + "="*80)
print("GRAPH GENERATION COMPLETE!")
print("="*80)
print("\nGenerated files structure:")
print("\nimg/comparison/")
print("  • model_accuracy_comparison.png")
print("  • feature_efficiency.png")
print("  • training_time_comparison.png")
print("  • confusion_matrix_comparison.png")
print("  • metrics_overview.png")
print("  • summary_dashboard.png")
print("  • preprocessing_comparison.png")
print("\nimg/full/")
print("  • confusion_matrix.png")
print("  • classification_metrics.png")
print("  • feature_importance.png")
print("  • preprocessing_flow.png")
print("\nimg/reduced/")
print("  • confusion_matrix.png")
print("  • classification_metrics.png")
print("  • feature_importance.png")
print("  • preprocessing_flow.png")
print("\nimg/minimal/")
print("  • confusion_matrix.png")
print("  • classification_metrics.png")
print("  • feature_importance.png")
print("  • preprocessing_flow.png")
print("\n✨ All graphs created successfully!")
