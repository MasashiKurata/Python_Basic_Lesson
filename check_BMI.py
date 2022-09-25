def check(bmi):
    if  bmi<18.5:
        return('低体重')
    elif 18.5 <= bmi < 25:
        return('普通体重')
    elif 25 <= bmi < 30:
        return('肥満:1度')
    elif 30 <= bmi < 35:
        return('肥満:2度')
    elif 35 <= bmi < 40:
        return('肥満:3度')
    else:
        return('肥満:4度')

