#print('NAZWA_GRUPY No Problem, ID DanielWap, ID Developer ppatyk')

def Division (A, B):
    if(B==0):
        print('nie dziel przez 0!')
        return 0.0
    else:
        return A/B



A = float(input("Enter Number A : "))
B = float(input("Enter Number B : "))
result = Division(A,B)
print(A, " / ", B, " = ", result)



