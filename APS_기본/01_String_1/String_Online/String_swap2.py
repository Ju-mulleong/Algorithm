s = 'string'
s = s[::-1]
print(s, type(s))
s_lst = list(s)
s_lst.reverse()
print(s_lst)
print(''.join(s_lst))
