import os
from eggHunt import eggHunt
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand
 
manager = Manager(eggHunt)
 
# these names will be available inside the shell without explicit import
def make_shell_context():
    return dict(app=eggHunt)
 
manager.add_command('shell', Shell(make_context=make_shell_context))

 
if __name__ == '__main__':
    manager.run()