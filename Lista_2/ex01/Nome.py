import threading


def imprimir_numeros(nome):
    for i in range(1, 6):
        print(f"Thread {nome}: {i}")


thread1 = threading.Thread(target=imprimir_numeros, args=("A",))
thread2 = threading.Thread(target=imprimir_numeros, args=("B",))


thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("Programa principal encerrado.")