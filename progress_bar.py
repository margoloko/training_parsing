from time import sleep
from tqdm import tqdm

if __name__ == '__main__':
    # Передача в функцию tqdm() итерируемого объекта
    for i in tqdm(range(200), desc='my first progress-bar'):
        sleep(0.003)
    for i in tqdm(range(300), desc = 'and second'):
        sleep(0.001)
    