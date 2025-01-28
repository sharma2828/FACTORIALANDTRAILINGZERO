def factorial(a):
    x=1
    for i in range(1,a+1):
        x=x*i
    print(f"THE FACTORIAL OF NUMBER {a} IS {x}")
    y=0
    while x%10==0:
        y=y+1
        x=x/10
    print(f"NUMBER OF TRAILING ZEROS IN THE FACTORIAL OF GIVEN NUMBER IS {y}")
factorial(20)        
        


        