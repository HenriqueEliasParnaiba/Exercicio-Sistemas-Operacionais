import threading
import time

#Filosofos
N = 5
hashis = [threading.Semaphore(1) for _ in range(N)]

mutex = threading.Semaphore(N - 1);

def pensar(filosofo_id):
    print(f"Filósofo {filosofo_id} está pensando.");
    time.sleep(1)

def comer(filosofo_id):
    left = filosofo_id;
    right = (filosofo_id + 1) % N;
    
    # Filósofo tenta pegar o hashi à esquerda e à direita
    while True:
        with mutex:  
            with hashis[left]: 
                if hashis[right].acquire(blocking=False):  
                    print(f"Filósofo {filosofo_id} está comendo.");
                    time.sleep(1)
                    hashis[right].release();  
                    break
                else:
                    hashis[left].release();
                    pensar(filosofo_id)

def filosofo(filosofo_id):
    while True:
        pensar(filosofo_id)
        comer(filosofo_id)

if __name__ == "__main__":
    threads = []
    for i in range(N):
        t = threading.Thread(target=filosofo, args=(i,));
        threads.append(t);
        t.start();

    for t in threads:
        t.join();
