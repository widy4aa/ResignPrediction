"""
Configuration - App settings and paths
"""

import os


class Config:
    """Application configuration"""
    
    # Flask settings
    DEBUG = True
    PORT = 5000
    HOST = '127.0.0.1'
    
    # CORS settings
    CORS_ORIGINS = '*'
    
    # Paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_DIR = os.path.join(BASE_DIR, '..', 'model')
    
    # Model files
    MODEL_PATH = os.path.join(MODEL_DIR, 'attrition_pipeline_minimal.pkl')
    RESULTS_PATH = os.path.join(MODEL_DIR, 'hasil.json')
    
    # Visualization
    IMG_BASE_PATH = os.path.join(MODEL_DIR, 'img')
    
    # Model info
    MODEL_TYPE = 'ultra_minimal'
    REQUIRED_FEATURES = 7
    
    @classmethod
    def validate_paths(cls):
        """Validate that required files exist"""
        paths = {
            'Model': cls.MODEL_PATH,
            'Results': cls.RESULTS_PATH,
            'Images': cls.IMG_BASE_PATH
        }
        
        missing = []
        for name, path in paths.items():
            if not os.path.exists(path):
                missing.append(f"{name}: {path}")
        
        return missing
