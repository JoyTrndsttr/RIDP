from flask import Blueprint, request, jsonify
from utils import DataQuery

model_management_bp = Blueprint('model_management', __name__)

@model_management_bp.route('/model-management/settings', methods=['POST'])
def set_model_params():
    BridgeType = request.args.get('BridgeType')
    ModelType = request.args.get('ModelType')
    Parameters = request.args.get('Parameters')
    DataQuery.update_parameters_by_bridge_and_model(BridgeType,ModelType,Parameters)
    return jsonify({"status": "success"})

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
