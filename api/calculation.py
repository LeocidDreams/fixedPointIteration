import numpy as np
import json
from mathparse import mathparse
# solving current expression
def dumpFile(dir_:dict):
      with open("iteration.json",mode='w',encoding='UTF-16') as file:
                file.write(
                    json.dump(dir_)
                )
def g(p):
    return mathparse.parse(p)

def iteration(p0=0.5,TOL=1e-6,N0=10000):
    i=1
    while i<=N0:
        p=g(p0)
        if np.abs(p0-p)<TOL:
            break
        # print(i,". iterasyon:/t","",p)
        # print("Bagil Hata:",np.abs(p0-p))
        dir_={
                "step":N0,
                "relativeError":np.abs(p0-p),
                "success":False
            }
        dumpFile(dir_)     
        i+=1
        p0=p

    if i==N0+1:
        print("{}. iterasyonda durdu(Hatali)".format(N0))
        dumpFile(dir_={
                    "step":N0+1,
                    "relativeError":'Failed',
                    "success":False
                })
    else:
        print("Basarili")

        dumpFile(dir_={
             "step":i,
             "relativeError":np.abs(p0-p),
             "success":True

        })