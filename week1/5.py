def zarb(x,y):
    result = 0
    cunter = 1

    while cunter <= y:
        result = result + x
        cunter = cunter+1

    return f"The sum is {result}"

print(zarb(4,6))

