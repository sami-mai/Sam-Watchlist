from app import create_app
from flask_script import Manager, Server, Shell


# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    # app.run(debug = True) ...remove the 'debug = True' argument from our
    # app.run() because the debug mode has been enabled in the configuration
    # file
    manager.run()
