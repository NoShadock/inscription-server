from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from senescribe.auth import login_required
from senescribe.db import get_db
from senescribe import model

bp = Blueprint('subcription', __name__)

