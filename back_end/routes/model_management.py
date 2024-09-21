from flask import Blueprint, request, jsonify
from utils import DataQuery,DataClean,DataCut,DataFilter
import json

model_management_bp = Blueprint('model_management', __name__)

@model_management_bp.route('/model-management/settings', methods=['POST'])
def set_model_params():
    BridgeType = request.args.get('BridgeType')
    ModelType = request.args.get('ModelType')
    Parameters = request.args.get('Parameters')
    DataQuery.update_parameters_by_bridge_and_model(BridgeType,ModelType,Parameters)
    return jsonify({"status": "success"})

@model_management_bp.route('/model-management/clean', methods=['GET'])
def get_cleaned_results():
    bridge = request.args.get('bridge')
    time = request.args.get('time')
    type = request.args.get('type')
    Parameters = json.loads(request.args.get('Parameters'))
    threshold = Parameters['threshold']

    metrics = DataQuery.get_file_name_and_content_by_bridge_time_type(bridge, time, type)
    data = json.loads(metrics['FileContent'])
    result = DataClean.is_valid_waveform(data, threshold)
    return jsonify({"status": "success", "result": result})

@model_management_bp.route('/model-management/cut', methods=['GET'])
def get_cut_results():
    bridge = request.args.get('bridge')
    time = request.args.get('time')
    type = request.args.get('type')
    Parameters = json.loads(request.args.get('Parameters'))
    threshold = Parameters['threshold']
    extension = Parameters['extension']

    metrics = DataQuery.get_file_name_and_content_by_bridge_time_type(bridge, time, type)
    data = json.loads(metrics['FileContent'])
    start_index, end_index, bias = DataCut.find_waveform_segment(data, threshold, extension)

    cut_data = data[start_index:end_index]
    for item in cut_data:
        item['value'] -= bias
    return jsonify({"status": "success", "data": cut_data})

@model_management_bp.route('/model-management/filter', methods=['GET'])
def get_filtered_results():
    bridge = request.args.get('bridge')
    time = request.args.get('time')
    type = request.args.get('type')
    Parameters = json.loads(request.args.get('Parameters'))
    window_size = Parameters['window_size']
    metrics = DataQuery.get_file_name_and_content_by_bridge_time_type(bridge, time, type)
    data = json.loads(metrics['FileContent'])
    filtered_data = DataFilter.filter_data(data, window_size)
    return jsonify({"status": "success", "data": filtered_data})