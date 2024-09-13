from flask import Blueprint, jsonify

process_bp = Blueprint('process', __name__)

@process_bp.route('/process', methods=['GET'])
def get_process():
    # 示例数据，描述数据处理流程
    process = {
        "原始数据波形": "url_to_waveform",
        "切割后的波形": "url_to_cut_waveform",
        "滤波后的波形": "url_to_filtered_waveform",
        "各项指标": "url_to_metrics_chart"
    }
    return jsonify(process)
