def main():
    #write your code below this line
    
    text = input('Give a string:')
    num = int(input('Give an integer:'))
    num2 = float(input('Give a float:'))
    ans = bool(input('Give a boolean:'))
    
#     print(f'You gave the string {text}')
#     print(f'You gave the integer {num}')
#     print(f'You gave the float {num2}')
#     print(f'You gave the boolean {ans}')

    print('You gave the string ' + text')
    print('You gave the integer ' + str(num)')
    print('You gave the float ' + str(num2)')
    print('You gave the boolean ' + str(ans)')
    
    

if __name__ == '__main__':
    main()

    
