""" Script for run project """
from source import app
from source import middlewares
from source.local_settings import DEBUG, SERVER_HOST, SERVER_PORT, SECRET_KEY

app.secret_key = SECRET_KEY

if __name__ == '__main__':
    app.run(
        debug=DEBUG,
        host=SERVER_HOST,
        port=SERVER_PORT,
    )
