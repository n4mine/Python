print filter(lambda x:x if x == 2 else not [y for y in range(2,x) if x%y ==0], range(2,101))
