import psutil

fragment = r"Docker"

for proc in psutil.process_iter(['pid', 'name']):
    try:
        process_info = proc.info
        process_name = process_info['name']
        
        if fragment in process_name:
            proc.kill()
            print(f"Killed process: PID={process_info['pid']}, Name={process_name}")
    
    except psutil.NoSuchProcess:
        pass
