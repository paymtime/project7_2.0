print('Welcome in our Bowling-club. Enter the names of the participants!!!')
a = map(str, input().split(' - '))
names = list(a)
name_1 = []
name_2 = []
for i in range(10):
    points_1 = int(input('{}{}'.format(names[0], ' - ')))
    name_1.append(points_1)
    points_2 = int(input('{}{}'.format(names[1], ' - ')))
    name_2.append(points_2)
    if sum(name_1) > sum(name_2):
        print('|{0:^12}|{1:^12}|'.format('WINS', 'LOSES'))
        print('|{0:^12}|{1:^12}|'.format(names[0], names[1]))
    elif sum(name_1) < sum(name_2):
        print('|{0:^12}|{1:^12}|'.format('WINS', 'LOSES'))
        print('|{0:^12}|{1:^12}|'.format(names[1], names[0]))
if sum(name_1) > sum(name_2):
    print('{} {}.{}'.format('Winner is', names[0],'Congratulations!'))
elif sum(name_1) < sum(name_2):
    print('{} {}.{}'.format('Победил(а)', names[1],'Congratulations!'))