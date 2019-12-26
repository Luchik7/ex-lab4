import time

class timer():
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = (time.time()) - self.start
        print(t)