from eightqueens.eightqueens import find_path
from gui.gui import visualize_search
from multiprocessing import Process, Queue


def eight_queens(n: int, visualize: bool = False):
    if visualize:
        q = Queue()
        visualization = Process(target=visualize_search, args=(n, (q),))
        visualization.daemon = True
        visualization.start()
    else:
        q = None

    res = find_path(n, events_queue=q)

    if visualize:
        visualization.join()

    return res


if __name__ == '__main__':
    eight_queens(8, True)
