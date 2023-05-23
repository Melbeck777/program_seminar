
## Function

### 重量と加速度を与えると力を得る
``` python
def gravity(mass, acceleration):
    return mass*acceleration
```

### 関数を使うメリット
関数を使わなかった場合
```python
if year%4 == 0 and year%100 != 0 or year%400 == 0:
    # do something
```
関数を使った場合
```python
def isLeapYear(year):
    return year%4 == 0 and year%100 != 0 or year%400 == 0
if isLeapYear(year):
    # do something
```

### 関数-問題

a, b, cの最大値を求める関数を作成しましょう

- 入力例
```python
15
34
7
```

- 出力例
```python
34
```

関数-解法
```python
def getMax3(a, b, c):
    if b <= a and c <= a:
        return a
    if c <= b:
        return b
    return c
a = int(input())
b = int(input())
c = int(input())
print(getMax3(a, b, c))
```

別解
```python
def getMax3(a, b, c):
    return max(a, max(b, c))
```
