#without optimization
def minion_game(string):
    # your code goes here
    scount = {}
    kcount = {}
    lis = list(string)
    ui = list()
    iu = list()
    for i in range(len(string)):
        if lis[i] in string:
            for k in range(len(string[i:])):
                ui.append(string[i:i+k+1])
        else:
            for k in range(len(string[i:])):
                iu.append(string[i:i+k+1])          
    
    stuart = []
    kevin = []
    vol = "AEIOU"
    for i in range(0, len(ui)):
        if ui[i][:1] == "A" or ui[i][:1] == "E" or ui[i][:1] == "I" or ui[i][:1] == "O" or ui[i][:1] == "U":
            kevin.append(ui[i])
        else:
            stuart.append(ui[i]) 
    for i in stuart:
        if i not in scount:
            scount[i] = 1
        else:
            scount[i] = scount[i] + 1 
    for i in kevin:
        if i not in kcount:
            kcount[i] = 1
        else:
            kcount[i] = kcount[i] +1
    si = []
    ki = []
    for (j,k) in scount.items():
        si.append(k)
    for (j,k) in kcount.items():
        ki.append(k)          
    if sum(si) == sum(ki):
        p = "Draw"
        return print(p)
    elif sum(si)<sum(ki):
        p = "Kevin"
        s = sum(ki)
        return print(p,s)        
    else:
        p = "Stuart"
        s = sum(si)    
        return print(p,s)
    
    
    
    
    
#With Optimization
def minion_game(string):
    # your code goes here
   s1  = 0
   s2 = 0
   vow = 'AEIOU'
   for i in range(0,len(s)):
        if s[i] in vow:
            s1 = s1 + len(s[i:])
        else:
             s2 = s2 + len(s[i:])
   if s1 > s2:
        print("Kevin", s1)
   elif s1 < s2:
        print("Stuart", s2)
   else:
        print("Draw")             
    
   
