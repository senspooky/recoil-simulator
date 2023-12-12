from threading import Thread, Lock, Event

# a thread that can be stopped
class StoppableThread(Thread):
    def __init__(self, *args, **kwargs):
        # thread fun
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = Event()

    # stops the thread by setting the stop event
    def stop(self):
        self._stop_event.set()

    # check if a thread is stopped
    def stopped(self):
        return self._stop_event.is_set()