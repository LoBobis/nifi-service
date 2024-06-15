import os


def get_free_location():
    x = int(os.getenv('X_LOCATION'))
    y = int(os.getenv('Y_LOCATION'))

    os.environ['X_LOCATION'] = str(x+700)
    os.environ['Y_LOCATION'] = str((x // 2100) * 700)

    return (x, y)
