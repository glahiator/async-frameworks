from twisted.internet import defer

def toInt(data):  # Первый обработчик превращает данные в int
    return int(data)

def increment_number(data):  # Второй обработчик увеличивает значение на единицу
    return data + 1

def print_result(data):  # Третий обработчик выводит данные в консоль
    print(data)

def handleFailure(f):  # Обработчик ошибок
    print("OOPS!")

def get_deferred():
    # Объявляем Deferred-объект
    d = defer.Deferred()

    # Добавляем обработчики в нужном порядке
    return d.addCallbacks(toInt, handleFailure).addCallbacks(increment_number, handleFailure).addCallback(print_result)


d = get_deferred()
# Передаём данные в цепочку функций, чтобы запустить расчёты
d.callback(12.123)