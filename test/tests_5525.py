import sys

"""
1 -> IOI
13
OOIOIOIOIIOII
"""

# TODO IOIOI 의 연속 집합의 그룹과 길이를 센다. N 으로 만들어 내는 2N+1 이 몇번 낑겨 들어갈 수 있는지 계산한다.

cnt = 0
grp = 0


def make_group_result(in_str):
    group_set = list()
    if len(in_str) < 3:
        pass
    else:
        continuing = 0
        current_group_start = 0
        is_open = False
        for i, v in enumerate(in_str):
            if not is_open:
                # 새로운 시작을 찾는 로직
                if v == 'I':
                    is_open = True
                    current_group_start = i
                    continuing = 1
            else:
                if in_str[i - 1] != v:
                    continuing = continuing + 1
                else:
                    if continuing > 2:
                        group_set.append((current_group_start, even2odd(continuing)))
                        continuing = 0

                    if v == 'I':
                        current_group_start = i
                        continuing = 1

                    if v != 'I':
                        is_open = False
                        continuing = 0

                if len(in_str) == i + 1:  # 그냥 끝
                    if continuing > 2:
                        group_set.append((current_group_start, even2odd(continuing)))
                        continuing = 0

    return group_set


def even2odd(maybeeven):
    if 0 == maybeeven % 2:
        return maybeeven - 1

    return maybeeven


def test_even2odd():
    assert 3 == even2odd(4)
    assert 3 == even2odd(3)
    assert 5 == even2odd(6)


def cnt_zero(matching_group_len):
    return int(matching_group_len / 2)


def test_cnt_in():
    assert 1 == cnt_zero(3)
    assert 2 == cnt_zero(5)
    assert 3 == cnt_zero(7)


def test_make_group():
    assert [] == make_group_result('00000000000000')
    assert [] == make_group_result('00000I00000000')
    assert [] == make_group_result('I0000I0000000I')
    assert [(13, 3)] == make_group_result('I0000I0000000IOI')
    assert [(13, 5)] == make_group_result('I0000I0000000IOIOI')
    assert [(13, 5)] == make_group_result('I0000I0000000IOIOIOOO')
    assert [(13, 5)] == make_group_result('I0000I0000000IOIOIIII')
    assert [(13, 5), (18, 3)] == make_group_result('I0000I0000000IOIOIIOI')
    assert [(13, 5), (18, 5), (25, 3)] == make_group_result('I0000I0000000IOIOIIOIOI00IOI')
    assert [(2, 7), (9, 3)] == make_group_result('OOIOIOIOIIOII')
    assert [(0, 5)] == make_group_result('IOIOIO')
    assert [(0, 5)] == make_group_result('IOIOI')
    assert [] == make_group_result('IOOOI')
    assert [(1, 3)] == make_group_result('OIOIO')
    assert [(1, 3)] == make_group_result('OIOI')
    assert [] == make_group_result('OIII')
    assert [] == make_group_result('OOOO')
    assert [] == make_group_result('IIII')
    assert [(0, 3)] == make_group_result('IOIO')
    assert [(0, 3)] == make_group_result('IOI')
    assert [] == make_group_result('IOO')
    assert [] == make_group_result('OOI')
    assert [] == make_group_result('IIO')
    assert [] == make_group_result('O')
    assert [] == make_group_result('I')
    assert [] == make_group_result('IO')
    assert [] == make_group_result('OI')


def test_cnt_zeros_in_array():
    assert sum_of_zero(2, 'IOIOIOI') == 2
    assert sum_of_zero(1, 'OIOI') == 1
    assert sum_of_zero(2, 'OOIOIIOIOIOIOIOIOIOIOOIOI') == 6
    assert sum_of_zero(2, 'OOIOIIOIOIOIOIOIOIOIOOIOI') == 6
    assert sum_of_zero(1, 'IOIOOI') == 1
    assert sum_of_zero(1, 'OOOOOOOOOOOOOOOOOOOOOIIIIIIIIIIIIII') == 0
    assert sum_of_zero(1, 'IIIIIIIIIIIIIIOOOOOOOOOOOOOOOOOOOOO') == 0
    assert sum_of_zero(1, 'IIIIIIIIIIIIIIOIIIIIIIIIIIIIIIIIIII') == 1
    assert sum_of_zero(1, 'IOIOIOIOIOIOIOI') == 7
    assert sum_of_zero(2, 'IOIOIOIOIOIOIOI') == 6
    assert sum_of_zero(3, 'IOIOIOIOIOIOIOI') == 5
    assert sum_of_zero(4, 'IOIOIOIOIOIOIOI') == 4
    assert sum_of_zero(5, 'IOIOIOIOIOIOIOI') == 3
    assert sum_of_zero(6, 'IOIOIOIOIOIOIOI') == 2
    assert sum_of_zero(7, 'IOIOIOIOIOIOIOI') == 1
    assert sum_of_zero(8, 'IOIOIOIOIOIOIOI') == 0
    assert sum_of_zero(1, 'OOIOIOIOIIOII') == 4
    assert sum_of_zero(2, 'OOIOIOIOIIOII') == 2
    assert sum_of_zero(1, 'IOI') == 1
    assert sum_of_zero(1, 'OOI') == 0


def sum_of_zero(N, in_str):
    tot_occurs = 0
    for t in make_group_result(in_str):
        length_of_group = t[1]
        cnt_z = cnt_zero(length_of_group)
        tot_occurs = tot_occurs + cnt_z - N + 1
    return tot_occurs


if __name__ == '__main__':
    N = sys.stdin.readline()
    M = sys.stdin.readline()
    S = sys.stdin.readline()

    N = int(N.strip())
    M = M.strip() # not using
    S = S.strip()

    # N = 1
    # M = 13
    # S = "OOIOIOIOIIOII"
    print(sum_of_zero(N, S))
