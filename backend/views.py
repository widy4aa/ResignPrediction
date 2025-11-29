"""
View Layer - Response formatting and API routes
"""

from flask import jsonify, send_file


class APIResponse:
    """Handles API response formatting"""
    
    @staticmethod
    def success(data, status_code=200):
        """Format success response"""
        return jsonify(data), status_code
    
    @staticmethod
    def error(message, code=400, details=None):
        """Format error response"""
        response = {
            'status': 'error',
            'message': message
        }
        if details:
            response['details'] = details
        return jsonify(response), code
    
    @staticmethod
    def image(file_path):
        """Send image file"""
        return send_file(file_path, mimetype='image/png')


class HealthView:
    """Health check view"""
    
    @staticmethod
    def render(health_data):
        """Render health check response"""
        return APIResponse.success(health_data)


class FeaturesView:
    """Features view"""
    
    @staticmethod
    def render(features_data, accuracy):
        """Render features response"""
        features_data['accuracy'] = f"{accuracy:.2f}%" if accuracy else 'N/A'
        return APIResponse.success(features_data)


class PredictionView:
    """Prediction view"""
    
    @staticmethod
    def render_success(prediction_result, model_info):
        """Render successful prediction"""
        response = {
            'prediction': prediction_result['prediction'],
            'confidence': prediction_result['confidence'],
            'probabilities': prediction_result['probabilities'],
            'model_info': model_info
        }
        return APIResponse.success(response)
    
    @staticmethod
    def render_error(error_data):
        """Render prediction error"""
        code = error_data.pop('code', 400)
        error_msg = error_data.pop('error', 'Prediction failed')
        return APIResponse.error(error_msg, code, error_data)


class ResultsView:
    """Results view"""
    
    @staticmethod
    def render_success(data):
        """Render successful results"""
        return APIResponse.success(data)
    
    @staticmethod
    def render_error(error_data):
        """Render results error"""
        code = error_data.get('code', 500)
        message = error_data.get('error', 'Error fetching results')
        return APIResponse.error(message, code)


class VisualizationView:
    """Visualization view"""
    
    @staticmethod
    def render_list(viz_data):
        """Render visualization list"""
        return APIResponse.success({
            'status': 'success',
            'visualizations': viz_data['visualizations'],
            'base_url': viz_data['base_url']
        })
    
    @staticmethod
    def render_image(img_path):
        """Render image file"""
        return APIResponse.image(img_path)
    
    @staticmethod
    def render_error(error_data):
        """Render visualization error"""
        code = error_data.get('code', 404)
        message = error_data.get('error', 'Visualization not found')
        return APIResponse.error(message, code)
