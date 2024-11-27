#Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3?
def cube(num):
    return num*num*num
def cubes(num):
    if (num%3)== 0:
        return cube(num)
    else:
        False

    
print(cubes(99))