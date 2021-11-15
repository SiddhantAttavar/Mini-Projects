code = input()
f1 = open('D:\Downloads\E_F_G_H\F\data\secret\\' + code + '.ans', 'r')
f2 = open('D:\Downloads\\' + code + '.ans', 'r')
for s1, s2 in zip(f1.readlines(), f2.readlines()):
    if s1.strip() != s2.strip():
        print(s1.strip())
        print(s2.strip())
        print()
