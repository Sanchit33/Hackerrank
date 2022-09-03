def print_formatted(number):
    # your code goes here
    j = len(str(bin(number))[2:])
    for i in range(1, number+1):
            print(str(i).rjust(j,' '),oct(i)[2:].rjust(j,' '),hex(i)[2:].upper().rjust(j,' '),bin(i)[2:].rjust(j,' '))    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
