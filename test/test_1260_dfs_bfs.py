"""
4 5 1
1 2
1 3
1 4
2 4
3 4

1 2 4 3 dfs
1 2 3 4 bfs
"""
import sys
from collections import deque


def build_connection(info, connection_info):
    vertex_cnt, edge_cnt, info_line_cnt = map(int, info.split())
    plist = connection_info.split("\n")

    conn = [[] for _ in range(vertex_cnt + 1)]

    for v in plist:
        _from, _to = map(int, v.split())
        conn[_from].append(_to)
        conn[_to].append(_from)

    return conn


def test_connection():
    """
    4 5 1
    1 2
    1 3
    1 4
    2 4
    3 4
    :return:
    """

    conn = get_connection()

    assert 3 in conn[4]
    assert 3 in conn[1]


def get_connection():
    return build_connection("4 5 1", """1 2
1 3
1 4
2 4
3 4""")


def bfs(conn, start=1):
    visited_seq = list()
    q = deque()

    q.append(start)
    visited_seq.append(start)

    while q:
        current_pos = q.popleft()
        for next_candidate in sorted(conn[current_pos]):
            if next_candidate not in visited_seq:
                q.append(next_candidate)
                visited_seq.append(next_candidate)

    return visited_seq


def dfs(conn, start=1):
    visited_seq = list()

    def dfs_core(current_pos):
        visited_seq.append(current_pos)

        for next_candidate in sorted(conn[current_pos]):
            if next_candidate not in visited_seq:
                dfs_core(next_candidate)

    dfs_core(start)

    return visited_seq


def test_dfs():
    conn = get_connection()
    assert "1 2 4 3" == " ".join(map(str, dfs(conn, 1)))


def test_bfs():
    conn = get_connection()
    assert "1 2 3 4" == " ".join(map(str, bfs(conn, 1)))


if __name__ == '__main__':
    v_cnt, e_cnt, start = map(int, sys.stdin.readline().split())

    conn = [[] for _ in range(v_cnt + 1)]

    for _ in range(e_cnt):
        _from, _to = map(int, sys.stdin.readline().split())
        conn[_from].append(_to)
        conn[_to].append(_from)

    print(" ".join(map(str, dfs(conn, start))))
    print(" ".join(map(str, bfs(conn, start))))
