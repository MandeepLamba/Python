symbols=['!', '@', '#', '$', '%', '&', '*']
def get(i):
    count2=count1=0
    temp1=[]
    temp2=[]
    if len(i)>=7:
        for j in symbols:
            if j in i:
                if j not in temp1:
                    temp1.append(j)
                    count1+=1
                    
        if count1>=2:
            for x in nums:
                if x in i:
                    if x not in temp2:
                        temp2.append(x)
                        count2+=1
        if count2>=2:
            return "Strong"
        else:
            return "Weak"                     
    else:
        return "Weak"

print(get(str(input("Enter Your Password: "))))