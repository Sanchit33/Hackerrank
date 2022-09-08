def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0,n,k):
        newstr = ''
        sub_str = string[i:i+k]
        for c in sub_str:
            if c not in newstr:
                newstr += c
        print(newstr)
       
            
        
           
   
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
