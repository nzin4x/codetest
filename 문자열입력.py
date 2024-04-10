# map 없이 string 형으로 인자를 받는다.
# a, b = input().split()
# print('a=' + a + ', b='+ b)

# map 을 이용해 숫자형태로 인자를 받는다.
# a,b,c = map(int , input().split())
# print(a,b,c)

# list
# numbers = list(map(int, input().split()))
# print(numbers)

# multi line
# lines = [input() for _ in range(3)]
# print(lines[2])

# 2차원 배열 한방에 입력
# nums = [list(map(int, input().split()) for _ in range(2))]
# print(nums)

# range in arraylist 배열에 대한 다건 선언
#print(['1' for _ in range(2)])

# 2번의 input 을 받아들여 배열을 선언하겠다.
#print([input() for _ in range(2)])

# 2번의 input 을 받아들여 list 로 선언하겠다.
# print([input().split() for _ in range(2)])

# 2번의 input 을 숫자로 받아들여 list 로 선언하겠다.
# map 은 일괄 형변환을 목표로 하고, 실제로는 다시 list 로 바꾸는 것이다.
# chars = ([input().split() for _ in range(2)])
# nums = ([list(map(int, input().split())) for _ in range(2)])
# print(type(chars[0][0]))
# print(type(nums[0][0]))

# 리스트 선언
# a=[]
# a.append("k")
# print(a)
# print("hello world")

# 배열의 연속 선언
# k1 = [0]*5 # 0,0,0,0,0
# print(k1)
# print(type(k1[2]))

# range 밖으로 빼서 2줄 입력 받을 수 있나? :: 이건 그냥 복사됨
# print([input()] *2)

#
# k2 = [0 for _ in range(5)] # 배열 내에서 선언
# print(k2)
# print(type(k2[2]))

# range(5) 란 몇부터 몇까지인가? 0 부터지 0,1,2
# for i in range(3):
#     print(i)

