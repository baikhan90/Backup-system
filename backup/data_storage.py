import os

class DataStorageInterface:
    def __init__(self, destination_dir):
        self.destination_dir = destination_dir

    def save(self, data, filename):
        raise NotImplementedError

    def fetch(self, filename):
        raise NotImplementedError

    def delete(self, filename):
        raise NotImplementedError
    
    def get_destination_path(self, filename):
        return f'{self.destination_dir}/{filename}'


class LocalDataStorage(DataStorageInterface):
    def save(self, data, filename):
        with open(self.get_destination_path(filename), 'wb') as file:
            file.write(data)

    def fetch(self, filename):
        with open(self.get_destination_path(filename), 'rb') as file:
            return file.read()

    def delete(self, filename):
        os.remove(self.get_destination_path(filename))

# class RemoteDataStorage(DataStorageInterface):
    # def __init__(self, host, port, username, password):
        # self.host = host
        # self.port = port
        # self.username = username
        # self.password = password
 
    # def save(self, data, destination_path):
        # transport = paramiko.Transport((self.host, self.port))
        # transport.connect(username=self.username, password=self.password)
        # sftp = transport.open_sftp()
        # sftp.putfo(data, destination_path)
        # sftp.close()
        # transport.close()
# 
    # def fetch(self, source_path):
        # transport = paramiko.Transport((self.host, self.port))
        # transport.connect(username=self.username, password=self.password)
        # sftp = transport.open_sftp()
        # data = sftp.open(source_path, 'rb').read()
        # sftp.close()
        # transport.close()
        # return data
# 
    # def delete(self, path):
        # transport = paramiko.Transport((self.host, self.port))
        # transport.connect(username=self.username, password=self.password)
        # sftp = transport.open_sftp()
        # sftp.remove(path)
        # sftp.close()
        # transport.close()
