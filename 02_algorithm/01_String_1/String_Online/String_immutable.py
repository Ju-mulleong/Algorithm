# input값은 abc

s1 = list(input())
print(s1)
s2 = input()
print(s2)
print(s1[1])
print(s2[1])

s1[1] = 'e'
print(s1)

# s2[1] = 'e'   String은 불변 객체, 아예 다른 객체를 참조하도록 하는건 가능하지만, 불변 객체를 바꿀 수는 없다.
# print(s2)
