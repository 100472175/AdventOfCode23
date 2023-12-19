import pprint


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


def transform_map(semillas: list[int], conditions: list[list[int]]) -> list[int]:
    """
    Convierte una lista de semillas en una lista de tierra.
    Las que estén en el rango de 98 a 98 + 2 se convierten en 50 a 50 + 2
    Las que estén en el rango de 50 a 50 + 48 se convierten en 52 a 52 + 48
    """
    # Create a dictionary with the keys as the seeds and the values as the soil
    semillas_procesadas = {seed: 0 for seed in semillas}
    for s in semillas:
        for condition in conditions:
            if semillas_procesadas[s] != 0:
                break
            # Primera condición
            if condition[1] <= s <= condition[1] + condition[2]:
                semillas_procesadas[s] = condition[0] + s - condition[1]
        if semillas_procesadas[s] == 0:
            semillas_procesadas[s] = s

    # Si no cumple ninguna condición, se queda igual

    return list(semillas_procesadas.values())


if __name__ == "__main__":
    import time

    a = time.time()
    data = get_data(path_seeds='semillas.txt')
    semillas = get_seeds(data[0])
    print(semillas)
    condiciones = get_conditions(data[1:])
    for condition in condiciones:
        semillas = transform_map(semillas, condition)
    print(min(semillas))
    print("Time taken: ", time.time() - a)
