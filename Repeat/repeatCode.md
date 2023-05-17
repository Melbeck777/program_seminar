
## for文
``for``文を使用して繰り返し処理を行うことができる

```python
for i in range(n):
    print(i)
```

``range(a, b)``で[a, b)の値を生成する<br>
``range(a, b, s)``で増加量を指定することができる<br>

```python
list(range(5, 10))            # [5, 6, 7, 8, 9]
list(range(0, 10, 3))         # [0, 3, 6, 9]
list(range(-10, -100, -30))   # [-10, -40, -70]
```

<br>

## for-問題
``for``文を使用し, a~bまでの合計を出力せよ<br>

**Ex.**
### 制約
- 1 <= a <= b <= 100

### 入力例

```python
1 100
```
### 出力例

```python
5050
```
1+2+...+100 = 5050 です

<br>

## for-解法
``range(a, b)``で[a, b)の値を生成できるので
``range(a, b+1)``で[a, b]の範囲を生成できる

```python
a = int(input())
b = int(input())
sum = 0
for i in range(a, b+1):
    sum += i
print(sum)
```

<br>

## while文
高度な繰り返し(if + whileというイメージ)<br>
条件式の値が``True``であれば実行を繰り返す

```python
while 条件式:
   処理
```

条件式が``False``であるか,  ``brake``文が実行されるとループを終了する.

```python
i = 0
while i < 3:
    print(i)
    i += 1
while i < 10:
    print(i)
    if i == 5:
        # ループを終了
        break
    i += 1
```

<br>

## while-問題
<!-- 最初のテストで出した問題を再利用すると良さそう? -->

