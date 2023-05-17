
## if文
if文を使って条件に応じた処理をする
```python
if x > 0:
    print("positive")
```

``elif``, ``else``を使って細かく

```python
if x < 0:
    print("negative")
elif x = 0:
    print("zero")
elif x = 10:
print("ten")
else
    print("more")
```

## if-問題
シカくんは二つの正整数 a, b を見つけました.
a と b の積が偶数なら ``Even`` , 奇数なら ``Odd`` を出力して下さい.
### 制約
- 1 <= a, b <= 10
<br>
#### 入力例
```python
3
4
```
#### 出力例
```python
Even
```
3 * 4 = 12 は偶数より``Even``

### 解法

- 偶数: 2で割ったあまりが0
- 奇数: 2で割ったあまりが1  

剰余は``%``演算子を使用すれば求めることができる

```python
a = int(input())
b = int(input())
if (a*b)%2 == 0:
    print("Even")
else:
    print("Odd")
```
