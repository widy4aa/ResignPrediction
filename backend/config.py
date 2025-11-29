"""
Configuration - App settings and paths
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Application configuration"""
    
    # Flask settings
    DEBUG = os.getenv('FLASK_DEBUG', 'true').lower() == 'true'
    PORT = int(os.getenv('FLASK_PORT', 5000))
    HOST = os.getenv('FLASK_HOST', '0.0.0.0')
    
    # CORS settings
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')
    
    # Base directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Paths from environment variables (with fallback to defaults)
    MODEL_PATH = os.getenv('MODEL_PATH', os.path.join(BASE_DIR, '..', 'model', 'attrition_pipeline_minimal.pkl'))
    RESULTS_PATH = os.getenv('RESULTS_PATH', os.path.join(BASE_DIR, '..', 'model', 'hasil.json'))
    IMG_BASE_PATH = os.getenv('IMG_BASE_PATH', os.path.join(BASE_DIR, '..', 'model', 'img'))
    
    # Convert relative paths to absolute paths
    if not os.path.isabs(MODEL_PATH):
        MODEL_PATH = os.path.join(BASE_DIR, MODEL_PATH)
    if not os.path.isabs(RESULTS_PATH):
        RESULTS_PATH = os.path.join(BASE_DIR, RESULTS_PATH)
    if not os.path.isabs(IMG_BASE_PATH):
        IMG_BASE_PATH = os.path.join(BASE_DIR, IMG_BASE_PATH)
    
    # Model info
    MODEL_TYPE = os.getenv('MODEL_TYPE', 'ultra_minimal')
    REQUIRED_FEATURES = int(os.getenv('REQUIRED_FEATURES', 7))
    
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
