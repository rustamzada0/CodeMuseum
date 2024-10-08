# import multiprocessing
# import time

# def cpu_bound_task(n):
#     while n > 0:
#         n -= 1

# # Multiprocessing ile süre ölçme
# def multiprocessing_example():
#     n = 10**8
#     start_time = time.time()

    # coxlu proses basladirig ve her bir proses ucun bir thread olacaq

#     process1 = multiprocessing.Process(target=cpu_bound_task, args=(n,))
#     process2 = multiprocessing.Process(target=cpu_bound_task, args=(n,))
    
#     process1.start()
#     process2.start()
    
#     process1.join()
#     process2.join()
    
#     end_time = time.time()
#     print(f"Multiprocessing süresi: {end_time - start_time} saniye")

# multiprocessing_example()


import threading
import time

def cpu_bound_task(n):
    while n > 0:
        n -= 1

# Threading ile süre ölçme
def threading_example():
    n = 10**8
    start_time = time.time()
    
    thread1 = threading.Thread(target=cpu_bound_task, args=(n,)) # bir proses texmini 5 saniyelik is gorur ve thread islederek "2" dene 5 saniyelik isi eyni anda gordursek de yene de 5 saniye etmeli idi ama GIL icaze vermir ve python kodu sira ile icra olunur (1 thread ile)
    thread2 = threading.Thread(target=cpu_bound_task, args=(n,)) # bir proses texmini 5 saniyelik is gorur ve thread islederek "2" dene 5 saniyelik isi eyni anda gordursek de yene de 5 saniye etmeli idi ama GIL icaze vermir ve python kodu sira ile icra olunur (1 thread ile)
    
    # coxlu thread baslatsaq da GIL pythonda ancag 1 thread icaze verir
    thread1.start()
    print("thread1 started")
    thread2.start()
    print("thread2 started")
    thread1.join()
    thread2.join()
    
    end_time = time.time()
    print(f"Threading süresi: {end_time - start_time} saniye")

threading_example()


# C++ , C, C# ve Java: Evet, aynı anda bir kodu (örneğin 5 thread ile) okuyup işleyebilirsiniz.
# Python: Hayır, GIL nedeniyle aynı anda birden fazla thread Python kodunu okuyup işleyemez.
# Evet, iki thread'in de çalıştığını görüyor olmanız normaldir, çünkü Python'da threading modülü ile thread'ler gerçekten çalışır. Ancak, GIL nedeniyle aynı anda yalnızca bir thread'in Python bytecode'u çalıştırmasına izin verilir. Bu nedenle, thread'ler arasında bağlam değişimi (context switching) yapılarak çalışırlar, fakat gerçek paralelizm sağlanmaz.

# import threading
# import time

# def cpu_bound_task():
#     x = 0
#     while x < 10**8:
#         x += 1

# def cpu_bound_task2():
#     x = 0
#     while x < 10**8:
#         x += 1

# time1 = time.time()
# thread1 = threading.Thread(target=cpu_bound_task) # bir proses texmini 5 saniyelik is gorur ve thread islederek "2" dene 5 saniyelik isi eyni anda gordursek de yene de 5 saniye etmeli idi ama GIL icaze vermir ve python kodu sira ile icra olunur (1 thread ile)
# thread2 = threading.Thread(target=cpu_bound_task2) # bir proses texmini 5 saniyelik is gorur ve thread islederek "2" dene 5 saniyelik isi eyni anda gordursek de yene de 5 saniye etmeli idi ama GIL icaze vermir ve python kodu sira ile icra olunur (1 thread ile)

# thread1.start()
# # thread2.start()

# thread1.join()
# # thread2.join()

# time2 = time.time()
# print(f"Threading CPU time: {time2 - time1} saniye")

# print("Both threads have finished execution.")


# ama multiprocessing ile çoklu thredlerle aynı anda Python kodu okuyup işleyebilirsiniz. 
# thread1 = multiprocessing.Process(target=cpu_bound_task)
# thread2 = multiprocessing.Process(target=cpu_bound_task2)