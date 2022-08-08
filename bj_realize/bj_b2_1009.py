#일의 자리 숫자가 처음 수의 일의 자리 숫자와 같기 전까지 곱하기
#그 동안의 수를 저장해두기..? ->그럼 반복되는 숫자들의 리스트
#


num = int(input())
for i in range(num):
    a, b = map(int, input().split())
    a_else = a % 10
    tot_list = [a_else]
    tot_else = a - 1
    mult_a = a
    while a_else != tot_else:
        mult_a *= a
        tot_else = mult_a % 10
        tot_list.append(tot_else)
    tot_list.pop()
    b_else = b % len(tot_list)
    result = tot_list[b_else - 1]
    if result == 0:
        print(10)
    else:
        print(result)
