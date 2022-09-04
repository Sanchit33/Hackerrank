def print_rangoli(size):
    # your code goes here
    c = "abcdefghijklmnopqrstuvwxyz"
    l = 5
    lens = c[n-1::-1] + c[1:n]
    b = len("-".join(lens))
    for i in range(1,n):
        print('-'.join(c[n-1:n-i:-1]+c[n-i:n]).center(b,'-'))
    for i in range(n,0,-1):
        print('-'.join(c[n-1:n-i:-1]+c[n-i:n]).center(b,'-'))    
      

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
