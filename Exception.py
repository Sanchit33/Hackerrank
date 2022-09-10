# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
for i in range(a):
    b,v = input().split()       
    try:
        print(int(b)//int(v))
    except Exception as e:
        print("Error Code:", e)  
