

# Input and Output
### 出力~
```python
print("Hello, World!") # Hello, World!
```

### カンマ区切り~
```python
print("Hello", "World", "!") # Hello World !
print("1 + 2 =", 1 + 2)      # 1 + 2 = 3
```

### formatを使用~
```python
print("{} is {} years old".format("Tom", 25))       # Tom is 25 years old
print("Pi is {:.2f}".format(3.141592))              # Pi is 3.14
print("{:3d} {:3d} {:3d}".format(1, 10, 100))       # 1 10 100
print("{:03d} {:03d} {:03d}".format(1, 10, 100))    # 001 010 100
```

<br>

# 入力
### キーボードから何らかを入力するには, input を使用する
```python
name = input()                 # Alice
print("Hello {}".format(name)) # Hello Alice
```

### キーボードからの値は, 数値を入力しても常に str であることに注意が必要
```python
age = input()         # 23
print(age, type(age)) # 23 <class 'str'>
```

### 数値として扱うには int でキャストする必要がある
```python
age = int(input())    # 24
print(age, type(age)) # 24 <class 'int'>
```

### 出力
```python
# print を使用して文字列を出力できる
print("Hello, World!") # Hello, World!
```

### カンマ区切りでスペースで区切られて出力
```python
print("Hello", "World", "!")                   # Hello World !
print("1 + 2 =", 1 + 2)                        # 1 + 2 = 3
```

### format を使用して思い通りのレイアウトを作成
```python
print("{} is {} years old".format("Tom", 25))  # Tom is 25 years old
print("Pi is {:.2f}".format(3.141592))         # Pi is 3.14
print("{:3d} {:3d} {:3d}".format(1, 10, 100))  # 1 10 100
print("{:03d} {:03d} {:03d}".format(1, 10, 100)) # 001 010 100
```

### 累算代入演算子
```python
a = 0
print(a)  # 0

a += 1
print(a)  # 1

a -= 3
print(a)  # -2

a *= 2
print(a)  # -4
```

### 比較演算
```python
a = 4
b = 6
c = 4

print(a > b)    # False
print(a < b)    # True

print(a == b)   # False
print(b == c)   # False
print(c == a)   # True
```

<br>

# Data type
## int型
```python
# 数字(1)の型を調べてみる
# In
type(1)

#Out
int
```

## float型
```python
# 数字(1.23)の型を調べてみる
# In
type(1.23)

#Out
float
```

## str型
```python
# 文字列(hoge)の型を調べてみる
# In
type("hoge")

# Out
str
```

<br>

# Operation
## 算術演算
### 四則演算 + , - , * , /
```python
print("7 + 4 = {}".format(7+4)) # 7 + 4 = 11
print("7 - 4 = {}".format(7-4)) # 7 - 4 = 3
print("7 * 4 = {}".format(7*4)) # 7 * 4 = 28
print("7 / 4 = {}".format(7/4)) # 7 / 4 = 1.75
```

## 切り捨て除算 (Floor division) //
### 小数部を切り捨てた整数値を返す
```python
print("7 // 3 = {}".format(7//3))     # 7 // 3 = 2
print("10 // 6 = {}".format(10//6))   # 10 // 6 = 1
print("-11 // 4 = {}".format(-11//4)) # -11 // 4 = -3
```

### 剰余 %
```python
print("7 % 3 = {}".format(7%3))   # 7 % 3 = 1
print("10 % 6 = {}".format(10%6)) # 10 % 6 = 4
```

### べき乗 **
```python
print("2 ** 3 = {}".format(2**3)) # 2 ** 3 = 8
print("5 ** 7 = {}".format(5**7)) # 5 ** 7 = 78125
```

### 丸括弧 () をグループ化に使うことが出来る
```python
print((50 - 5*6) / 4) # 5.0
print((2 + 5*3) ** 2) # 289
print((20%(7 + 2) + 5*3) - (3*5 - 10)) # 12
```

## 算術演算 - 解法
aと b を input で読み込む

### 整数型に直すために int でキャストする
```python
# a + b を出力する
a = int(input())
b = int(input())
print(a+b)
```
<br>

# Rule of variable name
## 変数名の付け方
たとえば, csvファイルから人の名前を取得するとき
```python
# 人の名前
a = "Alice"
```
というようにaとかとしてしまうと後でなんの変数だったかわすれてしまう
```python
# 人の名前
name = "Alice"
```
こうすると多少読みやすくなるが, nameでは意味の幅が広すぎる. 食べ物の名前かも
```python
# 人の名前
user_name = "Alice"
```
こうすると, あ, なんかのサービスの会員の名前なんだなってわかる<br>
リストは複数形で
```python
# 会員の名前
user_names = ["太郎", "次郎", "三郎"]
```
以上を踏まえて...
```python
# bad(全然わからん!)
a, b, ...

# better(わかるけど, なにこれ???)
name, adress, ...

# best(万人共通の理解)
lastName, UserName, mail_adress, ...
```
### ex
このプログラムは何を求めている?
adfafafa
adress
address
```python
a = 22
b = 49
c = b - a
# 答えは平林と親との年齢差
```

```python
a = 98
b = 400
c = 0.08
d = 98 * 400 * (1 + c)
# 答えは豚肉400gを買ったときの値段(税込み)
```

## 累算代入演算
```python
apple_num = 3
buy_apple_num = 23
apple_num += buy_apple_num
print(apple_num) # 26
```
<br>

# Rule of variable name
## 変数名の付け方
たとえば, csvファイルから人の名前を取得するとき
```python
# 人の名前
a = "Alice"
```
というようにaとかとしてしまうと後でなんの変数だったかわすれてしまう
```python
# 人の名前
name = "Alice"
```
こうすると多少読みやすくなるが, nameでは意味の幅が広すぎる. 食べ物の名前かも
```python
# 人の名前
user_name = "Alice"
```
こうすると, あ, なんかのサービスの会員の名前なんだなってわかる<br>
リストは複数形で
```python
# 会員の名前
user_names = ["太郎", "次郎", "三郎"]
```
以上を踏まえて...
```python
# bad(全然わからん!)
a, b, ...

# better(わかるけど, なにこれ???)
name, adress, ...

# best(万人共通の理解)
lastName, UserName, mail_adress, ...
```
### ex
このプログラムは何を求めている?
```python
a = 22
b = 49
c = b - a
# 答えは平林と親との年齢差
```

```python
a = 98
b = 400
c = 0.08
d = 98 * 400 * (1 + c)
# 答えは豚肉400gを買ったときの値段(税込み)
```

## 命名規則
同一プログラム内で統一するようにしよう
- スネークケース: ``snake_case``, ``get_input_reader`` 
- キャメルケース: ``camelCase``, ``getInputReader``
```python
# 定数
CONSTANT = 100
```
## 命名規則
同一プログラム内で統一するようにしよう
- スネークケース: ``snake_case``, ``get_input_reader`` 
- キャメルケース: ``camelCase``, ``getInputReader``
```python
# 定数
CONSTANT = 100
```
