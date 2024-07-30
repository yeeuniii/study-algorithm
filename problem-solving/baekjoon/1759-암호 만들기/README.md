# 💡**문제 분석 요약**

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 2초 | 128MB |


가능성 있는 암호
- 서로 다른 L개의 알파벳 소문자들로 구성
- 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성됨
- 알파벳 오름차순으로 구성되어있을 것

---
### 입력

첫째 줄 : 두 정수  L, C

- 3 ≤ L ≤ C ≤ 15

둘째 줄 : C개의 문자들이 공백으로 구분됨

- 알파벳 소문자 주어짐
- 중복되는 것 없음

### 출력

각 줄에 하나씩, 사전식으로 가능성 있는 암호 출력

---
#### **예제**
- 입력
    
    ```
    4 6
    a t c i s w
    ```
    
- 출력
    
    ```
    acis
    acit
    aciw
    acst
    acsw
    actw
    aist
    aisw
    aitw
    astw
    cist
    cisw
    citw
    istw
    ```
        
<br>
<aside>
📎 https://www.acmicpc.net/problem/1759

</aside>