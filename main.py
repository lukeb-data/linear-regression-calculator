#Linear regression model without using sklearn

import matplotlib.pyplot as plt


x_values = []
y_values = []
num = 0

def get_info():
    
    #X Values collect
    collect_state = True

    print("Enter the x values of your data. Else, enter 'done' when complete:")
    
    while collect_state != False: 
       val = input("X:")
       if val == 'done':
           collect_state = False
       else:
           x_values.append(int(val))
    
    #Y Values collect
    collect_state = True

    print("Now enter the y values of your data. Else, enter 'done' when complete:")
    
    while collect_state != False: 
       val = input("Y:")
       if val == 'done':
           collect_state = False
       else:
           y_values.append(int(val))
    return x_values, y_values


def change():
    n = len(x_values)
    index = 0
    temp = 0
    total = 0
    for i in range (n):
        temp = x_values[index] * y_values[index]
        total = total + temp
        index = index + 1
    calc_one = n * total
    calc_two = sum(x_values) * sum(y_values)

    index = 0
    temp = 0
    total = 0
    for i in range (n):
        temp = x_values[index] * x_values[index]
        total = total + temp
        index = index + 1
    calc_three = n * total
    calc_four = sum(x_values) ** 2
    
    num = (calc_one - calc_two)/(calc_three - calc_four)
    return num

def initial(num):
    calc_five = sum(y_values)
    calc_six = sum(x_values) * num
    num_two = (calc_five - calc_six) / len(x_values)
    return num_two




get_info()
num = change()
num_two = initial(num)
print(f"Your regression line is: y = {num}x + {num_two}")

plt.scatter(x_values, y_values, color='blue', label='Data Points')
regression_y = [num * x + num_two for x in x_values]

plt.plot(x_values, regression_y, color='red', label='Regression Line')
plt.title("Linear Regression Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)
plt.show()

        
