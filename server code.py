# Python code for the server
import socket
import threading


# Функція для обробки з'єднання з клієнтом
def socket_executor(client_socket):
    try:
        while True:
            # Отримуємо дані від клієнта
            data_received = client_socket.recv(1024)
            if not data_received:
                break
            print(f"Отримано від клієнта: {data_received.decode('ascii')}")

            # Відправляємо дані назад клієнту
            response = "Hello, Client!"
            client_socket.send(response.encode('ascii'))
    except Exception as e:
        print(f"Помилка: {e}")
    finally:
        # Закриваємо з'єднання з клієнтом
        print("Закриваємо з'єднання з клієнтом")
        client_socket.shutdown(socket.SHUT_RDWR)
        client_socket.close()


# Основна функція для запуску сервера
def main():
    # Створюємо сокет для сервера
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Задаємо адресу та порт для прослуховування
    ip_address = "127.0.0.1"
    port = 6116
    server_socket.bind((ip_address, port))

    # Починаємо прослуховування з'єднань
    server_socket.listen(10)
    print("Сервер готовий до прийому клієнтів...")

    iterator = 0

    while True:
        # Очікуємо на підключення клієнта
        client_socket, client_address = server_socket.accept()
        iterator += 1
        print(f"З'єднано з клієнтом {client_address[0]}:{client_address[1]} iterator {iterator}")

        # Створюємо новий потік для обробки клієнта
        thread = threading.Thread(target=socket_executor, args=(client_socket,))
        thread.start()


if __name__ == "__main__":
    main()
