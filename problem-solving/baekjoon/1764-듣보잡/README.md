# 💡**문제 분석 요약**

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 2초 | 256MB |

듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 
<br>
듣도 보도 못한 사람의 명단을 구하는 프로그램

---
### 입력

첫째 줄 : 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M

- N, M ≤ 500,000. 자연수

둘째 줄 ~ N개 : 듣도 못한 사람의 이름

N + 2줄 ~ M개 : 보도 못한 사람의 이름

- 이름은 띄어쓰기 없이
- 알파벳 소문자로만 구성
- 그 길이는 20 이하
- 각 명단에 중복 없음

### 출력

듣보잡의 수와 그 명단을 사전순으로 출력

---
**예제**
- 입력
    
    ```
    3 4
    ohhenrie
    charlie
    baesangwook
    obama
    baesangwook
    ohhenrie
    clinton
    ```
    
- 출력
    
    ```
    2
    baesangwook
    ohhenrie
    ```
        

<br>
<aside>
📎 https://www.acmicpc.net/problem/1764

</aside>