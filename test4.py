x = int(input()) #day
y = int(input()) #month

months = {
    'January': 30,
    'February': 14,
    'March': 30,
    'April': 31,
    'May': 30,
    'June': 31,
    'July': 30,
    'August': 30,
    'September': 31,
    'October': 30,
    'November': 31,
    'December': 30
}
monthTables = {}

def calculate_days(month,day):
    days_of_week = ["Thursday","Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
    x = 0
    for i in range(month):
        getMonth = months.get(list(months.keys())[i])
        x+=getMonth
    t=0
    table_={}
    for test in months:
        for days in range(months[test]):
            if t >= 7:
                t=0
            table_[days+1] = days_of_week[t]
            t+=1
        monthTables[test] = table_
        table_ = {}

    return monthTables[list(monthTables)[month-1]][day]

if y <=12 and x <= months.get(list(months.keys())[y-1]):
    print(calculate_days(y,x))
else:
    print('Invalid Time')

