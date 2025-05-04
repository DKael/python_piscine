from time import sleep
from Loading import ft_tqdm
from tqdm import tqdm

for elem in ft_tqdm(range(200)):
	sleep(0.1)
print()

for elem in tqdm(range(200)):
	sleep(0.1)
print()