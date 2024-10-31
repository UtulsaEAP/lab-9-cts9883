def int_to_reverse_binary(num1):
    if num1 == 0:
        binary_val = [0]
    else:
        binary_val = []
        while num1 >= 1:
            binary_val.append(num1 % 2)
            num1 = num1 // 2
    return "".join(map(str, binary_val))
    

def string_reverse(input_string): 
    return input_string[::-1]
    
if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = (int_to_reverse_binary(user_input))
    binary_string = (string_reverse(binary_string))
    
    print(binary_string)