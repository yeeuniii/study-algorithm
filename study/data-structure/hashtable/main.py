from hash_table import HashTable

if __name__ == "__main__":
    map = HashTable()

    map.set(13, "정현우")
    map.set(66, "푸이그")
    map.set(4, "카디네스")
    map.set(2, "이주형")
    map.set(24, "송성문")
    map.set(53, "최주환")
    map.set(38, "김동엽")
    map.set(97, "전태현")
    map.set(12, "김건희")
    map.set(1, "김태진")

    print("250308 키움 히어로즈 선발선수 등번호 해시테이블")
    for index in range(10):
        values = map.array[index]
        node = values.head
        print(index, end=" : ")
        while node:
            print(str(node.data.key) + "번 " + node.data.value, end=" ➡ ")
            node = node.next
        print("None")

    print("등번호 2번 : ", map.get(2))
    print("등번호 3번 : ", map.get(3))
    print("등번호 13번 : ", map.get(13))

    print("선발투수(13) 제거")
    map.remove(13)
    print("등번호 13번 : ", map.get(13))
