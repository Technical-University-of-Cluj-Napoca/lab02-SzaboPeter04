def multiply_all(*args:int)->int:
    product=1
    for n in args:
        product*=n
    return product

if __name__=="__main__":
    print(multiply_all(1,2,3,4,5))
    print(multiply_all())
    print(multiply_all(5))