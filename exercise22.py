# coding:utf-8
"""
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
"""
"""
all_pair = []
team1 = ["a", "b", "c"]
team2 = ["x", "y", "z"]
for i in team1:
    for m in team2:
        all_pair.append((i, m))

pair1 = all_pair[0:3]
pair2 = all_pair[3:6]
pair3 = all_pair[6:9]

for i in range(0,3):
    for m in range(0,3):
        for n in range(0,3):
            if i != m and m != n and i != n:
                if pair1[i] != ('a', 'x') and pair3[n] != ('c', 'x') and pair3[n] !=  ('c', 'z'):
                    print pair1[i], pair2[m], pair3[n]
"""
for i in range(ord('x'),ord('z')+1):
    for m in range(ord('x'),ord('z')+1):
        for n in range(ord('x'),ord('z')+1):
            if i != m and m != n and i != n:
                if i != ord('x') and n != ord('x') and n !=  ord('z'):
                    print "matchas are a vs %s, b vs %s, c vs %s" % \
                          (chr(i), chr(m), chr(n))
