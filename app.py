"""Example app with a single endpoint."""
from flask import Flask, render_template, request
from worker import example_task
from models import PageView, setup

# `application` to be compatible with uWSGI default naming
application = Flask(__name__)
_, session = setup()


@application.route('/', methods=['GET'])
def index():
    """Add a page view record and call an async task."""
    page_view = PageView(data={'UA': request.user_agent.string,
                               'cookies': request.cookies})
    session.add(page_view)
    session.commit()
    example_task.delay(page_view.id)
    return render_template('index.html')


if __name__ == '__main__':
    application.run()
