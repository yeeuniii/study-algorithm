from set import Set

def main():
    # Set 인스턴스 생성
    my_set = Set()

    # 초기 상태: 비어있어야 함
    print("is_empty:", my_set.is_empty())

    # 데이터 추가
    my_set.add(5)
    my_set.add(10)
    my_set.add(15)
    my_set.add(10)  # 중복 추가 시도 (무시되어야 함)

    print("\n5, 10, 15 추가 후:", end=" ")
    my_set.print_all()

    # 데이터 포함 여부 확인
    print("10이 포함되어 있나요?", my_set.is_contain(10))
    print("20이 포함되어 있나요?", my_set.is_contain(20))

    # 데이터 삭제
    my_set.remove(10)
    print("\n10 제거 후:", end=" ")
    my_set.print_all()
    print("10이 포함되어 있나요?", my_set.is_contain(10))

    # clear() 메서드 테스트
    my_set.clear()
    print("\n전체 클리어 후:", end=" ")
    my_set.print_all()
    print("is_empty:", my_set.is_empty())


if __name__ == '__main__':
    main()
