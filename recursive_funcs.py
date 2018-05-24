def recProduct(a,b): #Returns the product of two numbers using recursion

    if b == 0:
        return 0

    if b<0:
        return -a + recProduct(a,b+1)

    if b>0:
        return a + recProduct(a,b-1)
