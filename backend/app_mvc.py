"""
MVC FLASK API - Employee Attrition Prediction
Architecture: Model-View-Controller pattern for better code organization
"""

from flask import Flask
from flask_cors import CORS

from config import Config
from models import ModelManager, ResultsManager, VisualizationManager
from routes import register_routes


def create_app():
    """Application factory"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    
    # Enable CORS
    CORS(app, origins=Config.CORS_ORIGINS)
    
    return app


def initialize_managers():
    """Initialize all managers (models)"""
    print("="*80)
    print("🚀 INITIALIZING APPLICATION")
    print("="*80)
    
    # Validate paths
    print("\n📂 Validating paths...")
    missing = Config.validate_paths()
    if missing:
        print("❌ Missing files:")
        for item in missing:
            print(f"   - {item}")
        return None, None, None
    print("✅ All paths validated")
    
    # Initialize Model Manager
    print("\n🤖 Loading ML Model...")
    model_manager = ModelManager(Config.MODEL_PATH)
    if not model_manager.load_model():
        return None, None, None
    print(f"✅ Model loaded: {Config.MODEL_PATH}")
    
    # Initialize Results Manager
    print("\n📊 Loading Training Results...")
    results_manager = ResultsManager(Config.RESULTS_PATH)
    if not results_manager.load_results():
        return None, None, None
    print(f"✅ Results loaded: {Config.RESULTS_PATH}")
    
    # Display results info
    dataset_info = results_manager.get_dataset_info()
    if dataset_info:
        print(f"\n📈 Dataset Info:")
        print(f"   Total Samples: {dataset_info['total_samples']}")
        print(f"   Attrition Rate: {dataset_info['attrition_rate']:.2f}%")
    
    summary = results_manager.get_summary()
    if summary:
        print(f"\n🎯 Models Performance:")
        for model_name, model_data in summary['models_summary'].items():
            print(f"   {model_name.upper()}: {model_data['test_accuracy']:.2f}% " +
                  f"({model_data['features']} features)")
    
    # Initialize Visualization Manager
    print("\n🎨 Loading Visualizations...")
    viz_manager = VisualizationManager(Config.IMG_BASE_PATH)
    viz_list = viz_manager.list_all()
    total_viz = sum(len(files) for files in viz_list.values())
    print(f"✅ Found {total_viz} visualizations in {len(viz_list)} categories")
    
    print("="*80)
    
    return model_manager, results_manager, viz_manager


def main():
    """Main application entry point"""
    # Create Flask app
    app = create_app()
    
    # Initialize managers
    model_manager, results_manager, viz_manager = initialize_managers()
    
    if not all([model_manager, results_manager, viz_manager]):
        print("\n❌ Application initialization failed!")
        return
    
    # Register routes
    register_routes(app, model_manager, results_manager, viz_manager)
    
    # Start server
    print("\n🌐 Starting API Server...")
    print(f"📍 URL: http://{Config.HOST}:{Config.PORT}")
    print(f"📋 Required Features: {Config.REQUIRED_FEATURES}")
    print(f"🎯 Model Type: {Config.MODEL_TYPE}")
    print("\n💡 Endpoints:")
    print("   GET  /health")
    print("   GET  /features")
    print("   POST /predict")
    print("   GET  /api/results")
    print("   GET  /api/results/summary")
    print("   GET  /api/results/model/<type>")
    print("   GET  /api/visualizations/list")
    print("   GET  /api/visualizations/<category>/<filename>")
    print("\n" + "="*80)
    
    app.run(
        debug=Config.DEBUG,
        host=Config.HOST,
        port=Config.PORT
    )


if __name__ == '__main__':
    main()
