import time


class count(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print ("{:.3f} sec".format(time.time() - self._startTime))