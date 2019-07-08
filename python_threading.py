import threading
import time

def thread_func():
    for i in range(10):
        print "Hello abhinav common its a new thread"
        time.sleep(1)


def main():
    print "Create a Thread with a function without any arguments"

    th = threading.Thread(target = thread_func())
    th.start()
    # print  some messages
    for j in range(9):
        print "Hi this is main thread"
        time.sleep(1)

    th.join()

# used to execute only through command line
if __name__ == "__main__":
    main()



