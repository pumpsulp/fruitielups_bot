from roboflow.models.object_detection import ObjectDetectionModel
from config import classes_translation


class Model(ObjectDetectionModel):
    def __init__(self, api_key, id_, version):
        ObjectDetectionModel.__init__(self, api_key=api_key, id=id_, version=version)

    def get_predict(self, img_path, confidence=1, overlap=1, hosted=False, mode='list'):
        # Список
        if mode == 'list':
            prediction = self.predict(image_path=img_path, confidence=confidence, overlap=overlap, hosted=hosted,
                                      format='json').json()
            classes = []
            classes_translated = []

            for result in prediction['predictions']:
                if not result['class'] in classes:
                    classes.append(result['class'])
                    classes_translated.append(classes_translation[result['class']])

            return classes_translated
        # Изображение
        elif mode == 'image':
            prediction = self.predict(image_path=img_path, confidence=confidence, overlap=overlap, hosted=hosted,
                                      labels=True, format='image')
            return prediction
        # Неправильное наименование mode
        else:
            return None
