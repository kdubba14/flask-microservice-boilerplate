import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.app import create_app, db

# ==========================================================================
# ============= FOR MIGRATIONS NOT CURRENTLY IN USE ========================
# ==========================================================================

env_name = os.getenv('BUILD_ENV')
app = create_app(env_name)

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
