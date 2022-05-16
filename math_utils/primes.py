def isprime(num):
    if num == 2 or num == 3:
        return True
    if num ==1:
        return False
    for n in range(2,int(num**0.5)+1):
        if num%n == 0:
            return False
        return True
        