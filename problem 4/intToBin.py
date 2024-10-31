def int_to_reverse_binary(num1):
    binary_val = []
    while num1 >= 1:
        binary_val.append(num1 % 2)
        num1 = num1 // 2
    return str(binary_val)

def string_reverse(input_string): 
    reverse_input = str(str(input_string)[::-1])    
    return str(reverse_input)

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(str(binary_string))