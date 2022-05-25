from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.model import User
from apps.model import Picture
from apps import create_app
from ext import db
from flask_cors import CORS

app = create_app()
CORS(app, resources=r'/*')

manager = Manager(app=app)

migrate = Migrate(app=app, db=db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
