# 💡**문제 분석 요약**

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 2초 | 256MB |

알파벳 소문자로 이루어진 N개의 단어가 들어오는 경우 아래 조건에 따라 정렬하기

    조건1. 길이가 짧은 것부터
    조건2. 길이가 같으면 사전순으로

단, 중복된 단어는 하나만 남기고 제거

### 입력

첫째 줄 : 단어의 개수 N

- 1 ≤ N ≤ 20,000

둘째 줄 ~ N개 : 알파벳 소문자로 이루어진 단어

- 문자열의 길이 < 50

### 출력

조건에 따라 정렬된 단어 한줄에 하나씩

**예제**
- 입력
    
    ```
    13
    but
    i
    wont
    hesitate
    no
    more
    no
    more
    it
    cannot
    wait
    im
    yours
    ```
    
- 출력
    
    ```
    i
    im
    it
    no
    but
    more
    wait
    wont
    yours
    cannot
    hesitate
    ```
---

<aside>
📎 https://www.acmicpc.net/problem/1181

</aside>