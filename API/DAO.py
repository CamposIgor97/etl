from clickhouse_driver import Client
class SqlConnector():
    def __init__(self):
        self.__hostname = 'clickhouse-server'
        self.__client = None
    
    def connect(self):
        if self.__client: return
        self.__client = Client(host=self.__hostname)

    def __enter__(self):
        self.connect()
        return self.__client
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__client.disconnect()
        self.__client = None
