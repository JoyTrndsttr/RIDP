from flask import Flask
from routes.locations import locations_bp
from routes.metrics import metrics_bp
from routes.process import process_bp
from routes.model_management import model_management_bp
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# 注册蓝图
app.register_blueprint(locations_bp, url_prefix='/api/ridp')
app.register_blueprint(metrics_bp, url_prefix='/api/ridp')
app.register_blueprint(process_bp, url_prefix='/api/ridp')
app.register_blueprint(model_management_bp, url_prefix='/api/ridp')

if __name__ == '__main__':
    app.run(debug=True)
