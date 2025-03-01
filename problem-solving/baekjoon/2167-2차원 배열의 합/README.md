# 💡**문제 분석 요약**

| 시간 제한 | 메모리 제한 |
| --- | --- |
| 2초 | 128MB |

주어진 2차원 배열의 (i, j) 위치부터 (x, y) 위치까지 저장되어 있는 수의 합 구하는 프로그램
<br>
이때, 배열의 (i, j) 위치 = i행 j열

---
### 입력

첫째 줄 : 배열의 크기 N, M

- 1 ≤ N, M ≤ 300

둘째 줄 ~ N개 : 한 줄에 M개의 수. 배열 주어짐

- 배열에 포함되어 있는 수의 절댓값 ≤ 10,000

그 다음 줄 : 합을 구할 부분의 개수 K

- 1 ≤ k ≤ 10,000

~ K개 : 네 개의 정수 i, j, x, y

- 1 ≤ i ≤ x ≤ N
- 1 ≤ j ≤ y ≤ M

### 출력

K개의 줄에 순서대로 배열의 합 출력
<br>
이때, 배열의 합은 $2^{31} - 1$ 보다 작거나 같음

---
#### **예제**
- 입력
        
    ```
    2 3
    1 2 4
    8 16 32
    3
    1 1 2 3
    1 2 1 2
    1 3 2 3
    ```
        
- 출력
        
    ```
    63
    2
    36
    ```
        
<br>
<aside>
📎 https://www.acmicpc.net/problem/2167

</aside>