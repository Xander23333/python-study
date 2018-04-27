from time import sleep
from tqdm import *
from multiprocessing import Pool, freeze_support, RLock

str = '123124555'
for i in tqdm(str):
  sleep(0.1)