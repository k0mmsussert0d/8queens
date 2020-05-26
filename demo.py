from multiprocessing import Process, Queue

from eightqueens import eightqueens


def eight_queens(n: int, find_all: bool = True, visualize: bool = False):
    if visualize:
        from gui import gui
        q = Queue()
        visualization = Process(target=gui.visualize_search, args=(n, (q),))
        visualization.daemon = True
        visualization.start()
    else:
        q = None

    res = eightqueens.find_path(n, find_all, events_queue=q)

    if visualize:
        visualization.join()

    return res


if __name__ == '__main__':
    eight_queens(8, False, True)
