from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from utils import DataQuery

metrics_bp = Blueprint('metrics', __name__)

@metrics_bp.route('/times', methods=['GET'])
def get_times():
    bridge = request.args.get('bridge')
    times  = DataQuery.get_times_by_bridge(bridge)
    return jsonify(times)

@metrics_bp.route('/types', methods=['GET'])
def get_types():
    types = ["ZZWY1", "ZZWY2", "ZZWY3", "ZZWY4", "LFWY", "ZDJSD2", "ZDWY2", "ZDJSD1", "ZDWY1", "LDQJ", "WD", "SD", "SXJSDX", "XDWY1", "XDWY2", "SXJSDZ", "SXJSDY", "DND", "DYB"]
    return jsonify(types)

@metrics_bp.route('/metrics', methods=['GET'])
def get_metrics():
    bridge = request.args.get('bridge')
    time = request.args.get('time')
    type = request.args.get('type')
    metrics = DataQuery.get_file_name_and_content_by_bridge_time_type(bridge, time, type)
    return jsonify(metrics)
