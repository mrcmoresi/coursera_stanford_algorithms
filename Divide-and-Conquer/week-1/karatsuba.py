def karatsuba(number1: int, number2: int) -> int:
    """Calculate the katsuba algortihm for integer multiplication

    Args:
        number1 (int): first integer 
        number2 (int): second integer
    
    Returns:
        result of the multiplication of the two integers
    
    """
    len_x1 = len(str(number1))
    len_x2 = len(str(number2))

    if len_x1 < 2 or len_x2 < 2:
        return number1 * number2

    max_len = max(len_x1, len_x2)
    split_pos = int(max_len/2)
    a = number1 // (10**split_pos)
    b = number1 % (10**split_pos)
    c = number2 // (10**split_pos)
    d = number2 % (10**split_pos)


    z0 = karatsuba(a,c)
    z1 = karatsuba(b,d)
    z2 = karatsuba(a+b,c+d) - z0 - z1
    
    return (10**(2*split_pos) * z0) + (z2 * 10**(split_pos)) + z1

if __name__=='__main__':
    #int1 = input("Please insert the first integer: ")
    #int2 = input("Please insert the second integer: ")
    int1 = 3141592653589793238462643383279502884197169399375105820974944592
    int2 = 2718281828459045235360287471352662497757247093699959574966967627
    res = karatsuba(int(int1), int(int2))
    print("The result is {}".format(res))
    print("The result is {}".format(res == int1 * int2))
    print(int1*int2)
    print(res)
