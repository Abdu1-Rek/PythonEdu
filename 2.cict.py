x = 19234 + 465123 - 412**4
cnt = 0
for s in oct(x)[2:]:
    if s in '1357':
        cnt += 1
print(cnt)
        