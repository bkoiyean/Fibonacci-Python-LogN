
print('FIBONACCI FINDER')

def fibonacci(number):
    count_loop = 0
    fibo_list = [None] * (number + 1)
    fibo_list[1] = 1
    fibo_list[2] = 1
    fibo_list[3] = 2
    binary_str = bin(number)[2:]

    count_binary_step = 0
    fibo_index = 1
    while fibo_index < number:
        count_loop += 1
        count_binary_step += 1
        fibo_index =  fibo_index * 2 + int(binary_str[count_binary_step])
        if fibo_list[fibo_index] == None and int(binary_str[count_binary_step]) == 0:
            x = int(fibo_index/2)
            fibo_list[fibo_index] = fibo_list[x]*fibo_list[x] + 2*fibo_list[x]*fibo_list[x-1]
            fibo_list[fibo_index - 1] = fibo_list[x]*fibo_list[x] + fibo_list[x-1]*fibo_list[x-1]
        elif fibo_list[fibo_index] == None and int(binary_str[count_binary_step]) == 1:
            x = int((fibo_index - 1)/2)
            fibo_list[fibo_index] = 2*fibo_list[x]*fibo_list[x] + fibo_list[x-1]*fibo_list[x-1] + 2*fibo_list[x]*fibo_list[x-1]
            fibo_list[fibo_index - 1] = fibo_list[x]*fibo_list[x] + 2*fibo_list[x]*fibo_list[x-1]

    print('Fibonacci of',number,' is calculated as:',fibo_list[number],'in',count_loop,'loops! ')

while True:
    try: 
        number = int(input('Enter number: '))
        if number == 0: print('Fibonacci of',number,' is calculated as: 0 in 0 loops! ')
        elif number == 1 or number == 2: print('Fibonacci of',number,' is calculated as: 1 in 0 loops! ')
        else: fibonacci(number)
    except: break


