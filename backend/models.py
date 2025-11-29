"""
Model Layer - Data handling and business logic
"""

import pickle
import json
import os


class ModelManager:
    """Manages machine learning model loading and predictions"""
    
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None
        self.loaded = False
        
    def load_model(self):
        """Load the pickled model"""
        try:
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
            self.loaded = True
            return True
        except Exception as e:
            print(f"❌ Error loading model: {str(e)}")
            return False
    
    def predict(self, data_frame):
        """Make prediction using the loaded model"""
        if not self.loaded or self.model is None:
            raise ValueError("Model not loaded")
        
        prediction = self.model.predict(data_frame)[0]
        probabilities = self.model.predict_proba(data_frame)[0]
        
        return {
            'prediction': int(prediction),
            'probabilities': {
                'no': float(probabilities[0]),
                'yes': float(probabilities[1])
            }
        }


class ResultsManager:
    """Manages training results from hasil.json"""
    
    def __init__(self, results_path):
        self.results_path = results_path
        self.results = None
        self.loaded = False
    
    def load_results(self):
        """Load results from JSON file"""
        try:
            with open(self.results_path, 'r', encoding='utf-8') as f:
                self.results = json.load(f)
            self.loaded = True
            return True
        except Exception as e:
            print(f"❌ Error loading results: {str(e)}")
            return False
    
    def get_all_results(self):
        """Get complete results"""
        if not self.loaded:
            return None
        return self.results
    
    def get_summary(self):
        """Get summary of all models"""
        if not self.loaded:
            return None
        
        return {
            'training_date': self.results['training_date'],
            'dataset_info': self.results['dataset_info'],
            'models_summary': {
                'full': {
                    'features': self.results['models']['full']['num_features'],
                    'test_accuracy': self.results['models']['full']['test_accuracy'],
                    'training_time': self.results['models']['full']['training_time']
                },
                'reduced': {
                    'features': self.results['models']['reduced']['num_features'],
                    'test_accuracy': self.results['models']['reduced']['test_accuracy'],
                    'training_time': self.results['models']['reduced']['training_time']
                },
                'minimal': {
                    'features': self.results['models']['minimal']['num_features'],
                    'test_accuracy': self.results['models']['minimal']['test_accuracy'],
                    'training_time': self.results['models']['minimal']['training_time']
                }
            },
            'comparison': self.results['comparison']
        }
    
    def get_model_results(self, model_type):
        """Get detailed results for specific model"""
        if not self.loaded:
            return None
        
        if model_type not in ['full', 'reduced', 'minimal']:
            return None
        
        return self.results['models'][model_type]
    
    def get_dataset_info(self):
        """Get dataset information"""
        if not self.loaded:
            return None
        return self.results['dataset_info']
    
    def get_model_accuracy(self, model_type='minimal'):
        """Get accuracy for specific model"""
        if not self.loaded:
            return None
        return self.results['models'][model_type]['test_accuracy']


class VisualizationManager:
    """Manages visualization files"""
    
    def __init__(self, img_base_path):
        self.img_base_path = img_base_path
        self.categories = ['comparison', 'full', 'reduced', 'minimal']
    
    def list_all(self):
        """List all available visualizations"""
        visualizations = {category: [] for category in self.categories}
        
        for category in self.categories:
            category_path = os.path.join(self.img_base_path, category)
            if os.path.exists(category_path):
                files = [f for f in os.listdir(category_path) if f.endswith('.png')]
                visualizations[category] = files
        
        return visualizations
    
    def get_image_path(self, category, filename):
        """Get full path to visualization image"""
        if category not in self.categories:
            return None
        
        img_path = os.path.join(self.img_base_path, category, filename)
        
        if not os.path.exists(img_path):
            return None
        
        return img_path
    
    def validate_category(self, category):
        """Validate category name"""
        return category in self.categories
