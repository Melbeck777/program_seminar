```python
# 出力~
`print("Hello, World!") # Hello, World!`

# カンマ区切り~
`print("Hello", "World", "!") # Hello World !`
`print("1 + 2 =", 1 + 2)      # 1 + 2 = 3`

# formatを使用~
`print("{} is {} years old".format("Tom", 25))       # Tom is 25 years old`
`print("Pi is {:.2f}".format(3.141592))              # Pi is 3.14`
`print("{:3d} {:3d} {:3d}".format(1, 10, 100))       # 1 10 100`
`print("{:03d} {:03d} {:03d}".format(1, 10, 100))    # 001 010 100`

```

```python
# 入力

# キーボードから何らかを入力するには, input を使用する
name = input()                 # Alice
print("Hello {}".format(name)) # Hello Alice

# キーボードからの値は, 数値を入力しても常に str であることに注意が必要
age = input()         # 23
print(age, type(age)) # 23 <class 'str'>

# 数値として扱うには int でキャストする必要がある
age = int(input())    # 24
print(age, type(age)) # 24 <class 'int'>
```

```python
# 算術演算
# 四則演算 + , - , * , /
print("7 + 4 = {}".format(7+4)) # 7 + 4 = 11
print("7 - 4 = {}".format(7-4)) # 7 - 4 = 3
print("7 * 4 = {}".format(7*4)) # 7 * 4 = 28
print("7 / 4 = {}".format(7/4)) # 7 / 4 = 1.75

# 切り捨て除算 (Floor division) //
# 小数部を切り捨てた整数値を返す
print("7 // 3 = {}".format(7//3))
# 7 // 3 = 2
print("10 // 6 = {}".format(10//6))
# 10 // 6 = 1
print("-11 // 4 = {}".format(-11//4)) # -11 // 4 = -3

# 剰余 %
print("7 % 3 = {}".format(7%3))   # 7 % 3 = 1
print("10 % 6 = {}".format(10%6)) # 10 % 6 = 4

# べき乗 **
print("2 ** 3 = {}".format(2**3)) # 2 ** 3 = 8
print("5 ** 7 = {}".format(5**7)) # 5 ** 7 = 78125

# 丸括弧 () をグループ化に使うことが出来る
print((50 - 5*6) / 4) # 5.0
print((2 + 5*3) ** 2) # 289
print((20%(7 + 2) + 5*3) - (3*5 - 10)) # 12

"""
算術演算 - 解法
と b を input で読み込む
整数型に直すために int でキャストする
a + b を出力する
"""
a = int(input())
b = int(input())
print(a+b)

```

```python
# 
```

```python
# 
```

```python
# list 

```





```python
# tapl

```

```python
# dictionary

```

