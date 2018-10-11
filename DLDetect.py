import sys

# Length M, indicates number of avail resources
N = 5
M = 3
avail = [0, 0, 0]
# N x M matrix defines number of resources of each type
# currently allocated
alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
# nxm indicates the current request of each thread.
# if request[i][j] equals k, then thread T_i is requesting k more
# instances of resource type R_J
request = [[0, 0, 0], [2, 0, 2], [0, 0, 1], [1, 0, 0], [0, 0, 2]]

finish = [False] * N
work = avail[:]


def step_1():
    global work
    global avail
    global alloc
    global request
    global finish

    for i in range(N):
        finish[i] = all(x == 0 for x in alloc[i])


def step_2():
    global work
    global avail
    global alloc
    global request
    global finish

    i = 0
    while i < N:
        if not finish[i] and list_lte(request[i], work):
            step_3(i)
            i = -1
        i = i + 1
        print(i)
    return step_4()


def step_3(i):
    global work
    global alloc
    global finish

    work = list_add(work, alloc[i])
    finish[i] = True


def step_4():
    global finish

    for i in range(M):
        if not finish[i]:
            return False
    return True


def list_add(l1, l2):
    if len(l1) != len(l2):
        raise Exception("Different sized lists")
    return [x + y for x, y in zip(l1, l2)]


def list_lte(l1, l2):
    # l1 <= l2
    if len(l1) != len(l2):
        raise Exception("Different sized lists")

    for i in range(len(l1)):
        if l1[i] > l2[i]:
            return False
    return True


step_1()
flag = step_2()

if flag:
    print("The system is not deadlocked.")
else:
    procs = ' '.join([str(i) for i, x in enumerate(finish) if not x])
    print("These processes are deadlocked: {}".format(procs))


def main():
    for line in sys.stdin:
        print(line)


if __name__ == '__main__':
    main()
