"""
COMPLETE MODEL TRAINING - 3 VERSIONS
Training Full, Reduced, and Minimal models with comprehensive comparison
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import time
from datetime import datetime

# Create output folders
os.makedirs('img', exist_ok=True)
os.makedirs('visualizations', exist_ok=True)

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

print("="*80)
print("COMPLETE MODEL TRAINING - 3 VERSIONS COMPARISON")
print("="*80)
print(f"Training Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ============================================================================
# PART 1: DATA LOADING & PREPROCESSING
# ============================================================================

print("\n" + "="*80)
print("PART 1: DATA LOADING & PREPROCESSING")
print("="*80)

# Load dataset
print("\n🔄 Loading dataset...")
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
print(f"✅ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Drop useless columns
print("\n🔄 Removing useless columns...")
df = df.drop(['Over18', 'EmployeeCount', 'StandardHours'], axis=1)
print(f"✅ After cleanup: {df.shape[1]} columns remaining")

# Target variable
print("\n🔄 Extracting target variable...")
y = df['Attrition'].map({'Yes': 1, 'No': 0})
X = df.drop('Attrition', axis=1)
print(f"✅ Target variable: {y.shape[0]} samples")
print(f"   - Yes (Attrition): {y.sum()} ({y.sum()/len(y)*100:.1f}%)")
print(f"   - No (Retention):  {len(y)-y.sum()} ({(len(y)-y.sum())/len(y)*100:.1f}%)")

# Split data once (same split for all models)
print("\n🔄 Splitting data (80-20)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"✅ Training set: {X_train.shape[0]} samples ({X_train.shape[0]/len(X)*100:.1f}%)")
print(f"✅ Test set:     {X_test.shape[0]} samples ({X_test.shape[0]/len(X)*100:.1f}%)")

# ============================================================================
# DEFINE FEATURE SETS FOR 3 MODELS
# ============================================================================

print("\n" + "="*80)
print("FEATURE SETS DEFINITION")
print("="*80)

# FULL MODEL - All 31 features after cleanup
FULL_FEATURES = [
    'Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome',
    'Education', 'EducationField', 'EnvironmentSatisfaction', 'Gender',
    'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction',
    'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
    'OverTime', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction',
    'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
    'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
    'YearsSinceLastPromotion', 'YearsWithCurrManager', 'EmployeeNumber'
]

# REDUCED MODEL - 11 features (remove redundant & low importance)
REDUCED_FEATURES = [
    'OverTime', 'MonthlyIncome', 'Age', 'YearsAtCompany', 'JobLevel',
    'TotalWorkingYears', 'StockOptionLevel', 'DistanceFromHome',
    'EnvironmentSatisfaction', 'YearsInCurrentRole', 'YearsWithCurrManager'
]

# MINIMAL MODEL - 7 features (top importance ≥ 7%)
MINIMAL_FEATURES = [
    'OverTime', 'MonthlyIncome', 'Age', 'TotalWorkingYears',
    'DistanceFromHome', 'StockOptionLevel', 'EnvironmentSatisfaction'
]

print(f"\n📊 Full Model:    {len(FULL_FEATURES)} features")
print(f"📊 Reduced Model: {len(REDUCED_FEATURES)} features ({len(REDUCED_FEATURES)/len(FULL_FEATURES)*100:.1f}% of Full)")
print(f"📊 Minimal Model: {len(MINIMAL_FEATURES)} features ({len(MINIMAL_FEATURES)/len(FULL_FEATURES)*100:.1f}% of Full)")

# ============================================================================
# PART 2: TRAIN ALL 3 MODELS
# ============================================================================

print("\n" + "="*80)
print("PART 2: TRAINING ALL 3 MODELS")
print("="*80)

def identify_feature_types(features, df):
    """Identify categorical and numeric features"""
    categorical = []
    numeric = []
    for feat in features:
        if df[feat].dtype == 'object':
            categorical.append(feat)
        else:
            numeric.append(feat)
    return categorical, numeric

def create_pipeline(features, X_data):
    """Create preprocessing + model pipeline"""
    categorical_features, numeric_features = identify_feature_types(features, X_data)
    
    transformers = []
    if categorical_features:
        transformers.append(('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_features))
    
    preprocessor = ColumnTransformer(
        transformers=transformers,
        remainder='passthrough'
    )
    
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(
            n_estimators=300,
            max_depth=15,
            min_samples_split=10,
            min_samples_leaf=5,
            random_state=42,
            n_jobs=-1
        ))
    ])
    
    return pipeline, categorical_features, numeric_features

def train_and_evaluate(model_name, features, X_train, X_test, y_train, y_test):
    """Train model and return results"""
    print(f"\n{'='*60}")
    print(f"Training {model_name}")
    print(f"{'='*60}")
    print(f"Features: {len(features)}")
    
    # Filter data to selected features
    X_train_filtered = X_train[features].copy()
    X_test_filtered = X_test[features].copy()
    
    # Create pipeline
    pipeline, cat_features, num_features = create_pipeline(features, X_train_filtered)
    print(f"Categorical: {len(cat_features)}, Numeric: {len(num_features)}")
    
    # Train
    start_time = time.time()
    pipeline.fit(X_train_filtered, y_train)
    training_time = time.time() - start_time
    
    # Predict
    y_pred_train = pipeline.predict(X_train_filtered)
    y_pred_test = pipeline.predict(X_test_filtered)
    
    # Metrics
    train_acc = accuracy_score(y_train, y_pred_train)
    test_acc = accuracy_score(y_test, y_pred_test)
    
    print(f"✅ Training completed in {training_time:.4f}s")
    print(f"📊 Train Accuracy: {train_acc*100:.2f}%")
    print(f"📊 Test Accuracy:  {test_acc*100:.2f}%")
    print(f"📊 Overfitting:    {(train_acc - test_acc)*100:.2f}%")
    
    # Get feature importance
    feature_names = []
    if cat_features:
        encoder = pipeline.named_steps['preprocessor'].named_transformers_['cat']
        cat_names = encoder.get_feature_names_out(cat_features)
        feature_names.extend(cat_names)
    feature_names.extend(num_features)
    
    importances = pipeline.named_steps['classifier'].feature_importances_
    
    return {
        'model_name': model_name,
        'pipeline': pipeline,
        'features': features,
        'n_features': len(features),
        'train_acc': train_acc,
        'test_acc': test_acc,
        'training_time': training_time,
        'y_pred_test': y_pred_test,
        'feature_names': feature_names,
        'importances': importances,
        'categorical': cat_features,
        'numeric': num_features
    }

# Train all 3 models
results = {}

results['full'] = train_and_evaluate(
    "Full Model (31 Features)", FULL_FEATURES, X_train, X_test, y_train, y_test
)

results['reduced'] = train_and_evaluate(
    "Reduced Model (11 Features)", REDUCED_FEATURES, X_train, X_test, y_train, y_test
)

results['minimal'] = train_and_evaluate(
    "Minimal Model (7 Features)", MINIMAL_FEATURES, X_train, X_test, y_train, y_test
)

# ============================================================================
# PART 3: MODEL COMPARISON & VISUALIZATION
# ============================================================================

print("\n" + "="*80)
print("PART 3: MODEL COMPARISON & RESULTS")
print("="*80)

# Summary table
print("\n📊 PERFORMANCE COMPARISON:")
print("-" * 80)
print(f"{'Model':<25} {'Features':<12} {'Train Acc':<12} {'Test Acc':<12} {'Time (s)':<12}")
print("-" * 80)
for key in ['full', 'reduced', 'minimal']:
    r = results[key]
    print(f"{r['model_name']:<25} {r['n_features']:<12} {r['train_acc']*100:>10.2f}%  {r['test_acc']*100:>10.2f}%  {r['training_time']:>10.4f}")
print("-" * 80)

# Find best model
best_model_key = max(results.keys(), key=lambda k: results[k]['test_acc'])
best_model = results[best_model_key]
print(f"\n⭐ BEST MODEL: {best_model['model_name']} ({best_model['test_acc']*100:.2f}% accuracy)")

# ============================================================================
# VISUALIZATION 1: Model Comparison Bar Chart
# ============================================================================

print("\n🎨 Creating visualization: Model comparison...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

models = ['Full\n(31 features)', 'Reduced\n(11 features)', 'Minimal\n(7 features)']
train_accs = [results['full']['train_acc']*100, results['reduced']['train_acc']*100, results['minimal']['train_acc']*100]
test_accs = [results['full']['test_acc']*100, results['reduced']['test_acc']*100, results['minimal']['test_acc']*100]

x = np.arange(len(models))
width = 0.35

bars1 = ax1.bar(x - width/2, train_accs, width, label='Train Accuracy', color='#4ECDC4', edgecolor='black', linewidth=1.5)
bars2 = ax1.bar(x + width/2, test_accs, width, label='Test Accuracy', color='#FF6B6B', edgecolor='black', linewidth=1.5)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'{height:.2f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

ax1.set_xlabel('Model Type', fontweight='bold')
ax1.set_ylabel('Accuracy (%)', fontweight='bold')
ax1.set_title('Model Accuracy Comparison', fontweight='bold', fontsize=13)
ax1.set_xticks(x)
ax1.set_xticklabels(models)
ax1.legend()
ax1.set_ylim(75, 95)
ax1.grid(axis='y', alpha=0.3)

# Training time comparison
times = [results['full']['training_time'], results['reduced']['training_time'], results['minimal']['training_time']]
bars3 = ax2.bar(models, times, color=['#FFA500', '#4ECDC4', '#45B7D1'], edgecolor='black', linewidth=1.5)

for bar in bars3:
    height = bar.get_height()
    ax2.annotate(f'{height:.4f}s',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=9, fontweight='bold')

ax2.set_ylabel('Training Time (seconds)', fontweight='bold')
ax2.set_title('Training Time Comparison', fontweight='bold', fontsize=13)
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('visualizations/08_model_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: visualizations/08_model_comparison.png")

# ============================================================================
# VISUALIZATION 2: Feature Count Reduction
# ============================================================================

print("\n🎨 Creating visualization: Feature reduction process...")
fig, ax = plt.subplots(figsize=(10, 6))

feature_counts = {
    'Original\nDataset': 35,
    'After\nCleanup': 31,
    'Reduced\nModel': 11,
    'Minimal\nModel': 7
}

colors = ['#FF6B6B', '#FFA500', '#4ECDC4', '#45B7D1']
bars = ax.bar(feature_counts.keys(), feature_counts.values(), color=colors, edgecolor='black', linewidth=2)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}',
            ha='center', va='bottom', fontsize=14, fontweight='bold')

ax.set_ylabel('Number of Features', fontsize=12, fontweight='bold')
ax.set_title('Feature Reduction Process Across Models\nFrom 35 to 7 Features (80% Reduction)', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_ylim(0, 40)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('visualizations/01_feature_reduction.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: visualizations/01_feature_reduction.png")

# ============================================================================
# VISUALIZATION 3: Minimal Model Feature Importance
# ============================================================================

print("\n🎨 Creating visualization: Minimal model feature importance...")
minimal_result = results['minimal']
feature_imp_df = pd.DataFrame({
    'Feature': minimal_result['feature_names'],
    'Importance': minimal_result['importances']
}).sort_values('Importance', ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))
colors_bar = plt.cm.viridis(np.linspace(0.3, 0.9, len(feature_imp_df)))
bars = ax.barh(feature_imp_df['Feature'], feature_imp_df['Importance']*100, 
               color=colors_bar, edgecolor='black', linewidth=1.5)

for i, (bar, val) in enumerate(zip(bars, feature_imp_df['Importance']*100)):
    ax.text(val + 0.5, i, f'{val:.2f}%', va='center', fontweight='bold')

ax.set_xlabel('Importance (%)', fontweight='bold', fontsize=12)
ax.set_title('Minimal Model - Feature Importance Ranking\n7 Most Important Features', 
             fontweight='bold', fontsize=14, pad=20)
ax.invert_yaxis()
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('visualizations/07_feature_importance.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: visualizations/07_feature_importance.png")

# ============================================================================
# VISUALIZATION 4: Confusion Matrix for Best Model
# ============================================================================

print("\n🎨 Creating visualization: Confusion matrix...")
cm = confusion_matrix(y_test, best_model['y_pred_test'])

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=True, 
            xticklabels=['No (Retain)', 'Yes (Leave)'],
            yticklabels=['No (Retain)', 'Yes (Leave)'],
            annot_kws={'size': 16, 'weight': 'bold'})

ax.set_xlabel('Predicted Label', fontweight='bold', fontsize=12)
ax.set_ylabel('True Label', fontweight='bold', fontsize=12)
ax.set_title(f'Confusion Matrix - {best_model["model_name"]}\nTest Accuracy: {best_model["test_acc"]*100:.2f}%', 
             fontweight='bold', fontsize=14, pad=20)

plt.tight_layout()
plt.savefig('visualizations/05_confusion_matrix.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: visualizations/05_confusion_matrix.png")

# ============================================================================
# VISUALIZATION 5: Classification Report
# ============================================================================

print("\n🎨 Creating visualization: Performance metrics...")
report = classification_report(y_test, best_model['y_pred_test'], 
                               target_names=['No (Retain)', 'Yes (Leave)'],
                               output_dict=True)

metrics_df = pd.DataFrame(report).transpose()
metrics_df = metrics_df.iloc[:-3, :-1]  # Remove accuracy, macro avg, weighted avg and support

fig, ax = plt.subplots(figsize=(10, 5))
metrics_df.plot(kind='bar', ax=ax, color=['#4ECDC4', '#FF6B6B', '#FFA500'], 
                edgecolor='black', linewidth=1.5, width=0.8)

ax.set_ylabel('Score', fontweight='bold', fontsize=12)
ax.set_xlabel('Class', fontweight='bold', fontsize=12)
ax.set_title(f'{best_model["model_name"]} - Performance Metrics\nPrecision, Recall, F1-Score by Class', 
             fontweight='bold', fontsize=14, pad=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.legend(title='Metric', loc='upper right')
ax.set_ylim(0, 1.1)
ax.grid(axis='y', alpha=0.3)

for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', padding=3, fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('visualizations/06_performance_metrics.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: visualizations/06_performance_metrics.png")

# ============================================================================
# SAVE MODELS & RESULTS
# ============================================================================

print("\n" + "="*80)
print("SAVING MODELS & RESULTS")
print("="*80)

# Save all 3 models
for key in ['full', 'reduced', 'minimal']:
    filename = f'attrition_pipeline_{key}.pkl'
    with open(filename, 'wb') as f:
        pickle.dump(results[key]['pipeline'], f)
    file_size = os.path.getsize(filename) / 1024 / 1024
    print(f"✅ Saved: {filename} ({file_size:.2f} MB)")

# Save feature importance for minimal model
feature_imp_df.to_csv('feature_importance_minimal.csv', index=False)
print("✅ Saved: feature_importance_minimal.csv")

# Save minimal features list
with open('minimal_features.txt', 'w') as f:
    f.write("# Minimal Features for Ultra-Efficient Model\n")
    f.write(f"# Total: {len(MINIMAL_FEATURES)} features\n")
    f.write(f"# Test Accuracy: {results['minimal']['test_acc']*100:.2f}%\n")
    f.write(f"# Feature Reduction: {(1 - len(MINIMAL_FEATURES)/len(FULL_FEATURES))*100:.1f}%\n\n")
    for feat in MINIMAL_FEATURES:
        f.write(f"{feat}\n")
print("✅ Saved: minimal_features.txt")

# Save comprehensive results to JSON
import json

# Prepare confusion matrix for best model
cm = confusion_matrix(y_test, best_model['y_pred_test'])
report = classification_report(y_test, best_model['y_pred_test'], 
                               target_names=['No', 'Yes'],
                               output_dict=True)

# Build results dictionary
hasil_json = {
    "dataset_info": {
        "total_samples": int(X.shape[0]),
        "attrition_count": int(y.sum()),
        "attrition_rate": f"{(y.sum()/len(y)*100):.2f}%",
        "features_original": 35,
        "features_after_cleanup": int(X.shape[1]),
        "training_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "train_samples": int(X_train.shape[0]),
        "test_samples": int(X_test.shape[0])
    },
    "models": {},
    "best_model": best_model_key,
    "best_accuracy": float(best_model['test_acc']),
    "feature_sets": {
        "full": FULL_FEATURES,
        "reduced": REDUCED_FEATURES,
        "minimal": MINIMAL_FEATURES
    }
}

# Add each model's results
for key in ['full', 'reduced', 'minimal']:
    r = results[key]
    
    # Get classification report for this model
    model_report = classification_report(y_test, r['y_pred_test'], 
                                        target_names=['No', 'Yes'],
                                        output_dict=True)
    
    # Get confusion matrix for this model
    model_cm = confusion_matrix(y_test, r['y_pred_test'])
    
    # Build feature importance dict
    feature_importance_dict = {}
    for feat_name, importance in zip(r['feature_names'], r['importances']):
        feature_importance_dict[feat_name] = float(importance)
    
    hasil_json['models'][key] = {
        "name": r['model_name'],
        "features": int(r['n_features']),
        "feature_list": r['features'],
        "categorical_features": r['categorical'],
        "numeric_features": r['numeric'],
        "train_accuracy": float(r['train_acc']),
        "test_accuracy": float(r['test_acc']),
        "overfitting": float(r['train_acc'] - r['test_acc']),
        "precision": float(model_report['Yes']['precision']),
        "recall": float(model_report['Yes']['recall']),
        "f1_score": float(model_report['Yes']['f1-score']),
        "confusion_matrix": {
            "tn": int(model_cm[0][0]),
            "fp": int(model_cm[0][1]),
            "fn": int(model_cm[1][0]),
            "tp": int(model_cm[1][1])
        },
        "training_time_seconds": float(r['training_time']),
        "feature_importance": feature_importance_dict
    }

# Save to JSON file
with open('hasil.json', 'w') as f:
    json.dump(hasil_json, f, indent=2)

print("✅ Saved: hasil.json")

# Print detailed classification report
print("\n" + "="*80)
print(f"CLASSIFICATION REPORT - {best_model['model_name']}")
print("="*80)
print(classification_report(y_test, best_model['y_pred_test'], 
                           target_names=['No (Retain)', 'Yes (Leave)']))

print("\n" + "="*80)
print("TRAINING COMPLETED SUCCESSFULLY!")
print("="*80)
print(f"\n✅ All 3 models trained and saved")
print(f"✅ Best model: {best_model['model_name']} ({best_model['test_acc']*100:.2f}% accuracy)")
print(f"✅ Feature reduction: {len(FULL_FEATURES)} → {best_model['n_features']} features")
print(f"✅ Total visualizations: 5 images saved")
print(f"✅ Results saved in hasil.json")
print("\n" + "="*80)
