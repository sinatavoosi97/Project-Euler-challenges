   
def Smallest_multiple():

    for j in range(1,10000000000000):
            if j%1==0 and j%2==0 and j%3==0 and j%4==0 and j%5==0:
              if j%6==0  and j%7==0 and j%8==0 and j%9==0 and j%10==0:
                if j%11==0 and j%12==0 and j%13==0 and j%14==0 and j%15==0:
                  if j%16==0  and j%17==0 and j%18==0 and j%19==0 and j%20==0:
                                                            return j
print(Smallest_multiple())
