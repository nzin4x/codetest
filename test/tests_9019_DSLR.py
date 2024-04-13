import sys

def D(i):
    """
    무저건 2배, 10000 넘으면 짤라낸다.
    :param i:
    :return:
    """
    return i * 2 % 10000

def test_D():
    assert 2000 == D(1000)
    assert 6000 == D(8000)
    assert 2 == D(1)
    assert 0 == D(0)

def S(i):
    if i == 0:
        return 9999
    return i - 1


def test_S():
    assert 9999 == S(0)
    assert 2 == S(3)


def L(i):
    i_str = str(i).zfill(4)
    return int(f'{i_str[1:]}{i_str[:1]}')

def R(i):
    i_str = str(i).zfill(4)
    return int(f'{i_str[-1]}{i_str[:3]}')

def test_L():
    assert 2341 == L(1234)
    assert 10 == L(1)
    assert 9999 == L(9999)

def test_R():
    assert 4123 == R(1234)
    assert 1000 == R(1)
    assert 9999 == R(9999)


def dfs_DSLR(START, END):

    # LR / RL 은 의미 없음
    ans = ""
    ans_dict = dict()

    def dfs_solve(i):


        t = D(i)
        if t == END:
            return ans + "D"
        t = S(i)
        if t == END:
            return ans + "S"
        t = L(i)
        if t == END:
            return ans + "L"
        t = R(i)
        if t == END:
            return ans + "R"

    return dfs_solve(START)


def test_nulldict():
    a = dict()
    a[''] = 3
    a['4'] = 5

    assert 3 == a['']
    assert 5 == a['4']



def test_bfs():
    assert "D" == dfs_DSLR(int("1234"), int("2468"))
    # assert "LL" == dfs_DSLR(int("1234"), int("3412"))

if __name__ == '__main__':
    """
    3
    1234 3412
    1000 1
    1 16
    """

    N = sys.stdin.readline()
    M = sys.stdin.readline()
    S = sys.stdin.readline()

    N = int(N.strip())
    M = M.strip() # not using
    S = S.strip()

    # N = 1
    # M = 13
    # S = "OOIOIOIOIIOII"
