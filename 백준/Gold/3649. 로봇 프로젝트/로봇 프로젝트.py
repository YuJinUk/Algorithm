import sys
input=sys.stdin.readline

while True:
    try:
        x = int(input())
        N = int(input())
        check = sorted([int(input()) for _ in range(N)])

        left = 0 ; right = N-1 ; answer = -1 ; answer_list = []

        while left < right:
            if check[left] + check[right] == x * 10000000:

                if answer < abs(check[right]-check[left]):
                    answer_list = [check[left], check[right]]
                    answer = abs(check[right]-check[left])
                left += 1

            elif check[left] + check[right] > x * 10000000:
                right -= 1
            else:
                left += 1

        if len(answer_list):
            print("yes %d %d"%(answer_list[0] , answer_list[1]))
        else:
            print('danger')
    except:
        break