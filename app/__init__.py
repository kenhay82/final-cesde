from flask import Flask

app = Flask(__name__)

# MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sembrando_amor'
#mysql = MySQL(app)

# Session Setting
app.secret_key = 'mysecretkey'

# Carpeta 'estática'
app.static_folder = 'assets'

from app import routes