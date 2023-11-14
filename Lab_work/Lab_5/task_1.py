# TODO решите задачу
import json


def task() -> float:
    with open('input.json') as file:
        data = json.load(file)
        composition_sum = sum([dict_data["score"] * dict_data["weight"] for dict_data in data])
    return round(composition_sum, 3)


if __name__ == "__main__":
    print(task())
