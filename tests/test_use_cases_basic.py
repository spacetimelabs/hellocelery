from hello import tasks


def test_should_use_apply_async(celery_app):
    result = tasks.get_items.s(42).apply_async(queue='other_queue')
    assert len(result.get()) == 42


def test_should_create_a_basic_workflow():
    """
    .s() == Task signature
    Serial workflow
    get_items returns a list of 3 numbers
    then send that list to is_odd
    """
    workflow = (
        tasks.get_items.s(3) |
        tasks.is_odd.s()
    )
    
    result = workflow.apply_async(queue='other_queue')

    assert result.get() == [True, False, True]


def test_should_use_immutuble_signature(celery_app):
    """
    .si() == Task immutable signature
    so the send_notification will not receive the results from the former task
    """
    workflow = (
        tasks.get_items.s(3) |
        tasks.send_notification.si()
    )
    
    result = workflow.apply_async(queue='other_queue')

    assert result.get() == 'Success'


def test_should_create_a_basic_workflow(celery_app):
    """
    .s() == Task signature
    Serial workflow
    get_items returns a list of 3 numbers
    then send that list to is_odd
    """
    task1_sig = celery_app.signature(
        'hello.get_items', args=(3,), kwargs={}, queue='queue1',
    )

    task2_sig = celery_app.signature(
        'hello.is_odd', args=None, kwargs={}, queue='queue2',
    )

    workflow = (
        task1_sig |
        task2_sig
    )
    
    result = workflow.apply_async()

    assert result.get() == [True, False, True]
