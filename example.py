import easyocr

# Инициализация OCR с поддержкой русского языка
reader = easyocr.Reader(['ru'], gpu=False)

# Путь к изображению с российским автономером
image_path = 'C:/Users/ADMIN/PycharmProjects/ANPR with Python, Yolov8 and EasyOCR(3)/foto/foto5.jpg'

# Чтение номерного знака с изображения
results = reader.readtext(image_path)

# Вывод результатов
for detection in results:
    print(detection[1])  # Текст номерного знака
    print(detection[2])  # Уверенность в распознавании