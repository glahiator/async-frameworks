import aiohttp
from aiohttp import web

async def get_phrase():
    # Метод, который обращается к стороннему ресурсу и забирает данные
    async with aiohttp.ClientSession() as session:
        async with session.get('https://fish-text.ru/get', params={'type': 'title'}) as response:
            result = await response.json(content_type='text/html; charset=utf-8')
            return result.get('text')


async def index_handler(request):
    # Формируем ответ для клиента
    return web.Response(text=await get_phrase())


async def response_signal(request, response):
    # Увеличиваем все буквы в ответе
    response.text = response.text.upper()
    return response


async def make_app():
    # Объявляем приложение — ваш веб-сервер
    app = web.Application()

    # Добавим сигнал — метод, который нужно запустить при определённом событии
    # В этом случае он запустится после формирования ответа
    app.on_response_prepare.append(response_signal)

    # Добавим необходимый URL
    app.add_routes([web.get('/', index_handler)])
    return app


web.run_app(make_app())  # Запускаем приложение