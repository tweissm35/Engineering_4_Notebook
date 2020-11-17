def quadSolve(a,b,c):#function called quadSolve that takes three inputs
        import math

        disc=b**2-4*a*c#gets the discriminant

        if disc < 0:#if negative
                print("No real roots")
                return ["No real roots"]
        elif disc == 0:#if zero
                return [-b/(2*a)]#return formula w/o the discriminant
        else:#otherwise
                return [(-b-math.sqrt(b**2-4*a*c))/(2*a),(-b+math.sqrt(b**2-4*a*c))/(2*a)]#full quadratic formula

print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c = 0")
a =int(input("Enter a: "))#gets input for a
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print(quadSolve(a,b,c))#print result
