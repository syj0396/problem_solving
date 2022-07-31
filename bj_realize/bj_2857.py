#F를 찾고, 그 세글자가 FBI인지 확인.
#근데 세글자가 안되면?
# F부터 끝까지 인덱싱하고, 첫 세글자가 FBI인지 확인.
#근데 F가 여러 개일 수 있음.

#그냥 리스트 순회하면서 F가 나오면 그 세글자,
# 이때 순회는 마지막에서 세번째 원소까지만!!

index = []
for i in range(5):
    candidate = input()
    if 'FBI' in candidate:
        index.append(i+1)

if len(index) == 0:
    print("HE GOT AWAY!")
else:
    for i in index:
        print("%d" %i, end=" ")
