import pytest
from hello.tasks import app


@pytest.fixture()
def celery_app(request):
    # Allow celery executes tasks without a worker and queues
    # ATTENTION: This does not do exactly what a worker would do,
    # just allow you test .delay() and .apply_async() without a worker
    app.conf.task_always_eager = True
    return app
