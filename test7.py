bullet = int(input())
hp = float(input())
damage = float(input())

def deadCheck(hp):
    if hp > 0:
        print('alive :',hp,'health')
        return
    elif hp <= 0:
        print('dead :',bullet-fire,'bullet remain')

fire = 0
for i in range(bullet):
    if hp > 0:
        fire+=1
        hp-=damage
    else:
        break

deadCheck(hp)
