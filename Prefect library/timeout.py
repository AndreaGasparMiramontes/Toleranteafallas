from prefect import flow, task, get_run_logger
from time import sleep
import random


@task
def wait_task():
    num = random.randint(0,3)
    sleep(num)
    return 1


@flow
def my_flow():
    final_state = wait_task.submit().wait(2)
    logger = get_run_logger()
    if final_state:
        logger.info("The task is done")

    else:
        logger.info("The task is canceled because it takes too long to run")


if __name__ == "__main__":
    cont = 0
    while cont<5:
        my_flow()
        cont+=1