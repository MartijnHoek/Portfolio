from flask import Blueprint, request, jsonify
from .decoder.handler import VinDecodingHandler

# Create blueprint for all API routes
api_bp = Blueprint("api", __name__)

@api_bp.route("/decode", methods=["GET"])
def decode():
    """
    Endpoint: GET /api/decode?vin=<VIN>
    Purpose: Decode a VIN using VinDecodingHandler
    """
    vin = request.args.get("vin")

    # Return 400 error if VIN is missing
    if not vin:
        return jsonify({"error": "No VIN provided"}), 400

    # Create a VIN decoder handler instance
    handler = VinDecodingHandler(vin)

    # Get the specific decoder for this VIN
    decoder = handler.get_vin_decoder()

    # Return 404 if decoding is not supported
    if not decoder:
        return jsonify({"error": "VIN decoding not supported by API currently"}), 404

    # Decode the VIN
    result = handler.get_vin_decoding_result(decoder)

    # Return decoded result as JSON
    return jsonify(result), 200

@api_bp.route("/health", methods=["GET"])
def health():
    """
    Health check endpoint: GET /api/health
    Returns simple JSON indicating the server is running
    """
    return jsonify({"status": "ok"}), 200