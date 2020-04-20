def check2():
    try:
        res = suma(3,4)
        print(res)
        if res == 7:
            print("OK")
        else: 
            print("Error con la suma")
    except:
        print("funcion no implementada")
