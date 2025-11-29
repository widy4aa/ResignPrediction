"""
Controller Layer - Request handling and business logic orchestration
"""

import pandas as pd
from models import ModelManager, ResultsManager, VisualizationManager


class PredictionController:
    """Handles prediction requests"""
    
    MINIMAL_FEATURES = [
        'OverTime',
        'MonthlyIncome',
        'Age',
        'TotalWorkingYears',
        'DistanceFromHome',
        'StockOptionLevel',
        'EnvironmentSatisfaction'
    ]
    
    def __init__(self, model_manager):
        self.model_manager = model_manager
    
    def get_required_features(self):
        """Get list of required features"""
        return {
            'required_features': self.MINIMAL_FEATURES,
            'count': len(self.MINIMAL_FEATURES),
            'categories': {
                'work_life': ['OverTime', 'DistanceFromHome'],
                'compensation': ['MonthlyIncome', 'StockOptionLevel'],
                'experience': ['Age', 'TotalWorkingYears'],
                'satisfaction': ['EnvironmentSatisfaction']
            },
            'description': 'Only these 7 features are required and used'
        }
    
    def validate_input(self, input_data):
        """Validate prediction input data"""
        # Check if input data exists
        if not input_data:
            return {
                'valid': False,
                'error': 'No input data provided',
                'code': 400
            }
        
        # Check for missing features
        missing = [f for f in self.MINIMAL_FEATURES if f not in input_data]
        if missing:
            return {
                'valid': False,
                'error': 'Missing required features',
                'missing': missing,
                'required': self.MINIMAL_FEATURES,
                'hint': 'All 7 features are required',
                'code': 400
            }
        
        # Check for extra features
        extra = [f for f in input_data.keys() if f not in self.MINIMAL_FEATURES]
        if extra:
            return {
                'valid': False,
                'error': 'Extra features not allowed',
                'extra_features': extra,
                'allowed_features': self.MINIMAL_FEATURES,
                'hint': 'Only 7 minimal features are accepted',
                'code': 400
            }
        
        return {'valid': True}
    
    def predict(self, input_data):
        """Process prediction request"""
        # Validate input
        validation = self.validate_input(input_data)
        if not validation['valid']:
            return validation
        
        try:
            # Extract features in correct order
            minimal_data = {feat: input_data[feat] for feat in self.MINIMAL_FEATURES}
            
            # Convert to DataFrame
            df = pd.DataFrame([minimal_data])
            
            # Make prediction
            result = self.model_manager.predict(df)
            
            # Format response
            prediction_label = 'Yes' if result['prediction'] == 1 else 'No'
            confidence = max(result['probabilities'].values()) * 100
            
            return {
                'valid': True,
                'prediction': prediction_label,
                'confidence': round(confidence, 2),
                'probabilities': {
                    'No': round(result['probabilities']['no'] * 100, 2),
                    'Yes': round(result['probabilities']['yes'] * 100, 2)
                }
            }
        
        except Exception as e:
            return {
                'valid': False,
                'error': 'Prediction failed',
                'details': str(e),
                'code': 500
            }


class ResultsController:
    """Handles results requests"""
    
    def __init__(self, results_manager):
        self.results_manager = results_manager
    
    def get_all_results(self):
        """Get complete results"""
        results = self.results_manager.get_all_results()
        if results is None:
            return {'error': 'Results not loaded', 'code': 500}
        return {'valid': True, 'data': results}
    
    def get_summary(self):
        """Get results summary"""
        summary = self.results_manager.get_summary()
        if summary is None:
            return {'error': 'Results not loaded', 'code': 500}
        return {'valid': True, 'data': summary}
    
    def get_model_results(self, model_type):
        """Get specific model results"""
        if model_type not in ['full', 'reduced', 'minimal']:
            return {
                'error': 'Invalid model type. Use: full, reduced, or minimal',
                'code': 400
            }
        
        results = self.results_manager.get_model_results(model_type)
        if results is None:
            return {'error': 'Results not loaded', 'code': 500}
        return {'valid': True, 'data': results}


class VisualizationController:
    """Handles visualization requests"""
    
    def __init__(self, viz_manager):
        self.viz_manager = viz_manager
    
    def list_visualizations(self):
        """List all available visualizations"""
        try:
            visualizations = self.viz_manager.list_all()
            return {
                'valid': True,
                'visualizations': visualizations,
                'base_url': '/api/visualizations'
            }
        except Exception as e:
            return {
                'error': str(e),
                'code': 500
            }
    
    def get_image(self, category, filename):
        """Get visualization image"""
        # Validate category
        if not self.viz_manager.validate_category(category):
            return {
                'error': 'Invalid category. Use: comparison, full, reduced, or minimal',
                'code': 400
            }
        
        # Get image path
        img_path = self.viz_manager.get_image_path(category, filename)
        if img_path is None:
            return {
                'error': f'Visualization not found: {category}/{filename}',
                'code': 404
            }
        
        return {
            'valid': True,
            'path': img_path
        }


class HealthController:
    """Handles health check requests"""
    
    def __init__(self, model_manager, results_manager):
        self.model_manager = model_manager
        self.results_manager = results_manager
    
    def get_health_status(self):
        """Get API health status"""
        model_loaded = self.model_manager.loaded
        results_loaded = self.results_manager.loaded
        
        accuracy = None
        if results_loaded:
            accuracy = self.results_manager.get_model_accuracy('minimal')
        
        return {
            'status': 'healthy' if (model_loaded and results_loaded) else 'error',
            'model': {
                'loaded': model_loaded,
                'type': 'ultra_minimal',
                'features_required': 7,
                'accuracy': f"{accuracy:.2f}%" if accuracy else 'N/A'
            }
        }
