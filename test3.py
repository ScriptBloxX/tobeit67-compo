# โจทย์ยาวอ่าาา อ่านแล้วปวดหัวเล้ยยยยยย บ่นหน่อย ช่วงนี้ใกล้เปิดเทอม หงุดหงิด ยังนอนไม่เต็มที่เลย
n = input().lower()

# ลูกแก้วเขียนไงนะ? เอาเป็นว่าไอนี่คือลูกแก้วละกัน
someitem = ['q','w','e']

skillList = {
    'q3w0e0':'COLD SNAP',
    'q2w1e0':'GHOST WALK',
    'q2w0e1':'ICE WALL',
    'q0w3e0':'E.M.P',
    'q1w2e0':'TORNADO',
    'q0w2e1':'ALACRITY',
    'q0w0e3':'SUN STRIKE',
    'q1w0e2':'FORGE SPIRIT',
    'q0w1e2':'CHAOS METEOR',
    'q1w1e1': 'DEFEANING BLAST',
}

Invoker_someitem=[] # ไอบ้านี่ จะมีลูกแก้ว max=3
Invoker_Skills=[] # ไอบ้านี่ skill ไรสักอย่าง S,D 2 ช่อง Skill จะเพิ่มจากช่องหน้าสุด (S)
Invoker_SkillsUse=[] # สกิลที่ไอแก่นี่ยิงออกไป

# add ลูกแก้วไป Invoker_someitem (Is) some = ลูกแก้ว เขียนไม่เป็นโว้ยยย translate = marble รู้สึกแปลกๆ
def add_Is(some):
    if len(Invoker_someitem) < 3:
        Invoker_someitem.append(some)
    else:
        Invoker_someitem.pop(0)
        Invoker_someitem.append(some)

# โจทย์ยาวยิ่งความจำไม่ดีอยู่ ทำไมมันยาวขนาดนี้~~~ ahhhhhhhhh
# add skill s,d ไรนั่น
def add_Skill(skill):
    if len(Invoker_Skills) < 2: 
        if skill not in Invoker_Skills and len(Invoker_someitem)==3: # 2 ช่องซ้ำกันไม่ได้ เข้าใจถูกมะ ถ้าเพิ่ม a b b b = b a
            Invoker_Skills.insert(0,skill)
    else:
        if skill not in Invoker_Skills and len(Invoker_someitem)==3:
            Invoker_Skills.pop(1)
            Invoker_Skills.insert(0,skill)

def press_r():
    s = ''.join(Invoker_someitem) # QWQRS = GHOST WALK? didn't mean qqw but mean have 2q and 1w!??
    s = 'q'+str(s.count('q'))+'w'+str(s.count('w'))+'e'+str(s.count('e')) #bruhh
    if s in skillList:
        add_Skill(skillList[s])

def useSkill(i):
    if i <= len(Invoker_Skills)-1: # IndexError HERE!??? HAHAHA
        Invoker_SkillsUse.append(Invoker_Skills[i])

for i in [*n]:
    if i == 'q' or i =='w' or i =='e':
        add_Is(i)
    elif i == 'r':
        press_r()
    elif i == 's':
        useSkill(0)
    else:
        useSkill(1)

if len(Invoker_SkillsUse)>0:
    print(', '.join(Invoker_SkillsUse))
else:
    print('EZ MID')

#first run is Exception Error!??? IndexError:!?? ummm
