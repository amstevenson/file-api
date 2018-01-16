from file_api.routes import health, drive


def register_blueprints(app):
    app.register_blueprint(health.health)
    app.register_blueprint(drive.drive)
