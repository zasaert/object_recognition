from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Загружаем модель, обученную распознаванию объектов
model = tf.keras.models.load_model('object_detection_model.h5')

class_names = []

@app.route('/api/object_detection', methods=['POST'])
def object_detection():
    if request.method == 'POST':
        file = request.files['image']
        image = Image.open(file.stream)

        # Преобразование изображения для входа в модель
        image = image.resize((224, 224))
        image = np.array(image)
        image = image / 255.0
        image = np.expand_dims(image, axis=0)

        # Предсказание класса объекта на изображении
        predictions = model.predict(image)
        predicted_class = class_names[np.argmax(predictions)]

        return jsonify({'object': predicted_class})

if __name__ == '__main__':
    app.run(debug=True)