##Created by Keith Poore
##Start Date: April 24, 2008
##Purpose: To use Pygame to make a grapgh using user input data of a function.
##Functions accepted are: Absolute Value, Polynomial, Polynomial Rational,  Trigonometry

#open pygame and string class
import pygame
from pygame import *
from pygame.locals import *
from string import *
from math import *


##ask for function and display sample functions
print ("This program can only handle 2 x values with a single digit powers. \neg:-2x^2-3x+90")
print ("You can use an equation with 2 x values, both with powers. eg: .05x^4-4x^3")


print ("What is your function?")
func = raw_input()
##convert input to string for parseing
sFunc = str(func)
init()
pygame.font.init()
font =  pygame.font.Font (None,30)
size = width, height = 500, 500
screen = display.set_mode(size)
## make a count of how many x values there are
xNum = 0
for i in range (len(sfunc)):
        if func [i] == 'x':
            xNum += 1

##def multivariable (func, xNum):
##	if xNum > 0:
##		for i in range(len(func)):
##			if func[i] == 'x':
##        			##split at x
##			        split1 = split1 + func.split('x')
##	if xNum == 0:
##		return(multivaribale (func, xNum-1))

def pointsOnGraph (func, xNum):##a function to figure out the points of the function
    p = []
    n = 0
    split1=[]
    split2 = str
    ## split the function up into the equation components at the 'x'
    for i in range(len(func)):
        if func[i] == 'x':
        ##split at x
            split1 = split1 + func.split('x')

    if split1[0] == 'cos' or split1 [0] == 'sin' or split1[0] == 'tan':
        if split1 [0] == 'cos':
                a = cos

                for x in range (-250,250):##the values to be used on the graph
                        y = cos(x)## y is equal to the lambda expressions
                        p = p +[[x  + (width / 2) ]+[y +(height / 2) ]]## create a list of points
                
                return p
        elif split1[0] == 'sin':
                a = sin
                for x in range (-250,250):##the values to be used on the graph
                        y = sin(x*300)*200## y is equal to the lambda expressions
                        p = p +[[x  + (width / 2) ]+[y +(height / 2) ]]## create a list of points
                
                return p
        else:
                a = tan
                for x in range (-250,250):##the values to be used on the graph
                        y = (tan(x))*100## y is equal to the lambda expressions
                        p = p +[[x  + (width / 2) ]+[y +(height / 2) ]]## create a list of points
                
                return p

    if len(split1[0]) == 0:
        ## if there is no coeffcient in front of 'x' then it will = 1
        split1[0] = 1
    else:
        split1[0] = float(split1[0])

    if xNum == 3:
            ##3 powers no constants
            if split1[1][0] == '^' and split1[2][0] == '^' and split1[3][0] == '^':
                    ## use form a^x + b^y + c^z
                    ## x^1 +x^2 + x^3
                    a = -float(split1[0])
                    split1 [1] = split1[1].strip('^')
                    split1 [2] = split1[2].strip('^')
                    split1 [3] = split1[3].strip('^')
                    e3 = int(split1[3])
                    ##if statement to check the last sign ('+', '-')
                    if split1[2][1] == '+':
                            e2,c = split1[2].split ('+')
                            e2 = int(e2)
                            c = float (c)
                            ## if statement to check first sign
                            if split1[1][1] == '+':
                                    e1,b = split1[1].split('+')
                                    e1,b = int(e1), float(b)
                                    L1 = (lambda a,x,e1: a*x**e1)
                                    L2 = (lambda b,x,e2: b*x**e2)
                                    L3 = (lambda c,x,e3: c*x**e3)
                                    for x in range (-250,250):##the values to be used on the graph
                                        y = L1(a,x,e1) - L2 (b,x,e2) - L3 (c,x,e3)## y is equal to the lambda expressions
                                        p = p +[[x  + (width / 2) ]+[y +(height / 2) ]]## create a list of points
                                    print (p)
                                    return (p)
                            elif split1[1][1] == '-':
                                    e1,b = split1[1].split('-')
                                    e1,b = int(e1), float(b)
                                    L1 = (lambda a,x,e1: a*x**e1)
                                    L2 = (lambda b,x,e2: b*x**e2)
                                    L3 = (lambda c,x,e3: c*x**e3)
                                    for x in range (-250,250):##the values to be used on the graph
                                        y = L1(a,x,e1) + L2 (b,x,e2) - L3 (c,x,e3)## y is equal to the lambda expressions
                                        p = p +[[x  + (width / 2) ]+[y +(height / 2) ]]## create a list of points
                                    print (p)
                                    return (p)
                                
                                    
    elif xNum == 2:
            
        ##2 x, 2 power, no constant
        if split1[1][0] == '^' and split1[2][0] == '^' and len (split1[2]) <= 3 :
                ## use the form (ax +bx)
                ## because the origin is at the top left hand corner, 'a' value must be '-'
                a = -float(split1[0])
                split1 [1] = split1[1].strip('^')
                split1[2] = split1[2].strip('^')
                e2 = int (split1[2])##The second Power
                if split1 [1][1] == '+':
                        
                        e1,b = split1[1].split('+')##The first power and 2nd coeffient
                        e1,b = int(e1.strip('^')), float(b)
                        L1 = (lambda a,x,e1: a*x**e1)##Set Lambda expressions to do the math
                        L2 = (lambda b,x,e2: b*x**e2)
                        print (a, b,e1, e2)
                        for x in range (-250,250):##the values to be used on the graph
                                y = L1(a,x,e1) - L2 (b,x,e2)## y is equal to the lambda expressions
                                p = p +[[x  + (width / 2) ]+[y +(height / 2) ]]## create a list of points
                        print (p)
                        return (p)
            
                elif split1 [1][1] == '-':
                        e1,b = split1[1].split('-')
                        e1,b = int(e1.strip('^')), float(b)
                        L1 = (lambda a,x,e1: a*x**e1)##Set Lambda expressions to do the math
                        L2 = (lambda b,x,e2: b*x**e2)
                        b = float(b)
                        for x in range (-250,250):
                                y = L1(a,x,e1) + L2 (b,x,e2)
                                p = p +[[x  + (width / 2) ]+[y  + (height / 2) ]]
                        print (p)
                        return (p)

        ##2 x, 2 power, constant
        elif split1[1][0] == '^' and split1[2][0] == '^' and split1 [2][2] == '+' or split1[1][0] == '^' and split1[2][0] == '^' and split1 [2][2] == '-':
                a = -float(split1[0])
                split1[1] = split1[1].strip('^')
                split1[2] = split1[2].strip('^')
                if split1 [1][1] == '+':
                        e1,b = split1[1].split('+')
                        e1,b = int(e1), float(b)
                        if split1[2][1] == '+':
                                e2,c = split1[2].split('+')
                                e2,c = int(e2),float(c)
                                L1 = (lambda a,x,e1: a*x**e1)
                                L2 = (lambda b,x,e2: b*x**e2)
                                L3 = (lambda c : c)
                                for x in range (-250,250):   
                                        y = L1(a,x,e1) - L2 (b,x,e2)
                                        p = p +[[x  + (width / 2) ]+[y + c +(height / 2) ]]
                                print (p)
                                return (p)

                        elif split1[2][1] == '-':
                                e2,c = split1[2].split('-')
                                e2,c = int(e2),float(c)
                                L1 = (lambda a,x,e1: a*x**e1)
                                L2 = (lambda b,x,e2: b*x**e2)
                                L3 = (lambda c : c)
                        for x in range (-250,250):   
                                y = L1(a,x,e1) - L2 (b,x,e2)
                                p = p +[[x  + (width / 2) ]+[y - c +(height / 2) ]]
                        print (p)
                        return (p)
                                
            
                elif split1 [1][1] == '-':
                        e1,b = split1[1].split('-')
                        e1,b = int(e1), float(b)
                        if split1[2][1] == '+':
                                e2,c = split1[2].split('+')
                                e2,c = int(e2),float(c)
                                L1 = (lambda a,x,e1: a*x**e1)
                                L2 = (lambda b,x,e2: b*x**e2)
                                L3 = (lambda c : c)
                                for x in range (-250,250):   
                                        y = L1(a,x,e1) - L2 (b,x,e2)
                                        p = p +[[x  + (width / 2) ]+[y + c +(height / 2) ]]
                                print (p)
                                return (p)

                        elif split1[2][1] == '-':
                                e2,c = split1[2].split('-')
                                e2,c = int(e2),float(c)
                                L1 = (lambda a,x,e1: a*x**e1)
                                L2 = (lambda b,x,e2: b*x**e2)
                                L3 = (lambda c : c)
                        for x in range (-250,250):   
                                y = L1(a,x,e1) - L2 (b,x,e2)
                                p = p +[[x  + (width / 2) ]+[y - c +(height / 2) ]]
                        print (p)
                        return (p)



##2 x, 1 power, constant
        elif split1[1][0] == '^' and split1[2][0]== '-' or split1 [2][0] == '+':
                a = -float(split1[0])
                split1 [1] = split1[1].strip('^')
                if split1 [1][1] == '+':
                        e,b = split1[1].split('+')
                        e,b = int (e),float(b)
                        if split1[2][0] == '+':
                                c = float(split1[2].strip('+'))
                                L1 = (lambda a,x,e,: (a * x**e))
                                L2 = (lambda b,x: (b*x ))
                                for x in range (-250,250):   
                                    y = L1(a,x,e) - L2(b,x)
                                    p = p +[[x  + (width / 2) ]+[y - c +(height / 2) ]]
                                return (p)
                        
                        elif split1[2][0] == '-':
                                c = float(split1[2].strip('-'))
                                L1 = (lambda a,x,e,: (a * x**e))
                                L2 = (lambda b,x: (b*x))
                                for x in range (-250,250):   
                                    y = L1(a,x,e) - L2(b,x)
                                    p = p +[[x  + (width / 2) ]+[y + c +(height / 2) ]]
                                return (p)

                elif split1 [1][1] == '-':
                        e,b = split1[1].split('-')
                        e,b = int (e),float(b)
                        if split1[2][0] =='+':
                                c = float(split1[2].strip('+'))
                                L1 = (lambda a,x,e,: (a * x**e))
                                L2 = (lambda b,x: (b*x ))
                                for x in range (-250,250):   
                                    y = L1(a,x,e) + L2(b,x)
                                    p = p +[[x  + (width / 2) ]+[y - c + (height / 2) ]]
                                return (p)

                        elif split1[2][0] == '-':
                                c = float (split1[2].strip('-'))
                                L1 = (lambda a,x,e,: (a * x**e))
                                L2 = (lambda b,x: (b*x ))
                                for x in range (-250,250):   
                                    y = L1(a,x,e) + L2(b,x)
                                    p = p +[[x  + (width / 2) ]+[y +c + (height / 2) ]]
                                return (p)
            


        ## 2x, 1 power,  no constant
        elif split1[1][0] == '^':
                a = -float(split1[0])
                
                split1 [1] = split1[1].strip('^')
                if split1 [1][1] == '+':
                    e,b = split1[1].split('+')
                    e,b = int(e),float(b)
                    L1 = (lambda a,x,e,: (a * x**e))
                    L2 = (lambda b,x: (b*x ))
                    for x in range(float(-width/2.0), float(width/2.0), 1):  
                            y = L1(a,x,e) - L2(b,x)
                            p = p +[[x + (width/2)]+[y + (height / 2) ]]
                    return (p)
            
                elif split1 [1][1] == '-':
                    split1[1],split2 = split1[1].split('-')
                    for x in range(float(-width/2.0), float(width/2.0), 1):   
                            y = L1(a,x,e) + L2(b,x)
                            p = p +[[x + (width/2)]+[y + (height / 2) ]]
                    return (p)
                        


##1 x, no power, constant
    elif xNum == 1:
        
        if split1 [1][0] == '+':
                m = -float(split1[0])
                b = float(split1[1].strip ('+'))
                L = (lambda m,x,b: m * x - b)
                for i in range (-250,250):  
                    y = L(m,i,b)
                    p = p +[[i  + (width / 2)]+[y + (height / 2) ]]
                return p
        elif split1 [1][0] == '-':
                m = -float(split1[0])
                b = float(split1[1].strip ('-'))
                L = (lambda m,x,b: m * x + b)
                for i in range (-250,250):  
                    y = L(m,i,b)
                    p = p +[[i  + (width / 2)]+[y + (height / 2) ]]
                return p
            


        ##1 x, 1 power,constant 
        elif split1[1][0] == '^':
                m = -float(split1[0])
                split1 [1] = split1[1].strip('^')
                if split1 [1][1] == '+':
                        split1[1],split2 = split1[1].split('+')
                        e = float(split1[1])
                        b = float(split2)
                        L = (lambda m,x,e,b: m * x **e - b)
                        print (L)
                        for i in range (-250,250):
                                y = L(m,i,e,b)
                                p = p +[[i  + (width / 2)]+[y + (height / 2) ]]
                        return p

                elif split1 [1][1] == '-':
                        
                        m = -float(split1[0])
                        split1 [1] = split1[1].strip('^')
                        if split1 [1][1] == '-':
                                split1[1],split2 = split1[1].split('-')
                                e = float(split1[1])
                                b = -float(split2)
                                L = (lambda m,x,e,b: m * x **e - b)
                                for i in range (-250,250):
                                        y = L(m,i,e,b)
                                        p = p +[[i  + (width / 2)]+[y + (height / 2) ]]
                                return p
            
            


screen.fill ((255, 255, 255))
display.flip()

def drawScene (screen, p,func):
        POG = [int]## create a list of int points on a graph
        POG = p ## the points are equal to the float points which is cast as an integer
        s = font.render(sFunc, 1, (255,0,0))## takes the string of the function and displays it at (0,0), red
        screen.blit(s, (0,0))
        display.flip()
        
        screen.fill((255, 255, 255))
        ##Draw Cartisian Plane
        draw.line (screen, (0, 0, 0), (width / 2, 0), (width/2, height))
        draw.line (screen, (0, 0, 0), (0, height / 2), (width, height / 2))
        display.flip()
        for i in range (len(p) - 1):## graph the points
            draw.line (screen, (100, 100, 100) , POG[i], POG[i + 1])
            display.flip()
        screen.blit(s, (0,0))
        display.flip()
drawScene(screen, pointsOnGraph (func, xNum),func)

## to escape
print ("To exit, press enter:")
escape = raw_input()
quit()
