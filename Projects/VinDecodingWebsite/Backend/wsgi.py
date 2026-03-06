import os
from app import create_app

# Create a Flask app instance using the factory
# This app is WSGI-ready for Gunicorn
app = create_app()

# Port defaults to 5000 locally, Render provides PORT env variable
port = int(os.getenv("PORT", 5000))

# Mapping of routes that need example query parameters
example_queries = {
    "/api/decode": "?vin=ZFFEX63X000146685"
}

if __name__ == "__main__":
    if not os.getenv("RENDER"):
        # Local development server
        host = "127.0.0.1"

        # Build clickable URLs dynamically
        clickable_endpoints = []
        for rule in app.url_map.iter_rules():
            # Only GET methods, skip internal Flask/static routes
            if "GET" in rule.methods and not rule.rule.startswith("/static"):
                url = f"http://{host}:{port}{rule.rule}"
                # Add example query if route is in example_queries
                if rule.rule in example_queries:
                    url += example_queries[rule.rule]
                clickable_endpoints.append(url)

        # Print server info and clickable URLs
        print(f"\n🚀 Development server running at: http://{host}:{port}\n")
        print("📌 Available API endpoints (clickable in terminal):")
        for endpoint in clickable_endpoints:
            print(f"  {endpoint}")
        print("\nPress CTRL+C to stop the server.\n")

        # Start Flask dev server
        app.run(host=host, port=port, debug=True)

    else:
        # Production on Render (Gunicorn handles the server)
        print(f"Render detected, app ready for WSGI server on port {port}")
