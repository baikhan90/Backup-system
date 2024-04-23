import argparse
import logging
from encryptor import Encryptor
from file_monitor import FileMonitor
from data_storage import LocalDataStorage

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    parser = argparse.ArgumentParser(description='CLI tool to monitor file changes and create encrypted backups.')
    parser.add_argument('--directory', '-d', type=str, help='Directory to monitor')
    parser.add_argument('--interval', '-i', type=str, help='Time interval (e.g., 10m for 10 minutes, 2h for 2 hours, 1d for 1 day)')
    args = parser.parse_args()

    interval = int(args.interval[:-1])
    interval_type = args.interval[-1].lower()

    encryptor = Encryptor()
    backup = LocalDataStorage('./backup') # or RemoteDataStorage(host, port, username, password)
    file_monitor = FileMonitor(args.directory, interval, interval_type, encryptor, backup)
    file_monitor.start()

if __name__ == "__main__":
    main()
