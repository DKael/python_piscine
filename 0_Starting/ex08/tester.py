from time import sleep
from Loading import ft_tqdm
from tqdm import tqdm

for elem in ft_tqdm(range(200000)):
	sleep(0.05)
print()

for elem in tqdm(range(2000)):
	sleep(0.05)
print()