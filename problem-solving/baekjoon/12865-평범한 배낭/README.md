# 💡**문제 분석**

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 2초 | 512MB |


배낭에 넣을 수 있는 물건들의 가치의 최댓값 찾기
<br>
즉, N개의 물건 중, 최대 K만큼의 무게만을 넣을 수 있는 배낭에 최대의 가치 V 찾기
<br>
이때 모든 물건은 무게 W와 가치 V를 가짐

> 참고)
[(9) 동적 프로그래밍](https://www.notion.so/9-800067dae6334db8b9b6e3866826a636?pvs=21)

---

### 입력

첫째 줄 : N, K

- 1 ≤ N ≤ 100
- 1 ≤ K ≤ 100,000

두번째 줄 ~ N개: 각 물건의 무게 W, 해당 물건의 가치 V

- 1 ≤ W ≤ 100,000
- 0 ≤ V ≤ 1,000

### 출력

배낭에 넣을 수 있는 물건들의 가치합의 최댓값

---

#### **예제**
- 입력
    
    ```
    4 7
    6 13
    4 8
    3 6
    5 12
    ```
    
- 출력
    
    ```
    14
    ```
        
<br>


> 📎 https://www.acmicpc.net/problem/12865

