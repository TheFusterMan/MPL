from concurrent.futures import ProcessPoolExecutor as Pool
import pandas as pd
import random as rd

def generate_csv(filename: str) -> None:
    data = {
        'cathegory': [],
        'value': []
    }

    for _ in range(20):
        cathegory = chr(rd.randint(ord('A'), ord('D')))
        value = rd.random()

        data['cathegory'].append(cathegory)
        data['value'].append(value)

    df = pd.DataFrame(data)

    try:
        df.to_csv(filename, index=False)
    except Exception as e:
        print(f"an error occurred: {e}")


def process_csv(filename: str):
    df = pd.read_csv(f"{filename}.csv")
    result_df = df.groupby('cathegory')['value'].agg(['median', 'std']).reset_index()
    result_df = result_df.rename(columns={'std': 'dispersion'})
    result_df = result_df.fillna(0)

    return result_df.to_dict(orient='records')

def merge_processed_files(filenames: list[str]):
    merged_data = {
        'cathegory': [],
        'value': []
    }

    for filename in filenames:
        data_to_merge = pd.read_csv(f"{filename}.csv").to_dict(orient='records')
        for row in data_to_merge:
            merged_data['cathegory'].append(row['cathegory'])
            merged_data['value'].append(row['median'])

    df = pd.DataFrame(merged_data)

    try:
        df.to_csv("data_processed_merged.csv", index=False)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    #1. генерация
    filenames_to_process = []

    for i in range(5):
        generate_csv(f"data_{i+1}.csv")
        filenames_to_process.append(f"data_{i+1}")

    #2. параллельная обработка
    with Pool(max_workers=5) as executor:
        results = list(executor.map(process_csv, filenames_to_process))

    for i in range(5):
        df = pd.DataFrame(results[i])
        filenames_to_process[i] = f"{filenames_to_process[i]}_processed"

        #2.1 промежуточный результат
        try:
            df.to_csv(f"{filenames_to_process[i]}.csv", index=False)
        except Exception as e:
            print(f"Ошибка: {e}")

    #3. финальная обработка
    merge_processed_files(filenames_to_process)
    result = process_csv("data_processed_merged")
    df = pd.DataFrame(result)

    try:
        df.to_csv("result.csv", index=False)
    except Exception as e:
        print(f"Ошибка: {e}")

    print("Готово! Результат в result.csv. Чтобы увидеть все стадии процесса обработки, проверьте другие файлы")