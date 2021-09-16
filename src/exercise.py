def main():
    #write your code below this line
    
    text = input('Give a string:')
    num = int(input('Give an integer:'))
    num2 = float(input('Give a float:'))
    ans = input('Give a boolean:')
    
    print('You gave the string ' + text)
    print('You gave the integer ' + str(num))
    print('You gave the float ' + str(num2))
    
    # if boolean input is non-empty it's always True, so a workaround is:
    if ans == 'True':
        print('You gave the boolean ' + ans)
    elif ans == 'False':
        print('You gave the boolean ' + ans)
        
    
    

if __name__ == '__main__':
    main()

    
