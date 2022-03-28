import time
import gc

#no1
def p1_uruu_hantei(year: int) ->bool:
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False

#no3
def p2_uruu_hantei(year: int) ->bool:
    if year%400==0 or (year%100==0 and year%4==0):
        return True
    else:
        return False

#no2
def p3_uruu_hantei(year: int) ->bool:
    if (year%100!=0 and year%4==0) or year%400==0:
        return True
    else:
        return False

def hikaku():
    gc.disable()
    years = range(1000000)

    gc.collect()
    t = time.time()
    for y in years:
        p1_uruu_hantei(y)
    print('p1:',time.time()-t)

    gc.collect()
    t = time.time()
    for y in years:
        p2_uruu_hantei(y)
    print('p2:',time.time()-t)

    gc.collect()
    t = time.time()
    for y in years:
        p3_uruu_hantei(y)
    print('p3:',time.time()-t)

def test():
    years = (1000,1992,2000,2001)
    for y in years:
        if p2_uruu_hantei(y):
            print(f"{y} is a leap year")
        else:
            print(f"{y} is not a leap year")

def main():
    hikaku()

if __name__=='__main__':
    main()