from flask import render_template

def index():
    """Homepage of this app

    :return: None
    """
    return render_template('home.html')


def error_pages(error):
    """Return Error pages
    :param error: Error or Exception object
    :return:
    """
    return render_template('error.html', error=str(error))


