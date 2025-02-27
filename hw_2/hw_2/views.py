from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <html>
        <head>
            <title>API Endpoints</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding: 30px; }
                h1 { color: #333; }
                ul { list-style: none; padding: 0; }
                li { margin: 10px 0; }
                a { text-decoration: none; color: #007bff; font-size: 18px; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <h1>Добро пожаловать в API!</h1>
            <p>Доступные эндпоинты:</p>
            <ul>
                <li><a href="/movies/">📽 /movies/ - Список фильмов</a></li>
                <li><a href="/movies/1/">🎬 /movies/1/ - Фильм с ID=1</a></li>
                <li><a href="/articles/">📝 /articles/ - Список статей</a></li>
                <li><a href="/articles/1/">📜 /articles/1/ - Статья с ID=1</a></li>
            </ul>
        </body>
        </html>
    """)
