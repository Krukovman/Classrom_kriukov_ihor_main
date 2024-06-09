# применение версии пайтон
FROM python:3.12

# Установка раочей дерриктории
WORKDIR /app

# Копирования файлов зависимости
COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


# Определения команды запуска ПО
CMD ["python", "app.py"]
