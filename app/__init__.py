from flask import Flask, render_template
from instance.config import DevConfig
from flask_bootstrap import Bootstrap

app = Flask (__name__)

Bootstrap(app = app)

app.config.from_object(DevConfig)
from app import views