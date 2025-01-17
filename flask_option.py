# pylint: disable=missing-docstring

import os

def start():
    ''' returns the right message'''
    value = os.getenv('FLASK_ENV')
    if value == 'development':
        return "Starting in development mode..."
    if value == 'production':
        return "Starting in production mode..."

    return "Starting in empty mode..."

if __name__ == "__main__":
    print(start())
