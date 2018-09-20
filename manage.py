#encoding:utf-8
#专门存放命令

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from zlktqa import app
from exts import db
from models import User, Question, Answer

manger = Manager(app)

#使用Migrate绑定APP和DB
migrate = Migrate(app, db)

#添加迁移脚本的命令到manager中
manger.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manger.run()

