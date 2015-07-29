import psutil, os 
 
s = set(range(1000000))
    
process = psutil.Process(os.getpid()) 
mem = process.get_memory_info().rss / 1000 
print("Used this much memory: " + str(mem) + ' kb')