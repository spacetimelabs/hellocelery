
attempts = 0


def run_unstable_task(inputs):
    global attempts
    attempts += 1

    raise RuntimeError("Error {}".format(attempts))
