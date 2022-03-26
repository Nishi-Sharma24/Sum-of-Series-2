#Find the sum of series:1-1/2!+1/3!-1/4!...1/n!
n=int(input("Enter the number:"))
s=0
p=0
for x in range(1,n+1):
        f=1
        for y in range(n,1,-1):
           f*=y
        
        p=(-1)**x+1*(1/f)
        
        s=s+p
print("The sum is",s)
input()       
