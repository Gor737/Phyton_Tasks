import random
import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'The function executed in {end_time - start_time} seconds')
        return result
    return wrapper

def filterFunc(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()

    processed_lines = map(lambda line: list(filter(lambda x: x > 40, map(int, line.split()))), lines)

    with open(fileName, 'a') as file:
        for line in processed_lines:
            file.write(' '.join(map(str, line)) + '\n')
          
def generatorOfRandomNubers(fileName, num_lines=100, num_per_line=20):
    with open(fileName, 'w') as file:
        for _ in range(num_lines):
            numbers = [random.randint(-100, 100) for _ in range(num_per_line)]
            line = ' '.join(map(str, numbers))
            file.write(line + '\n')


def read_file_generator(fileName):
    with open(fileName, 'r') as file:
        for line in file:
            yield list(map(int, line.split()))


fileName = 'acc_randomNumbers.txt'
generatorOfRandomNubers(fileName)
filterFunc(fileName)
gen = read_file_generator(fileName)

for line in gen:
    print(line)
