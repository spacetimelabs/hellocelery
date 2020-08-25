import pytest
from hello import tasks


def test_should_retry_3_times_before_fail(celery_app):
    with pytest.raises(Exception) as error:
        result = tasks.unstable_task.s(42).apply_async()
        assert str(error.value) == "Error 4"
