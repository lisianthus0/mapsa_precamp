#empty parallelogram
def empty_parallelogram(tol = int(input("tol ra vared kon: ")),arz = int(input("arz ra vared kon: "))):
    for i in range(tol):
        for j in range(tol-i-1):
            print(" ", end="")
        for k in range(arz):
            if k==0 or i==0 or k==(arz-1) or i==(tol-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
empty_parallelogram()



