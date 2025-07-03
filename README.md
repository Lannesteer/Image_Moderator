# Image_Moderator

1. Клонируйте репозиторий и перейдите в папку проекта:
   ```bash
   git clone https://github.com/Lannesteer/Image_Moderator.git
   cd Image_Moderator

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
4. Добавьте файл .env в корень проекта

5. Запустите сервер:
   ```bash
   #Через скрипт app.py
    python app.py
   #Или через uvicorn
    uvicorn app:app --reload

6. Пример запроса:
   ```bash
   curl -X POST http://127.0.0.1:8000/moderate -F "image=@photo_2025-06-03_20-32-15.jpg"