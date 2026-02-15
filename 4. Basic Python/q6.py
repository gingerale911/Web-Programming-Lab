class Power:
    def pow(self, x, n):
        if n==0:
            return 1
        elif n<0:
            return 1/self.pow(x,-n)
        else: 
            half = self.pow(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x


x=float(input("Enter base x: "))
n=int(input("Enter exp: "))

obj=Power()
result=obj.pow(x,n)

print(f"{x}^{n} = ",result)