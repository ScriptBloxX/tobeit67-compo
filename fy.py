bullets = int(input())
hp = float(input())
dmg = float(input())
for hit in range(1, bullets+1):
    hp -= dmg
    bullets -= 1
    if hp <= 0:
        print('dead :', bullets, 'bullet remain')
        break
if hp > 0:
    print('alive :', hp, 'health')