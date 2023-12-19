import sys
import time


def get_data(path_seeds: str) -> list[str]:
    """
    Obtiene las condiciones de conversión de semillas a tierra
    """
    with open(path_seeds, 'r') as f:
        data = f.readlines()
        data = [s.strip() for s in data]
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
    """
    Convierte una lista de semillas en una lista de tierra.
    Las que estén en el rango de 98 a 98 + 2 se convierten en 50 a 50 + 2
    Las que estén en el rango de 50 a 50 + 48 se convierten en 52 a 52 + 48
    """
    # Create a dictionary with the keys as the seeds and the values as the soil
    min_actual = sys.maxsize
    for i in range(len(semillas)):
        if i % 2 == 0:
            start = int(semillas[i])
            for i in range(int(semillas[i + 1])):
                min_local = trans(start + i, conditions)
                min_actual = min(min_actual, min_local)
    return min_actual


def trans(semilla, conditions):
    for condition in conditions:
        # Primera condición
        if condition[1] <= semilla <= condition[1] + condition[2]:
            return condition[0] + semilla - condition[1]



if __name__ == "__main__":
    a = time.time()
    data = get_data(path_seeds='semillas.txt')
    semillas = get_seeds(data[0])
    print(semillas)
    condiciones = get_conditions(data[1:])
    condiciones = [condition for sublist in condiciones for condition in sublist]
    semillas = transform_map(semillas, condiciones)
    print(semillas)
    print("Time taken: ", time.time() - a)
