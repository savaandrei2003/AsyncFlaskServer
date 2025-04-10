import multiprocessing
import os
from queue import Queue
from threading import Thread, Event
import time

class Task:
    def __init__(self, job_id: int, data: dict):
        self.job_id = job_id
        self.data = data

    def execute(self):
        pass


class ThreadPool:
    def __init__(self):
        self.job_queue = Queue()
        self.threads = []
        self.start_threads()


    def start_threads(self):
        if "TP_NUM_OF_THREADS" in os.environ:
            self.num_threads = int(os.environ["TP_NUM_OF_THREADS"])
        else:
            self.num_threads = multiprocessing.cpu_count()

        for i in range(self.num_threads):
            thread = TaskRunner(self)
            thread.start()
            self.threads.append(thread)

    def extract_from_queue(self) -> Task:
        try:
            task = self.job_queue.get(timeout=1)
            return task
        except Queue.Empty:
            return None
        
    def add_task(self, task: Task):
        self.job_queue.put(task)


        

class TaskRunner(Thread):
    def __init__(self, threadpool):
        # TODO: init necessary data structures
        Thread.__init__(self)
        self.threadpool = threadpool
        

    def run(self):
        while True:
            try:
                task_to_be_executed = self.threadpool.extract_from_queue()
                if task_to_be_executed is not None:
                    task_to_be_executed.execute()

            
            except Exception as e:
                print(f"Error while processing job: {e}")
            except Queue.Empty:
                continue
