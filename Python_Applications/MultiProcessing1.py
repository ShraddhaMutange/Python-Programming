import time
import multiprocessing

def SumEven(No):

    sum = 0

    for i in range(2, No, 2):
        sum = sum + i

    print("Summation of even :", sum)

def SumOdd(No):
    sum = 0

    for i in range(1, No, 2):
        sum = sum + i

    print("Summation of odd :", sum)
    
def main():
    start_time = time.perf_counter()

    T1 = multiprocessing.Process(target=SumEven, args=(100000000,))
    T2 = multiprocessing.Process(target=SumOdd, args=(100000000,))

    T1.start()
    T2.start()   

    T1.join()
    T2.join() 

    end_time = time.perf_counter()

    print(f"Required time is : {end_time - start_time:.4f}")

if (__name__ == "__main__"):
    main()
    