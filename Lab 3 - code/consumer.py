import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError, Error
import json
import jsonschema
from jsonschema import validate
from kafka import KafkaConsumer
from datetime import datetime
import sys

def db_connect(dsn):
    try:
        conn = psycopg2.connect(dsn)
        return conn
    except psycopg2.OperationalError as e:
        print(f"Ошибка при подключении к БД: {e}")
        sys.exit(1)

def db_create_table(conn, table_name, fields):
    cols = sql.SQL(', ').join(
        sql.SQL("{} {}").format(sql.Identifier(field['name']), sql.SQL(field['type']))
        for field in fields
    )
    query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
        sql.Identifier(table_name),
        cols
    )

    try:
        with conn.cursor() as cur:
            cur.execute(query)
    except psycopg2.Error as e:
        print(f"Ошибка при создании таблицы \"{table_name}\": {e}")
        conn.rollback()

def db_insert(conn, table_name, values):
    cols = values[0].keys()
    query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
        sql.Identifier(table_name),
        sql.SQL(', ').join(map(sql.Identifier, cols)),
        sql.SQL(', ').join(sql.Placeholder() * len(cols))
    )

    try:
        with conn.cursor() as cur:
            for record in values:
                data = [record.get(col) for col in cols]
                cur.execute(query, data)
            
            conn.commit()
    except psycopg2.OperationalError as e:
        print(f"Произошла ошибка при вставке в таблицу БД: {e}")
        conn.rollback()

def json_validate(data):
    try:
        return json.loads(data.value)
    except json.JSONDecodeError as e:
        print(f"Строка \"{data.value}\" не соответствует формату JSON: {e}")
        return None

def json_schema_validate(data):
    schema = {
        "type": "object",
        "properties": {
            "table_name": {"type": "string"},
            "fields": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string"}
                    },
                    "required": ["name", "type"]
                }
            },
            "values": {
                "type": "array",
                "items": {"type": "object"}
            }
        },
        "required": ["table_name", "values"] # планируется, что fields необязателен, если такая таблица уже создана
    }

    try:
        validate(instance=data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Ошибка валидации JSON Schema: {e.message}")
        return False

if __name__ == '__main__':
    try:
        conn = db_connect("postgresql://admin:12345@127.0.0.1:5432/db")
        consumer = KafkaConsumer(
            'user-data',
            bootstrap_servers='127.0.0.1:9092',
            value_deserializer=lambda m: m.decode('utf-8')
        )

        for msg in consumer:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{now} сообщение: {msg.value}")

            valid_msg = json_validate(msg)

            if (valid_msg is None) or (not json_schema_validate(valid_msg)):
                continue

            table_name = valid_msg.get("table_name")
            fields = valid_msg.get("fields")
            values = valid_msg.get("values")

            if fields:
                db_create_table(conn, table_name, fields)

            db_insert(conn, table_name, values)
    except KeyboardInterrupt:
        print("Завершение работы...")
    finally:
        if conn:
            conn.close()