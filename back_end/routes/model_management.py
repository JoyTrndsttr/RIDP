from flask import Blueprint, request, jsonify
from utils import DataQuery,DataClean
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

#待修改
@model_management_bp.route('/model-management/processed', methods=['GET'])
def get_processed_results():
    location = request.args.get('location')
    datetime = request.args.get('datetime')
    # 返回处理后的结果，这里需要根据参数从模型获取数据
    processed_data = {
        "location": location,
        "datetime": datetime,
        "processed_results": "数据"
    }
    return jsonify(processed_data)
