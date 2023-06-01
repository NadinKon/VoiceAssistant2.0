# VoiceAssistant (голосовой помошник)

Распознает команды, оценивает их с помощью логистической регрессии и выполняет соответствующие функции на основе обученной модели.

## **Установка**
Убедитесь, что у вас установлен Python 3.7 или выше.<br>
Установите зависимости, используя команду:
pip install -r requirements.txt

## **Использование**
Запустите голосового помощника, выполнив команду:<br>
python main.py

Произнесите команду для голосового помощника. Он будет ожидать триггерное слово "захар".<br> 
Затем произнесите фразу, содержащую команду, которую вы хотите выполнить.

## **Работа с кодом**
Функция callback используется для получения данных с микрофона и добавления их в очередь.<br>
Функция recognize принимает распознанный текст, векторизатор и классификатор. Она ищет триггерные слова в тексте, затем векторизует текст и выполняет предсказание с помощью классификатора. После этого она вызывает соответствующую функцию на основе предсказанного ответа.<br>
Функция main подготавливает модель классификации и запускает голосовой помощник.

## **Настройка**
Данные для обучения модели в файле words.py можно дополнить и реализованные функции, которые выполняются при определенных командах, в файле functions.py можно расширить.
