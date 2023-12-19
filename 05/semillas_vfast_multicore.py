import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def get_data(path_seeds: str) -> list[str]:
    """
    Obtiene las condiciones de conversión de semillas a tierra
    """
    with open(path_seeds, 'r') as f:
        data = [s.strip() for s in f.readlines()]
        data = [s for s in data if s != '']
    return data


def get_seeds(data: str) -> list[int]:
    """
    Obtiene las semillas de la lista de condiciones
    """
    semillas = data.replace('seeds: ', '').split(' ')
    return [int(s) for s in semillas]


def get_conditions(data: list[str]):
    """
    Obtiene las condiciones de conversión de semillas a tierra
    :param data:
    :return:
    """
    conditions = []
    latest_index = ""
    counter = 0
    for line in data:
        if line[0] not in '0123456789':
            conditions.append([])
            latest_index = line[:-5]
        else:
            conditions[-1].append([int(s) for s in line.split(' ')])
            conditions[-1][-1][-1] -= 1

    return conditions


def transform_map(semillas: list[int], conditions: list[list[int]]) -> int:
    min_actual = sys.maxsize
    start = int(semillas[0])
    for i in range(int(semillas[1])):
        min_local = trans(start + i, conditions)
        min_actual = min(min_actual, min_local)
    return min_actual


def trans(semilla: int, conditions: list[list[list[int]]]) -> int:
    for main_step in conditions:
        for condition in main_step:
            # Primera condición
            if condition[1] <= semilla <= condition[1] + condition[2]:
                semilla = condition[0] + semilla - condition[1]
                break
    return semilla


if __name__ == "__main__":
    a = time.time()
    data = get_data(path_seeds='semillas.txt')
    semillas = get_seeds(data[0])
    print(semillas)
    condiciones = get_conditions(data[1:])
    # Divide the list of seeds into lists of two elements
    semillas = [semillas[i:i + 2] for i in range(0, len(semillas), 2)]

    # Call the function in parallel and get the results, ten do the min
    min_total = sys.maxsize
    with ProcessPoolExecutor(max_workers=16) as executor:
        futures = [executor.submit(transform_map, semilla, condiciones) for semilla in semillas]
        for future in as_completed(futures):
            result = future.result()
            print(result)
            min_total = min(min_total, result)

    # semillas = transform_map(semillas, condiciones)
    print("Mínimo resultante: ", min_total)
    print("Time taken: ", time.time() - a)
