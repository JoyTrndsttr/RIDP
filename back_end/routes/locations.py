from flask import Blueprint, jsonify

locations_bp = Blueprint('locations', __name__)

@locations_bp.route('/bridges', methods=['GET'])
def get_locations():
    bridges = ["滁宁城际铁路西涧路特大桥及路桥过渡段", "朔黄重载铁路281#桥2#跨", "朔黄重载铁路281#桥4#跨", "武广高铁枫树下大桥", "武广高铁枫树下桥头路基段", "武广高铁淦河连续梁桥", "武广高铁行将山1#隧道"]
    return jsonify(bridges)
