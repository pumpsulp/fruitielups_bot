ROBOFLOW_ID = 'mortuus-stellaris-raxs6/-object-detection-pukbl/3'
ROBOFLOW_VERSION = 3

command_start_message = 'Привет! Я Бот, распознающий овощи, фрукты и другие продукты 👋\nПросто отправьте мне изображение‍ 🌾\n_Подробнее в /help_'
command_help_message = 'Выберите интересующий вопрос'

class_list = ['apple', 'lemon', 'orange', 'mandarin', 'banana', 'grape', 'pear',
              'peach', 'cherry', 'strawberry', 'tomato', 'potato', 'carrot',
              'bell pepper', 'chilli pepper', 'cabbage', 'mushrooms', 'zucchini',
              'eggplant', 'bulb onion', 'green onion', 'cucumber', 'garlic',
              'egg', 'milk', 'chicken meat', 'beef', 'pork']

classes_translation = {'apple': 'Яблоко 🍎', 'lemon': 'Лимон 🍋', 'orange': 'Апельсин 🍊', 'mandarin': 'Мандарин 🍊',
                       'banana': 'Банан 🍌', 'grape': 'Виноград 🍇', 'pear': 'Груша 🍐', 'peach': 'Персик 🍑',
                       'cherry': 'Вишня 🍒', 'strawberry': 'Клубника 🍓', 'tomato': 'Помидор 🍅', 'potato': 'Картошка 🥔',
                       'carrot': 'Морковка 🥕', 'bell pepper': 'Болгарский перец 🫑', 'chilli pepper': 'Перец чили 🌶',
                       'cabbage': 'Капуста', 'mushrooms': 'Грибы 🍄', 'zucchini': 'Кабачок 🐗', 'eggplant': 'Баклажан 🍆',
                       'bulb onion': 'Репчатый лук 🧅', 'green onion': 'Зелёный лук 🥬', 'cucumber': 'Огурец 🥒',
                       'garlic': 'Чеснок 🧄', 'egg': 'Куриное яйцо 🥚', 'milk': 'Молоко 🥛',
                       'chicken meat': 'Куриное мясо 🐓', 'beef': 'Говядина 🐄', 'pork': 'Свинина 🥩'}

class_labels = ['Яблоко', 'Банан', 'Свекла', 'Болгарский перец', 'Капуста', 'Стручковый перец', 'Морковь',
                'Цветная капуста',
                'Перец чили', 'Кукуруза', 'Огурец', 'Баклажан', 'Чеснок', 'Имбирь', 'Виноград', 'Халапеньо', 'Киви',
                'Лимон', 'Латук', 'Манго', 'Лук', 'Апельсин', 'Паприка', 'Груша', 'Горох', 'Ананас', 'Гранат',
                'Картофель', 'Редька', 'Соевые бобы', 'Шпинат', 'Сладкая кукуруза', 'Батат', 'Помидор', 'Репа', 'Арбуз']

text_phrases = ['Я пока не научился разговаривать 😭',
                'Простите, я пока только фрукты да овощи на фотографиях различаю 👉👈',
                'Я не умею разговаривать, лучше отправь мне фото с овощем или фруктом, а я попробую угадать его! 👀',
                'Эээ... Мм... Что же ответить на это, я не умею разговаривать 🤕',
                'Я робот *бип-буп* *би-би, буп-буп* ни-че-го не-по-ни-маю ошибка ошибка (лучше отправь мне фото с фруктом или овощем)🤖',
                '😵']

author_info = 'Создатель: @mrtsstlrs\nДанный бот - демонстрация работы нейронной сети в рамках проекта Chef AI.'
model_info = 'Модель нейронной сети: YOLOv8\nPowered by Ultralytics.'
