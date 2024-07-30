import sys

# sys.stdin.readline() 함수는 개행을 제거하지 않음
tmp = sys.stdin.readline()
print("-"*20)
print("input : " + tmp)
print("-"*20)

# 개행 제거를 원한다면 strip() 메서드 사용
print("-"*20)
print("After strip : " + tmp.strip())
print("-"*20)

# n줄 입력
print()
n = int(input("몇 줄을 입력하실건가요? 자연수를 입력하세요.\n"))
lst = list(sys.stdin.readline().strip() for _ in range(n))
print(lst)