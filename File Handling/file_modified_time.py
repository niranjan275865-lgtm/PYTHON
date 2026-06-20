import os
import time

modified_time = os.path.getmtime("sample.txt")

print("Last Modified Time:")
print(time.ctime(modified_time))