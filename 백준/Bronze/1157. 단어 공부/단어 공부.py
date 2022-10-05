import sys

st = sys.stdin.readline().strip()
st = st.upper()
dic = dict()

for s in st:
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1

m = max(dic.values())
values = list(dic.values())

if values.count(m) == 1:
    print(max(dic,key=dic.get))
else:
    print("?")
