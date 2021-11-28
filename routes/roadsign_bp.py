from flask import Blueprint

from controller.RoadSignController import test
from controller.RoadSignController import predict

roadsign_bp = Blueprint('roadsign_bp', __name__)

roadsign_bp.route('/', methods=['GET'])(test)
roadsign_bp.route('/predict',methods=['POST'])(predict)