"""Example Celery app."""
from celery import Celery
import datetime
from models import PageView, setup
app = Celery()
_, session = setup()


@app.task(name='scheduled_task')
def scheduled_task(page_view_id):
    """Print current date and time."""
    page_view = session.query(PageView).filter_by(id=page_view_id).one()
    print(f'Pretending to handle {page_view}')


@app.task(name='example_task')
def example_task(data):
    """Print current date and time."""
    print(f'Started an example task at {datetime.datetime.utcnow()}')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """Set up scheduled tasks for the beat worker."""
    sender.add_periodic_task(60, scheduled_task.s(), name='A scheduled task')


if __name__ == '__main__':
    app.worker_main()
