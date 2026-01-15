import json
import sys
import os
from kafka import KafkaProducer
from kafka.errors import KafkaError

def kafka_connect(servers):
    try:
        producer = KafkaProducer(
            bootstrap_servers=servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            retries=5
        )
        return producer
    except KafkaError as e:
        print(f"Ошибка при подключении к Kafka: {e}")
        sys.exit(1)


def get_manual_input():
    print("\n--- Режим ручного ввода ---")
    table_name = input("Введите название таблицы: ").strip()

    fields = []
    print("Введите поля (имя и тип через пробел, например 'id SERIAL PRIMARY KEY'). Пустая строка - закончить:")
    while True:
        field_input = input("> ").strip()
        if not field_input:
            break
        parts = field_input.split(maxsplit=1)
        if len(parts) == 2:
            fields.append({"name": parts[0], "type": parts[1]})

    values = []
    print(
        "Введите данные (в формате JSON-объекта, например: {'username': 'admin', 'password': '123'}). Пустая строка - закончить:")
    while True:
        val_input = input("> ").strip()
        if not val_input:
            break
        try:
            val_json = json.loads(val_input.replace("'", "\""))
            values.append(val_json)
        except json.JSONDecodeError:
            print("Ошибка: Неверный формат JSON. Попробуйте еще раз.")

    return {
        "table_name": table_name,
        "fields": fields,
        "values": values
    }


def read_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл {file_path} не найден.")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError as e:
        print(f"Ошибка при чтении JSON из файла: {e}")
        return None


def send_message(producer, topic, data):
    try:
        future = producer.send(topic, data)
        record_metadata = future.get(timeout=10)
        print(
            f"Успешно отправлено в топик {record_metadata.topic} (partition: {record_metadata.partition}, offset: {record_metadata.offset})")
    except KafkaError as e:
        print(f"Ошибка при отправке сообщения: {e}")


if __name__ == '__main__':
    KAFKA_TOPIC = 'user-data'
    KAFKA_SERVERS = ['195.209.210.116:9092']

    producer = kafka_connect(KAFKA_SERVERS)

    try:
        while True:
            print("\nВыберите действие:")
            print("1. Ввести данные вручную")
            print("2. Загрузить из JSON-файла")
            print("3. Выход")

            choice = input("Ваш выбор: ").strip()

            payload = None

            if choice == '1':
                payload = get_manual_input()
            elif choice == '2':
                path = input("Введите путь к JSON-файлу: ").strip()
                payload = read_from_file(path)
            elif choice == '3':
                break
            else:
                print("Неверный ввод.")
                continue

            if payload and payload.get("table_name") and payload.get("values"):
                send_message(producer, KAFKA_TOPIC, payload)
            else:
                print("Ошибка: Данные неполные (отсутствует название таблицы или значения).")

    except KeyboardInterrupt:
        print("\nЗавершение работы продюсера...")
    finally:
        producer.close()