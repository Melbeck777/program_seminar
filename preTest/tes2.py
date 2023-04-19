
# inputは入力です
Attack = int(input())
Monstar_life = int(input())

count = 0
# 何回攻撃するとモンスターは倒せるか 
while Monstar_life > 0:
    Monstar_life -= Attack
    count += 1

print(count)
    


