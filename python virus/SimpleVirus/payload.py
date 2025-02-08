import threading
import random

def overload_cpu():
    while True:
        random.random() ** random.random()

def main():
    for _ in range(100):
        thread = threading.Thread(target=overload_cpu)
        thread.start()

if __name__ == "__main__":
    main()
