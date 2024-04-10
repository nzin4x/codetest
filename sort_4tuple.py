# sorted tuple 비교

s1 = [(1, 1), (1, 2), (2, 2), (2, 1)]
s2 = [(1, 1), (2, 1), (2, 2), (1, 2)]

s_s1 = sorted(s1)
s_s2 = sorted(s2)

print(s1 == s2)
print(s_s1 == s_s2)
