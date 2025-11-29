"""
Routes - API endpoint definitions
"""

from flask import request
from controllers import (
    PredictionController,
    ResultsController,
    VisualizationController,
    HealthController
)
from views import (
    HealthView,
    FeaturesView,
    PredictionView,
    ResultsView,
    VisualizationView
)


def register_routes(app, model_manager, results_manager, viz_manager):
    """Register all API routes"""
    
    # Initialize controllers
    health_controller = HealthController(model_manager, results_manager)
    prediction_controller = PredictionController(model_manager)
    results_controller = ResultsController(results_manager)
    viz_controller = VisualizationController(viz_manager)
    
    # ========================================================================
    # HEALTH & INFO ROUTES
    # ========================================================================
    
    @app.route('/health', methods=['GET'])
    def health_check():
        """Health check endpoint"""
        health_data = health_controller.get_health_status()
        return HealthView.render(health_data)
    
    @app.route('/features', methods=['GET'])
    def get_features():
        """Get required features"""
        features_data = prediction_controller.get_required_features()
        accuracy = results_manager.get_model_accuracy('minimal')
        return FeaturesView.render(features_data, accuracy)
    
    # ========================================================================
    # PREDICTION ROUTE
    # ========================================================================
    
    @app.route('/predict', methods=['POST'])
    def predict():
        """Prediction endpoint"""
        input_data = request.get_json()
        result = prediction_controller.predict(input_data)
        
        if not result.get('valid'):
            return PredictionView.render_error(result)
        
        # Get model info
        model_info = {
            'type': 'ultra_minimal',
            'features_used': 7,
            'accuracy': f"{results_manager.get_model_accuracy('minimal'):.2f}%"
        }
        
        return PredictionView.render_success(result, model_info)
    
    # ========================================================================
    # RESULTS ROUTES
    # ========================================================================
    
    @app.route('/api/results', methods=['GET'])
    def get_results():
        """Get complete results"""
        result = results_controller.get_all_results()
        if 'error' in result:
            return ResultsView.render_error(result)
        return ResultsView.render_success(result['data'])
    
    @app.route('/api/results/summary', methods=['GET'])
    def get_results_summary():
        """Get results summary"""
        result = results_controller.get_summary()
        if 'error' in result:
            return ResultsView.render_error(result)
        return ResultsView.render_success(result['data'])
    
    @app.route('/api/results/model/<model_type>', methods=['GET'])
    def get_model_results(model_type):
        """Get specific model results"""
        result = results_controller.get_model_results(model_type)
        if 'error' in result:
            return ResultsView.render_error(result)
        return ResultsView.render_success(result['data'])
    
    # ========================================================================
    # VISUALIZATION ROUTES
    # ========================================================================
    
    @app.route('/api/visualizations/list', methods=['GET'])
    def list_visualizations():
        """List all visualizations"""
        result = viz_controller.list_visualizations()
        if 'error' in result:
            return VisualizationView.render_error(result)
        return VisualizationView.render_list(result)
    
    @app.route('/api/visualizations/<category>/<filename>', methods=['GET'])
    def get_visualization(category, filename):
        """Get visualization image"""
        result = viz_controller.get_image(category, filename)
        if 'error' in result:
            return VisualizationView.render_error(result)
        return VisualizationView.render_image(result['path'])
