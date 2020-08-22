height = int(input("Enter the height:\n"))

width = int(input("Enter the width:\n"))

gap=" "

def print_rectangle(height, width):
    for i in range(height):
        if i == 0 or i == height-1:
            print(width * '*')
        else: 
            print('*' + gap*(width-2) + '*')


print_rectangle(height,width) 