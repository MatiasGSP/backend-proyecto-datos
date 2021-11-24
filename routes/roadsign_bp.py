from flask import Blueprint

from controller.RoadSignController import test

roadsign_bp = Blueprint('roadsign_bp', __name__)
roadsign_bp.route('/', methods=['GET'])(test)