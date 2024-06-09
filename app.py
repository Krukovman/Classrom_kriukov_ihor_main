import logging
import os
from faker import Faker
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s')
def main():
    logging.info('начинается выполнения ПО')
    fake = Faker()
    name = fake.name
    address = fake.address()
    text = fake.text()

    logging.info(f"сгенерированное имя:{name}")
    logging.info(f"сгенерированное Адрес:{address}")
    logging.info(f"сгенерированное Текст:{text}")

    print(name)
    print(address)
    print(text)

    # получение переменного окружения
    api_key= os.getenv("API_KEY","Ключ отсутствует")
    message =os.getenv("MESSAGE","нет сообщений")

    print(f"API key:{api_key}")
    print(f"message:{message}")

    logging.info(f"API key:{api_key}")
    logging.info(f"message:{message}")

    logging.info("Завершение работы ПО")

if __name__ == '__main__':
    main()