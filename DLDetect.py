import sys


def init_finish(alloc_arr):
    """
    Returns an array that is len(alloc_ar) large, with each index
    referring to the respective process number. It is set to true,
    if the process has no resources allocated to it.

    :param alloc_arr: A 2D array that lists resource assignment
    :returns: A 1D array that contains true/false in the index of the
        respective process if that process is "done"
    """
    return [all(x == 0 for x in proc) for proc in alloc_arr]


def find_next_unfinished_proc(finish_arr, request_arr, work_arr):
    """
    Given an array of status of processes (finish_arr),
    :param finish_arr:
    :param request_arr:
    :param work_arr:
    :param num_procs:
    :return:
    """
    return next((i for i, val in enumerate(finish_arr) if
                 not val
                 and list_lte(request_arr[i], work_arr)), -1)


def is_deadlock(finish_arr):
    """
    Determines if the system is in deadlock based on finish_arr.
    If any processes are still False in the finish_arr we are in
    a state of deadlock.

    :return:  If the system is deadlocked or not.
    """
    return not all(finish_arr)


def output_results(finish_arr):
    """
    Outputs the results that the program found regarding the
    system being deadlocked. Requires the array of statuses of
    processes (finish_arr)
    """
    deadlock = is_deadlock(finish_arr=finish_arr)
    if deadlock:
        procs = ' '.join([str(i) for i, x in enumerate(finish_arr) if not x])
        print("These processes are deadlocked: {}".format(procs))
    else:
        print("The system is not deadlocked.")


def list_add(l1, l2):
    """
    Adds each element of a list, returns a new list.

    e.x.
        l1 = [1,2,3]
        l2 = [3,2,1]
        returns [4,4,4] since [1 + 3, 2 + 2, 1 + 3]
    """
    if len(l1) != len(l2):
        raise Exception("Different sized lists")

    # zip returns a tuple of each index of the lists, to iterate over.
    return [x + y for x, y in zip(l1, l2)]


def list_lte(l1, l2):
    """
    Determines if list one is less than list two for each and every
    element, where order matters.

    e.x.
        l1 = [0,1,2,3]
        l2 = [0,1,2,2]

        In this case, it would return false since the l1[3] > l2[3]

    e.x. 2
        l1 = [1,1,1,1]
        l2 = [1,1,4,5]

        In this case True would be returned, since in every index
        l1[idx] <= l2[idx]

    """
    if len(l1) != len(l2):
        raise Exception("Different sized lists")

    # zip returns a tuple of each index of the lists, to iterate over.
    return all(x <= y for x, y in zip(l1, l2))


def main():
    # Line 1: Number of processes, a positive int
    num_procs = int(sys.stdin.readline())
    # Line 2: Number of resource types, a positive int
    num_res = int(sys.stdin.readline())
    # Line 3: The contents of array Avail, each will be separated by whitespace
    avail = [int(x) for x in sys.stdin.readline().split()]
    # Next |num_procs| lines: contents of array Alloc, separated by whitespace
    # List comprehension to read in the next num_procs lines into a
    # num_procs x num_res 2d array.
    alloc = [[int(x) for x in next(sys.stdin).split()] for n in range(num_procs)]
    # Next |num_procs| lines: contents of array req. separated by whitespace
    request = [[int(x) for x in next(sys.stdin).split()] for n in range(num_procs)]

    # Copy the avail list, so it isn't referencing same object
    # This is specified in the algorithm definition, however, `avail`
    # is not used anywhere. So unaware of why.
    work = avail[:]
    finish = init_finish(alloc_arr=alloc)

    # See PEP 315 for syntax justification
    # Loops until no more processes are incomplete or
    # there are not enough resources to complete any more processes.
    while True:
        unfin_proc_idx = find_next_unfinished_proc(finish_arr=finish,
                                                   request_arr=request,
                                                   work_arr=work)
        if unfin_proc_idx >= 0:
            finish[unfin_proc_idx] = True
            work = list_add(work, alloc[unfin_proc_idx])
        else:
            break

    output_results(finish_arr=finish)


if __name__ == '__main__':
    main()
