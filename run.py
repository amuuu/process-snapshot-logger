import psutil
import time 
from datetime import datetime

index = 0
iter = 0

while True:
    
    time.sleep(0.5)
        
    index += 1
    if index == 10:
        iter += 1
        index = 0

    file_name = str(index) + ".txt"

    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        processes.append(proc.info)

    with open(file_name, 'w') as file:
        file.write("TIME: " + str(datetime.now().strftime("%H:%M:%S")))
        file.write("\nITER: " + str(iter))
        file.write("\n________________________________________________\n\n")
        for process in processes:
            file.write(f"PID: {process['pid']}\n")
            file.write(f"Name: {process['name']}\n")
            file.write(f"Status: {process['status']}\n")
            file.write("-" * 30 + "\n")