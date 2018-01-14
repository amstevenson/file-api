from flask_script import Manager
from file_api.main import app

manager = Manager(app)


@manager.command
def runserver(port=8081):
    """Run the app using flask server"""
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True, port=int(port))


if __name__ == "__main__":
    manager.run()
