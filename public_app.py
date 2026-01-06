from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from functools import wraps
import os

app = Flask(__name__, template_folder='template')
app.secret_key = os.environ.get("APP_SECRET_KEY", "public-demo-key")

# -------------------------
# Login setup
# -------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

users = {
    'demo': User(id=1, username='demo', password='demo')
}

@login_manager.user_loader
def load_user(user_id):
    for user in users.values():
        if user.id == int(user_id):
            return user
    return None


# -------------------------
# Utility
# -------------------------
def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = view(*args, **kwargs)
        response.headers['Cache-Control'] = 'no-store'
        return response
    return no_cache


@app.context_processor
def inject_user():
    return dict(current_user=current_user)


# -------------------------
# Routes
# -------------------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Usermaunal')
def usermaunal():
    return render_template('usermaual.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.get(username)
        if user and user.password == password:
            login_user(user)
            flash("Login successful")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials")
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully")
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('datageneration_TP.html')


@app.route('/analysis')
def analysis():
    return render_template('Analysis.html')


# -------------------------
# API (Public Stub)
# -------------------------
@app.route('/predict', methods=['POST'])
def predict():
    """
    Public stub endpoint.
    Full prediction pipeline is not included in the public version.
    """
    return jsonify({
        "status": "disabled",
        "message": "Prediction service is not available in the public demo version. Please contact the author for full access."
    })


@app.route('/upload', methods=['POST'])
def upload_file():
    return jsonify({
        "status": "disabled",
        "message": "Upload and training features are not available in the public demo version."
    })


@app.route('/train', methods=['POST'])
@login_required
def train_models_endpoint():
    return jsonify({
        "status": "disabled",
        "message": "Training is not available in the public demo version."
    })


# -------------------------
# Metadata Endpoint
# -------------------------
@app.route('/about')
def about():
    return jsonify({
        "project": "TheRMO_DynaMIC AnalySIS",
        "author": "Ashish Joshi, Kaushik Joshi",
        "contact": "Please contact the author directly for full code, datasets, and reproducibility.",
        "license": "All Rights Reserved © 2026 Ashish Joshi, Kaushik Joshi"
    })


if __name__ == '__main__':
    app.run(debug=True)
