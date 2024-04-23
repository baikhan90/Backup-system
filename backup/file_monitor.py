import os
import logging
import hashlib
import schedule
import time

class FileMonitor:
    def __init__(self, directory, interval, interval_type, encryption, data_storage):
        self.directory = directory
        self.interval = interval
        self.interval_type = interval_type
        self.encryption = encryption
        self.backup = data_storage
        self.checksums = {}

    def calculate_checksum(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
            return hashlib.md5(data).hexdigest()

    def check_files(self, directory):
        files = os.listdir(directory)
        for filename in files:
            logging.info('Checking file {}'.format(filename))
            file_path = os.path.join(directory, filename)

            # If file is a directory, recursively check files in the directory
            if os.path.isdir(file_path):
                self.check_files(file_path)
                return

            if os.path.isfile(file_path):
                checksum = self.calculate_checksum(file_path)
                if filename in self.checksums:
                    logging.info('File {} already exists'.format(filename))
                    if self.checksums[filename] == checksum:
                        logging.info('File {} has not changed'.format(filename))
                        continue
                    logging.info('File {} has changed'.format(filename))
                    with open(file_path, 'rb') as file:
                        logging.info('Reading & encrypting file {}...'.format(filename))
                        data = file.read()
                        encrypted_data = self.encryption.encrypt(data)

                        logging.info('Saving encrypted file {}...'.format(filename))
                        self.backup.save(encrypted_data, filename)
                        logging.info('File {} has been backed up'.format(filename))
                else:
                    logging.info('File {} is new'.format(filename))
                    with open(file_path, 'rb') as file:
                        logging.info('Encrypting file {}...'.format(filename))
                        data = file.read()
                        encrypted_data = self.encryption.encrypt(data)
                        logging.info('Saving encrypted file {}...'.format(filename))
                        self.backup.save(encrypted_data, filename)
                        logging.info('File {} has been backed up'.format(filename))
                self.checksums[filename] = checksum
            print("\n")

    def start(self):
        logging.info('Starting...')
        self.check_files(self.directory)

        if self.interval_type == 'm':
            schedule.every(self.interval).minutes.do(self.check_files, self.directory)
        elif self.interval_type == 'h':
            schedule.every(self.interval).hours.do(self.check_files, self.directory)
        elif self.interval_type == 'd':
            schedule.every(self.interval).days.do(self.check_files, self.directory)
        elif self.interval_type == 's':
            schedule.every(self.interval).seconds.do(self.check_files, self.directory)
        else:
            raise ValueError('Invalid interval type')

        while True:
            schedule.run_pending()
            time.sleep(1)
