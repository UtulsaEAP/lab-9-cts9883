def feet_to_steps(user_feet):
   steps = int(user_feet/2.5)
   return steps

if __name__ == '__main__':
    user_feet = float(input())
    user_steps = feet_to_steps(user_feet)
    
    print(user_steps)
    feet_to_steps(5280)