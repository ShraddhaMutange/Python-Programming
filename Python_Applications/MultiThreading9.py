import time
import threading

def SumEven(No):
    print("TID of SumEven thread is :", threading.get_ident())

def SumOdd(No):
    print("TID of SumOdd thread is :", threading.get_ident())
    
def main():
    print("TID of main thread is :", threading.get_ident())

    start_time = time.perf_counter()

    T1 = threading.Thread(target=SumEven, args=(100000000,))
    T2 = threading.Thread(target=SumOdd, args=(100000000,))

    T1.start()
    T2.start()   

    T1.join()
    T2.join() 

    end_time = time.perf_counter()

    print(f"Required time is : {end_time - start_time:.4f}")

if (__name__ == "__main__"):
    main()
    