"""Simple cooperative scheduler."""
import queue

tasks = queue.Queue()


def schedule(task):
    tasks.put(task)


def run_once():
    if not tasks.empty():
        fn = tasks.get()
        fn()
