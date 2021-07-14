import numpy as np

def sigmoid(x):
  # Sigmoid activation function: f(x) = 1 / (1 + e^(-x))
  return 1 / (1 + np.exp(-x))

def deriv_sigmoid(x):
  # Derivative of sigmoid: f'(x) = f(x) * (1 - f(x))
  fx = sigmoid(x)
  return fx * (1 - fx)

def mse_loss(y_true, y_pred):
  # y_true and y_pred are numpy arrays of the same length.
  return ((y_true - y_pred) ** 2).mean()
inp = " "
#основные параметры
happiness = 0
fitness = 0
training = 0
love = 0
fluffiness = 0
jump = 0
speed = 0
intelligence = 0
scent = 0
strength = 0
#общие параметры
beauty = 0
physical_abilities = 0
well_being = 0
#счет
score = 0

#Действия
#Покормить сухим кормом  //happiness+1, fitness -1, love +2, fluffiness +2, speed -1
#Покормить влажным кормом //happiness+2, fitness -2, love +2, speed -1, strength +1
#Покормить человеческой едой //happiness+3, fitness -4, love +3, speed -1, scent +1
#Попоить водой // fluffiness +1, fitness +2
#Попоить молоком // happiness +2, love +1, fluffiness +4
#Погладить // happiness +1, love +1, fluffiness +2
#Поиграть с удочкой// fitness +3, training +2, jump +2, speed +1
#Поиграть рукой// hapiness -1. love -2, strength +3, intelligence +1
#Поиграть  в догонялки // happiness -2, love -2, training +1, jump +2, speed+5
#Поиграть с лазерной указкой // happiness -1, speed +4, intelligence +3, training +1
#Напугать огурцом // happiness -4,intellegence -2, speed +6, jump +10
#Сходить к ветеринару// happiness -3. love -2, fluffiness +1, intellegence +2, scent +1, strength +2
#Накормить витаминами// happiness -1, love -1, allother +1
#Познакомить с другой кошкой //happiness +3, love +4

for i in range (10):
    inp = input()
    if inp == "сухим":
        happiness =happiness+1
        fitness = fitness -1
        love = love +2
        fluffiness = fluffiness +2
        speed = speed - 1
    
    if inp == "влажным" :
        happiness =happiness+2
        fitness = fitness -2
        love = love +2
        strength =strength +1
        speed = speed - 1
    
    
    if inp == "человеческой" :
        happiness = happiness+3
        fitness = fitness -4 
        love = love +3
        speed = speed -1
        scent = scent +1
    
    if inp == "вода" :
        fluffiness = fluffiness +1
        fitness = fitness +2
    
    if inp == "молоко" :
        happiness = happiness +2
        love =  love +1
        fluffiness =  fluffiness +4
    
    if inp == "погладить" :
        happiness = happiness +1
        love = love +1
        fluffiness =  fluffiness +2
    
    if inp =="удочка" :
        fintess = fitness +3
        training = training +2
        jump = jump +2
        speed = speed +1
    
    if inp == "рука" :
        happiness = happiness -1
        love = love -2
        strength = strength +3
        intelligence = intelligence +1
    
    if inp == "догонялки" :
        happiness -2
        love = love -2
        training = training +1
        jump = jump +2
        speed = speed+5
     
    if inp == "указка":
        happiness = happiness -1
        speed = speed +4
        intelligence = intelligence +3
        training = training +1
    
    if inp == "огурец" :
        happiness = happiness -4
        intelligence = intelligence -2
        speed = speed +6
        jump = jump +10
    
    if inp == "ветеринар":
        happiness = happiness -3
        love = love -2
        fluffiness  = fluffiness +1
        intelligence = intelligence +2
        scent = scent +1
        strength = strength +2
    
    if inp == "витамин" :
        happiness = happiness -1
        love = love -1
        fitness = fitness +1
        training = training +1
        fluffiness = fluffiness +1
        jump = jump +1
        speed = speed +1
        intelligence = intelligence +1
        scent = scent +1
        strength = strength +1    
    
    if inp == "кошка" :
        love = love +4
        happiness =happiness +3
        strength = strength -2
        fitness = fitness -1
    
    beauty = fluffiness + fitness 
    physical_abilities = jump +speed +strength +scent
    well_being = happiness + love +training +intelligence
    score = (beauty+physical_abilities+well_being)/3
    print ("Красота: " + str(beauty) +"  Способности: "+ str(physical_abilities) + " Благополучие: " + str(well_being) + " Общий счет: "+ str(int((score))))
    print ("Осталось ходов:" + str(9-i))
print ("Очки на конец игры:")
print ("Красота: " + str(beauty) +"  Способности: "+ str(physical_abilities) + " Благополучие: " + str(well_being) + " Общий счет: "+ str(int((score))))