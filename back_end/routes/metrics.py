from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from utils import DataQuery
import json
import random

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

@metrics_bp.route('/modelTypes', methods=['GET'])
def get_modelTypes():
    types = ["CleanModel", "CutModel", "FilterModel"]
    return jsonify(types)

@metrics_bp.route('/metrics', methods=['GET'])
def get_metrics():
    bridge = request.args.get('bridge')
    time = request.args.get('time')
    type = request.args.get('type')
    metrics = DataQuery.get_file_name_and_content_by_bridge_time_type(bridge, time, type)
    return jsonify(metrics)

@metrics_bp.route('/data', methods=['GET'])
def get_data():
    metrics = DataQuery.get_sample_metrics_data()
    data = []
    for metric in metrics:
        content = json.loads(metric['Content'])
        metric['Content'] = content[:10]
        data.append(metric)
    print(data)
    return jsonify(data)

@metrics_bp.route('/model_manage', methods=['GET'])
def get_model_data():
    def get_random(base,bias):
        return round(random.uniform(base-bias,base+bias), 6)
    def get_clean_model(model,model_name,id):
        model["ModelID"] = id
        model['ModelName'] = model_name
        model["threshold1"] = get_random(0.1,0.03)
        model["threshold2"] = get_random(0.1,0.05)
        model["threshold3"] = get_random(0.1,0.06)
        model["threshold4"] = get_random(0.1,0.04)
        return model
    def get_cut_model(model,model_name,id):
        model["ModelID"] = id
        model['ModelName'] = model_name
        model["threshold1"] = get_random(0.1,0.03)
        model["threshold2"] = get_random(0.1,0.05)
        model["threshold3"] = get_random(0.1,0.06)
        model["threshold4"] = get_random(0.1,0.04)
        model["extension"]  = get_random(0.05,0.02)
        return model
    def get_filter_model(model,model_name,id):
        model["ModelID"] = id
        model['ModelName'] = model_name
        model["window_size"] = int(get_random(275,225))
        return model
    def get_new_model(model):
        _model = {'ModelID':model['ModelID'], 'Type':model['Type'], 'ModelType':model['ModelType'], 'threshold1':'', 'threshold2':'', 'threshold3':'', 'threshold4':'', 'extension':'', 'window_size':''}
        return _model
    models = DataQuery.get_model_data()
    data = []
    id = 0
    for model in models:
        if model['ModelType'] == "CleanModel":
            data.append(get_clean_model(get_new_model(model), "模型1", id+1))
            data.append(get_clean_model(get_new_model(model), "模型2", id+2))
            data.append(get_clean_model(get_new_model(model), "模型3", id+3))
            id += 3
        if model['ModelType'] == "CutModel":
            data.append(get_cut_model(get_new_model(model), "模型1", id+1))
            data.append(get_cut_model(get_new_model(model), "模型2", id+2))
            data.append(get_cut_model(get_new_model(model), "模型3", id+3))
            id += 3
        if model['ModelType'] == "FilterModel":
            data.append(get_filter_model(get_new_model(model), "模型1", id+1))
            data.append(get_filter_model(get_new_model(model), "模型2", id+2))
            data.append(get_filter_model(get_new_model(model), "模型3", id+3))
            id += 3
    return jsonify(data)