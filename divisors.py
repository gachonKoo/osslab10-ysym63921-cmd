import sys

# 첫 번째 명령줄 인수를 정수로 변환하여 number 변수에 저장합니다.
number = int(sys.argv[1])

# 1부터 number까지 반복합니다. (range(1, number + 1) 사용)
for i in range(1, number + 1):
    # number를 i로 나누었을 때 나머지가 0이면 (i가 약수이면)
    if number % i == 0:
        # i를 출력하고, end="" 옵션을 사용하여 공백으로 구분합니다.
        print(i, end=" ")

# 모든 약수를 출력한 후, 줄 바꿈을 합니다.
print()
