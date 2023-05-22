
## Error
### 全角スペースのエラー
エラー文

code
```python
print("hello")　
```

error
```
  File "./error.py", line 1
    print("hello")　
                  ^
SyntaxError: invalid non-printable character U+3000

```

### 未定義エラー
エラー文

code
```python
a = 2
b = c+1
```

error
```
  File "./error2.py", line 2, in <module>
    b = c + 1
NameError: name 'c' is not defined
```

### if分行末エラー
エラー文

code
```python
a = 4
b = 5
if a < b
print(b)
```

error
```
  File "/home/hira/lab/tes/error3.py", line 4
    if a < b
            ^
SyntaxError: expected ':'
```

### 出力型エラー 
エラー文

code
```python
a = "my age is"
b = 41
print(a + b)
```

error
```
  File "./error4.py", line 4, in <module>
    print(a + b)
TypeError: can only concatenate str (not "int") to str
```

