from flask import Flask
from fastai.basic_train import load_learner
from fastai.vision import open_image
from flask_cors import CORS

from routes.roadsign_bp import roadsign_bp

app = Flask(__name__)

app.register_blueprint(roadsign_bp, url_prefix='/roadsign')

if __name__ == "__main__":
  app.run()