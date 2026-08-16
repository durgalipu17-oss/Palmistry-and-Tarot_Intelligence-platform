import os
import time
import psutil

process = psutil.Process(os.getpid())

def ram_mb():
    return process.memory_info().rss / (1024 * 1024)

print(f"RAM before TensorFlow: {ram_mb():.2f} MB")

import tensorflow as tf

print(f"RAM after TensorFlow import: {ram_mb():.2f} MB")

from ai.predict import model

print(f"RAM after model loading: {ram_mb():.2f} MB")

# Keep process alive for a few seconds
time.sleep(5)

print(f"RAM final: {ram_mb():.2f} MB")