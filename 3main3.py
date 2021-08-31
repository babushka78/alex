# Импорт библиотек
from binance.client import Client
import configparser

# Загрузка ключей из файла config
config = configparser.ConfigParser()
config.read_file(open('secret.cfg'))
test_api_key = config.get('BINANCE', 'TEST_API_KEY')
test_secret_key = config.get('BINANCE', 'TEST_SECRET_KEY')



client = Client(test_api_key, test_secret_key, testnet=True)

client.API_URL = 'https://testnet.binance.vision/api'  # Это нужно, чтобы изменить URL-адрес конечной точки тестового аккаунта

info = client.get_account()  # Получение информации об аккаунте

print(info)
