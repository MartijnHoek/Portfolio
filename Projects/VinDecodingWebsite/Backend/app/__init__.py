import json
from datetime import datetime
import logging
from flask import Flask, request
from flask_cors import CORS
from app.config import Config

def create_app():
    """
    This function builds and returns configured Flask instance.

    Can be used for defining different instances (dev, prod)
    :return: Configured Flask instance
    """
    # Create Flask application and load config
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS so that frontend can reach it
    CORS(app)

    # Import blueprint containing the API routes
    from .routes import api_bp      # Inside the function to avoid circular imports

    # Register the blueprint on the app under /api prefix
    # Example: "/decode" becomes "/api/decode"
    app.register_blueprint(api_bp, url_prefix="/api")

    # Custom logging: cleaner API logs
    logging.getLogger('werkzeug').setLevel(logging.ERROR)

    @app.after_request
    def log_request(response):
        """Log only API requests."""
        path = request.path
        if path.startswith("/api/"):
            # Collect query parameters
            query_params = dict(request.args)

            # Pretty-print query params as JSON
            query_params_str = json.dumps(query_params, indent=2)

            # Color-coded status
            status_color = "\033[92m" if response.status_code < 400 else "\033[91m"
            reset_color = "\033[0m"

            # Timestamp
            timestamp = datetime.now().isoformat()

            # Print formatted log
            print(f"{status_color}[{timestamp}] {request.method} {path} -> {response.status_code}\n"
                  f"Query Parameters:\n{query_params_str}{reset_color}")
        return response

    # Return the fully configured app instance
    return app