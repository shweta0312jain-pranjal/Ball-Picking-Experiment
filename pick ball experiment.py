import random

def pick_ball_experiment():

    balls = ['red', 'blue', 'green']


    result = random.choice(balls)


    pro = balls.count('red') / len(balls)
    print("Probability of picking Red ball is: ", pro)


    if result == 'red':
        return "You picked a Red ball!"
    else:
        return 'Better Luck Next Time!'
    
res = pick_ball_experiment()
print(res)