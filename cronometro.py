import time

print("Presiona CTRL+C para detener el cronómetro")
start_time = time.time()
try:
    while True:
        elapsed = time.time() - start_time
        mins, secs = divmod(int(elapsed), 60)
        hours, mins = divmod(mins, 60)
        print(f"\rTiempo transcurrido: {hours:02d}:{mins:02d}:{secs:02d}", end="")
        time.sleep(1)
except KeyboardInterrupt:
    elapsed = time.time() - start_time
    mins, secs = divmod(int(elapsed), 60)
    hours, mins = divmod(mins, 60)
    print(f"\nCronómetro detenido en: {hours:02d}:{mins:02d}:{secs:02d}")

