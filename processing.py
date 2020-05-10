from multiprocessing import cpu_count, Pool 
from tweet import main 

PROCESSES = cpu_count() - 1

def run_processes(users):

    pool = Pool(PROCESSES)
    pool.map_async(main, users)
    pool.close()
    pool.join()

    return 0
