import time
import psutil
import datetime


def get_network_throughput():
    old_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    time.sleep(1)
    new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    return ((new_value - old_value) / 1_000_000) * 8  # Convert bytes to MB and then MB to Mbps (multiply by 8)


def log_throughput():
    with open("network_throughput.log", "a") as f:
        while True:
            throughput = get_network_throughput()
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{current_time} - Throughput: {throughput:.5f} Mbps\n"

            # Write to file
            f.write(log_entry)
            f.flush()  # Ensure data is written immediately

            # Print to console
            print(log_entry.strip())

            time.sleep(4)  # We already waited 1 second in the get_network_throughput function


if __name__ == "__main__":
    log_throughput()
