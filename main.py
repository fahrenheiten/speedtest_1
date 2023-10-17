import speedtest
import time

def get_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # converting from bits to Megabits per second
    upload_speed = st.upload() / 10**6      # converting from bits to Megabits per second
    return download_speed, upload_speed

def write_to_file_and_console(message):
    with open("internet_speed_results.txt", "a") as f:
        f.write(message + "\n")
    print(message)

if __name__ == "__main__":
    while True:
        try:
            download, upload = get_speed()
            result_message = f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}, Download: {download:.2f} Mbps, Upload: {upload:.2f} Mbps"
            write_to_file_and_console(result_message)
        except Exception as e:
            error_message = f"Error occurred at {time.strftime('%Y-%m-%d %H:%M:%S')}: {e}"
            write_to_file_and_console(error_message)
        time.sleep(5)  # wait for 5 seconds

