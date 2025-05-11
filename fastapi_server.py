from fastapi import FastAPI

# Инициализация объекта приложения
app = FastAPI()

# Используем декоратор, который указывает, что GET-запросы будут обрабатываться
# указанной функцией по дефолтному url
@app.get('/')
def handle_root():
    return {
        'app': 'v3'
    }
