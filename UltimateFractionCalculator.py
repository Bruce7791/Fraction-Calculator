# Ultimate Fraction Calculator
# This program is my attempt to make a comprehensive and more powerful fraction calculator.
# https://howchoo.com/g/nddmztjkmwe/dealing-with-fractions-in-python
# https://en.wikibooks.org/wiki/Mathematics_with_Python_and_Ruby/Fractions_in_Python
# https://rosettacode.org/wiki/Farey_sequence
# https://en.wikipedia.org/wiki/Egyptian_fraction
# https://docs.python.org/3/library/statistics.html


from fractions import Fraction
from math import ceil
from statistics import mean
from fractions import Fraction as F

def Farey(a,b):
    n = a.numerator+b.numerator
    d = a.denominator+b.denominator
    return Fraction(n,d)

class Fr(Fraction):
    def __repr__(self):
        return '(%s/%s)' % (self.numerator, self.denominator)
 
 
def farey(n, length=False):
    if not length:
        return [Fr(0, 1)] + sorted({Fr(m, k) for k in range(1, n+1) for m in range(1, k+1)})
    else:
        #return 1         +    len({Fr(m, k) for k in range(1, n+1) for m in range(1, k+1)})
        return  (n*(n+3))//2 - sum(farey(n//k, True) for k in range(2, n+1))

def egypt(f):
    e = int(f)
    f -= e
    parts = [e]
    while(f.numerator>1):
        e = Fraction(1, int(ceil(1/f)))
        parts.append(e)
        f -= e
    parts.append(f)
    return parts

while True:

    print("\nWELCOME TO BRUCE'S ULTIMATE FRACTION CALCULATOR VERSION 1.0")
    print("\nA collection of 50 operations to perform on fractions")

    print("\nSelect operation.")
    print("\n1. Adding Fractions")
    print("2. Subtracting Fractions")
    print("3. Multiplying Fractions")
    print("4. Dividing Fractions")
    print("5. Modulus done on Fractions")
    print("6. Inverting Fractions")
    print("7. Adding Negative Fractions")
    print("8. Subtracting Negative Fractions")
    print("9. Multiplying Negative Fractions")
    print("10. Dividing Negative Fractions")
    print("11. Modulus done on Negative Fractions")
    print("12. Adding Positive & Negative Fractions: First fraction positive, 2nd fraction negative")
    print("13. Subtracting Positive & Negative Fractions: First fraction positive, 2nd fraction negative")
    print("14. Multiplying Positive & Negative Fractions: First fraction positive, 2nd fraction negative")
    print("15. Dividing Positive & Negative Fractions: First fraction positive, 2nd fraction negative")
    print("16. Modulus done on Positive & Negative Fractions: First fraction positive, 2nd fraction negative")
    print("17. Exponents: Returns a decimal number")
    print("18. Exponents: Returns a semi-accurate fraction")
    print("19. GCF: Find the greatest common factor of two numbers - Included here because it is calculated using the Python Fractions module")
    print("20. Farey Reduction")
    print("21. Convert Improper Fractions to Mixed Numbers")
    print("22. Convert Mixed Numbers to Improper Fractions")
    print("23. Make a Farey Sequence of Fractions from a range of numbers")
    print("24. Egyptian Fractions: Shows the components of the fraction")
    print("25. Comparing Fractions by size")
    print("26. GCF-3/4: Find the greatest common factor of three or four numbers - Done with the Python Fractions module")
    print("27. Fraction to Decimal Converter")
    print("28. Fraction to Percentage Converter")
    print("29. Adding Mixed Numbers")
    print("30. Subtracting Mixed Numbers")
    print("31. Multiplying Mixed Numbers")
    print("32. Dividing Mixed Numbers")
    print("33. Modulus done on Mixed Numbers")
    print("34. Adding Fractions to Whole Numbers")
    print("35. Subtracting Fractions from Whole Numbers")
    print("36. Multiplying Fractions from Whole Numbers")
    print("37. Dividing Fractions by Whole Numbers")
    print("38. Modulus with Fractions & Whole Numbers")
    print("39. Decimal to Fraction and Percent converter")
    print("40. Fraction Reducer")
    print("41. Adding three Fractions")
    print("42. Subtracting three Fractions")
    print("43. Multiplying three Fractions")
    print("44. Dividing three Fractions")
    print("45. Equivalent Fractions - Comparing two Fractions")
    print("46. Finding the Mean of four Fractions")
    print("47. Adding a mixed number to a whole number")
    print("48. Subtracting a mixed number from a whole number")
    print("49. Multiplying a whole number and a mixed number")
    print("50. Dividing a whole number by a mixed number")


    # Take input from the user 
    choice = input("\nEnter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50): ")



    if choice == '1':
        print("\n1. Adding Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(a + b)

    elif choice == '2':
        print("\n2. Subtracting Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))       
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(a - b)

    elif choice == '3':
        print("\n3. Multiplying Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(a * b)

    elif choice == '4':
        print("\n4. Dividing Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(a / b)

    elif choice == '5':
        print("\n5. Modulus done on Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(a % b)

    elif choice == '6':
        print("\n6. Inverting Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        print(1/a)

    elif choice == '7':
        print("\n7. Adding Negative Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(-a + -b)

    elif choice == '8':
        print("\n8. Subtracting Negative Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(-a - -b)

    elif choice == '9':
        print("\n9. Multiplying Negative Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(-a * -b)

    elif choice == '10':
        print("\n10. Dividing Negative Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(-a / -b)

    elif choice == '11':
        print("\n11. Modulus done on Negative Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(-a % -b)

    elif choice == '12':
        print("\n12. Adding Positive & Negative Fractions: First fraction positive, 2nd fraction negative")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(a + -b)

    elif choice == '13':
        print("\n13. Subtracting Positive & Negative Fractions: First fraction positive, 2nd fraction negative")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(a - -b)

    elif choice == '14':
        print("\n14. Multiplying Positive & Negative Fractions: First fraction positive, 2nd fraction negative")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(a * -b)

    elif choice == '15':
        print("\n15. Dividing Positive & Negative Fractions: First fraction positive, 2nd fraction negative")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(a / -b)

    elif choice == '16':
        print("\n16. Modulus done on Positive & Negative Fractions: First fraction positive, 2nd fraction negative")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(a % -b)

    elif choice == '17':
        print("\n17. Exponents: Returns a decimal number")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(a ** b) # It returns a float probably because the fraction is impossible to calculate within reason.

    elif choice == '18':
        print("\n18. Exponents: Returns a semi-accurate fraction")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        f = Fraction(a) ** Fraction(b)
        print(Fraction(f).limit_denominator()) # limit_denominator used to get a semi-accurate fraction from exponents.  

    elif choice == '19':
        print("\n19. GCF: Find the greatest common factor of two numbers - Included here because it is calculated using the Python Fractions module")
        from fractions import gcd 
        num1 = int(input("\nEnter First Number: "))
        num2 = int(input("Enter Second Number: "))
        a = gcd(num1, num2)
        print("The Greatest Common Factor of your numbers is", a)

    elif choice == '20':
        print("\n20. Farey Reduction")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        print(Farey(a,b))

    elif choice == '21':
        print("\n21. Convert Improper Fractions to Mixed Numbers")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        quotient = num1 // num2
        remainder = num1 % num2
        a = Fraction(remainder, num2)
        print(quotient, a)

    elif choice == '22':
        print("\n22. Convert Mixed Numbers to Improper Fractions")
        num0 = int(input("\nEnter Whole Number: "))
        num1 = int(input("Enter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        quotient = num0 * num2 + num1
        a = Fraction(quotient, num2)
        print(a)

    elif choice == '23':
        print("\n23. Make a Farey Sequence of Fractions from a range of numbers")
        num1 = int(input("\nEnter 1st number of the range: "))
        num2 = int(input("Enter 2nd number of the range: "))
        print('Farey sequence for the number range that you chose (inclusive):')
        for n in range(num1, num2):
            print(farey(n))

    elif choice == '24':
        print("\n24. Egyptian Fractions: Shows the components of the fraction")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        a = Fraction(num1,num2)
        print(egypt(a))            # Shows the components of the faction
        print(sum(egypt(a)))        # Confirms that these fractions add up to the original value
        
    elif choice == '25':
        print("\n25. Comparing Fractions by size")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        if a > b:
            print(a, "is bigger than", b)
        else:
            print(a, "is smaller than", b)

    elif choice == '26':
        print("\n26. GCF-3/4: Find the greatest common factor of three or four numbers - Done with the Python Fractions module")
        from fractions import gcd 
        print("\nEnter a zero for your fourth number if there are only three numbers to calculate:")
        num1 = int(input("\nEnter First Number: "))
        num2 = int(input("Enter Second Number: "))
        num3 = int(input("Enter Third Number: "))
        num4 = int(input("Enter Fourth Number: "))
        a = gcd(num1, num2)
        b = gcd(num3, num4)
        c = gcd(a, b)
        print("The Greatest Common Factor of your numbers is", c)

    elif choice == '27':
        print("\n27. Fraction to Decimal Converter")
        s = int(input("\nEnter your Numerator: ",))
        t = int(input("Enter your Denominator: ",))
        print("\nHere is your fraction as a decimal:", s/t)

    elif choice == '28':
        print("\n28. Fraction to Percentage Converter")
        s = int(input("\nEnter your Numerator: ",))
        t = int(input("Enter your Denominator: ",))
        print("\nHere is your fraction as a percent:", s/t*100, "%")

    elif choice == '29':
        print("\n29. Adding Mixed Numbers")
        num0 = int(input("\nEnter Whole Number: "))
        num1 = int(input("Enter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        a = num0 + Fraction(num1, num2)
        num3 = int(input("Enter Whole Number: "))
        num4 = int(input("Enter Numerator: "))
        num5 = int(input("Enter Denominator: "))
        b = num3 + Fraction(num4, num5)
        c = a+b
        quotient = c.numerator // c.denominator
        remainder = c.numerator % c.denominator
        d = Fraction(remainder, c.denominator)
        print(quotient, d)

    elif choice == '30':
        print("\n30. Subtracting Mixed Numbers")
        num0 = int(input("\nEnter Whole Number: "))
        num1 = int(input("Enter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        a = num0 + Fraction(num1, num2)
        num3 = int(input("Enter Whole Number: "))
        num4 = int(input("Enter Numerator: "))
        num5 = int(input("Enter Denominator: "))
        b = num3 + Fraction(num4, num5)
        c = a-b
        quotient = c.numerator // c.denominator
        remainder = c.numerator % c.denominator
        d = Fraction(remainder, c.denominator)
        print(quotient, d)

    elif choice == '31':
        print("\n31. Multiplying Mixed Numbers")
        num0 = int(input("\nEnter Whole Number: "))
        num1 = int(input("Enter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        a = num0 + Fraction(num1, num2)
        num3 = int(input("Enter Whole Number: "))
        num4 = int(input("Enter Numerator: "))
        num5 = int(input("Enter Denominator: "))
        b = num3 + Fraction(num4, num5)
        c = a*b
        quotient = c.numerator // c.denominator
        remainder = c.numerator % c.denominator
        d = Fraction(remainder, c.denominator)
        print(quotient, d)

    elif choice == '32':
        print("\n32. Dividing Mixed Numbers")
        num0 = int(input("\nEnter Whole Number: "))
        num1 = int(input("Enter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        a = num0 + Fraction(num1, num2)
        num3 = int(input("Enter Whole Number: "))
        num4 = int(input("Enter Numerator: "))
        num5 = int(input("Enter Denominator: "))
        b = num3 + Fraction(num4, num5)
        c = a/b
        quotient = c.numerator // c.denominator
        remainder = c.numerator % c.denominator
        d = Fraction(remainder, c.denominator)
        print(quotient, d)

    elif choice == '33':
        print("\n33. Modulus done on Mixed Numbers")
        num0 = int(input("\nEnter Whole Number: "))
        num1 = int(input("Enter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        a = num0 + Fraction(num1, num2)
        num3 = int(input("Enter Whole Number: "))
        num4 = int(input("Enter Numerator: "))
        num5 = int(input("Enter Denominator: "))
        b = num3 + Fraction(num4, num5)
        c = a%b
        quotient = c.numerator // c.denominator
        remainder = c.numerator % c.denominator
        d = Fraction(remainder, c.denominator)
        print(quotient, d)

    elif choice == '34':
        print("\n34. Adding Fractions to Whole Numbers")
        num1 = int(input("\nEnter Whole Number: "))
        num2 = int(input("Enter Numerator: "))
        num3 = int(input("Enter Denominator: "))
        a = Fraction(num1)
        b = Fraction(num2, num3)
        print(a + b)
        print("Enter your answer to get the answer back as a Mixed Number")
        num4 = int(input("Enter Numerator: "))
        num5 = int(input("Enter Denominator: "))
        quotient = num4 // num5
        remainder = num4 % num5
        c = Fraction(remainder, num5)
        print(quotient, c)

    elif choice == '35':
        print("\n35. Subtracting Fractions from Whole Numbers")
        num1 = int(input("\nEnter Whole Number: "))
        num2 = int(input("Enter Numerator: "))
        num3 = int(input("Enter Denominator: "))
        a = Fraction(num1)
        b = Fraction(num2, num3)
        print(a - b)
        print("Enter your answer to get the answer back as a Mixed Number")
        num4 = int(input("Enter Numerator: "))
        num5 = int(input("Enter Denominator: "))
        quotient = num4 // num5
        remainder = num4 % num5
        c = Fraction(remainder, num5)
        print(quotient, c)

    elif choice == '36':
        print("\n36. Multiplying Fractions from Whole Numbers")
        num1 = int(input("\nEnter Whole Number: "))
        num2 = int(input("Enter Numerator: "))
        num3 = int(input("Enter Denominator: "))
        a = Fraction(num1)
        b = Fraction(num2, num3)
        print(a * b)

    elif choice == '37':
        print("\n37. Dividing Fractions by Whole Numbers")
        num1 = int(input("\nEnter Whole Number: "))
        num2 = int(input("Enter Numerator: "))
        num3 = int(input("Enter Denominator: "))
        a = Fraction(num1)
        b = Fraction(num2, num3)
        print(a / b)

    elif choice == '38':
        print("\n38. Modulus with Fractions & Whole Numbers")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Whole Number: "))
        a = Fraction(num1, num2)
        b = Fraction(num3)
        print(a % b)

    elif choice == '39':
        print("\n39. Decimal to Fraction and Percent converter")
        import fractions
        s = input("\nEnter a decimal number to have it turned into a fraction and a percent: ", )
        t = float(s)
        f = fractions.Fraction(s)
        print("Here is your decimal number as a fraction and a percent:")
        print("%s = %s" % (s, f), "&", t*100,"%")

    elif choice == '40':
        print("\n40. Fraction Reducer")
        from fractions import Fraction
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        print("Your fraction reduces to",a)

    elif choice == '41':
        print("\n41. Adding three Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        num5 = int(input("Enter Numerator: "))
        num6 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        c = Fraction(num5, num6)
        print(a + b + c)

    elif choice == '42':
        print("\n42. Subtracting three Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        num5 = int(input("Enter Numerator: "))
        num6 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        c = Fraction(num5, num6)
        print(a - b - c)

    elif choice == '43':
        print("\n43. Multiplying three Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        num5 = int(input("Enter Numerator: "))
        num6 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        c = Fraction(num5, num6)
        print(a * b * c)

    elif choice == '44':
        print("\n44. Dividing three Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        num5 = int(input("Enter Numerator: "))
        num6 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        c = Fraction(num5, num6)
        print(a / b / c)

    elif choice == '45':
        print("\n45. Equivalent Fractions - Comparing two Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        if a == b:
            print(a, "and", b, "are equivalent fractions - *all fractions are automatically reduced in the answer")
        else:
            print(a, "and", b, "are not equivalent fractions - *all fractions are automatically reduced in the answer")

    elif choice == '46':
        print("\n46. Finding the Mean of four Fractions")
        num1 = int(input("\nEnter Numerator: "))
        num2 = int(input("Enter Denominator: "))
        num3 = int(input("Enter Numerator: "))
        num4 = int(input("Enter Denominator: "))
        num5 = int(input("Enter Numerator: "))
        num6 = int(input("Enter Denominator: "))
        num7 = int(input("Enter Numerator: "))
        num8 = int(input("Enter Denominator: "))
        a = Fraction(num1, num2)
        b = Fraction(num3, num4)
        c = Fraction(num5, num6)
        d = Fraction(num7, num8)
        e = mean([F(a), F(b), F(c), F(d)])
        print("The mean of your four fractions is", e)

    elif choice == '47':
        print("\n47. Adding a mixed number to a whole number")
        num0 = int(input("\nEnter Whole Number: "))
        a = num0
        num3 = int(input("Enter Whole Number: "))
        num4 = int(input("Enter Numerator: "))
        num5 = int(input("Enter Denominator: "))
        b = num3 + Fraction(num4, num5)
        c = a+b
        quotient = c.numerator // c.denominator
        remainder = c.numerator % c.denominator
        d = Fraction(remainder, c.denominator)
        print(quotient, d)

    elif choice == '48':
        print("\n48. Subtracting a mixed number from a whole number")
        num0 = int(input("\nEnter Whole Number: "))
        a = num0 
        num3 = int(input("Enter Whole Number: "))
        num4 = int(input("Enter Numerator: "))
        num5 = int(input("Enter Denominator: "))
        b = num3 + Fraction(num4, num5)
        c = a-b
        quotient = c.numerator // c.denominator
        remainder = c.numerator % c.denominator
        d = Fraction(remainder, c.denominator)
        print(quotient, d)

    elif choice == '49':
        print("\n49. Multiplying a whole number and a mixed number")
        num0 = int(input("\nEnter Whole Number: "))
        a = num0 
        num3 = int(input("Enter Whole Number: "))
        num4 = int(input("Enter Numerator: "))
        num5 = int(input("Enter Denominator: "))
        b = num3 + Fraction(num4, num5)
        c = a*b
        quotient = c.numerator // c.denominator
        remainder = c.numerator % c.denominator
        d = Fraction(remainder, c.denominator)
        print(quotient, d)

    elif choice == '50':
        print("\n50. Dividing a whole number by a mixed number")
        num0 = int(input("\nEnter Whole Number: "))
        a = num0 
        num3 = int(input("Enter Whole Number: "))
        num4 = int(input("Enter Numerator: "))
        num5 = int(input("Enter Denominator: "))
        b = num3 + Fraction(num4, num5)
        c = a/b
        quotient = c.numerator // c.denominator
        remainder = c.numerator % c.denominator
        d = Fraction(remainder, c.denominator)
        print(quotient, d)

    else:
        print("Invalid input")

    while True:
    
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break