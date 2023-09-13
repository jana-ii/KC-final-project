import time
print ('please enter your details to know your daily calorie')
time.sleep(1)
weight = float(input('enter your weight in kg ')) 
height = int(input('enter your height in cm '))
age    = int(input('enter your age '))
gender = input('what is your gender? female or male ')
workout = input('what is your activty level? low, mid, high')





def calculate_counter(weight,height,age,gender):
    if gender == 'male':
        bmr = 66.47 + (13.75 * weight) +  (5 * height) - (6.75 * age)

    else :
        bmr = 655.09 + (9.56 * weight)+ (1.84 * height) - (4.67 * age)
    
    return bmr

def sport_counter(bmr,workout):
    if workout == 'low':
        bmr2 = bmr * 1.2
    elif workout == 'mid':
        bmr2 = bmr * 1.375
    elif workout =='high':
        bmr2 = bmr  * 1.55
    else :
        print('not valid answer')
    return bmr2


bmr = calculate_counter (weight,height,age,gender)
bmr2 = sport_counter(bmr,workout)

print('your daily calorie intake should be' ,bmr2)

time.sleep(1)
print ('please enter your calorie intake from the last 7 days :)')
time.sleep(0.5)
day1 = int(input('day one: '  ))
day2 = int(input('day two: '  ))
day3 = int(input('day three: '))
day4 = int(input('day four: ' ))
day5 = int(input('day five: ' ))
day6 = int(input('day six: '  ))
day7 = int(input('day seven: '))
total = day1 + day2 + day3 + day4 + day5 + day6 +day7

Theaverge = int(total / 7)

print (f'your total calorie intake for this week is {total} ')
print (f'the averge amount calorie intake for this week is {Theaverge}')

test =   bmr2*7 
print (test)

if    total < test < 200 :
    print ('you are eating too little calorie')
elif   total > test < 1500:
    print ('you are eating too much calorie')
else :
    print('you are eating a good amount of calorie')