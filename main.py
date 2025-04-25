import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv


def create_message_text(completed_modules, modules_progress, time):
    completed_modules_text = f"""
    Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. 
    В процессе я выполнил модули: {', '.join(completed_modules)}! 
    Сейчас я работаю над модулями {', '.join(modules_progress)}.
    Обучение мне нравится, я получил море знаний!
    """

    progress_modules_text = f"""
    Привет Мама(Папа), я занимаюсь в школе третье место уже {time}.
    Сейчас я работаю над модулями {', '.join(modules_progress)}. 
    Пока что я улучшаю свои навыки и узнаю много нового!
    """

    availability_completed_modules = input('У вас есть завершенные модули (Да / Нет): ')
    if availability_completed_modules.lower() == 'да':
        return completed_modules_text
    else:
        return progress_modules_text


def main():
    load_dotenv()

    completed_modules = ['Командная строка', 'Git и GitHub', 'WEB разработка (HTML / CSS)', 'Введение JavaScript', 'API веб-сервисов']
    modules_progress = ['Основы Python', 'Python введение', 'Основы JavaScript', 'Знакомство с Django: ORM', 'Вёрстка для питониста', 'Математика и статистика для Data Science', 'Продвинутая вёрстка Html/Css']
    time = '2 года'

    body = create_message_text(completed_modules, modules_progress, time)

    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    username = os.getenv('EMAIL_USERNAME')
    password = os.getenv('EMAIL_PASSWORD')

    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = os.getenv('RECEIVER_EMAIL')
    subject = 'Мои успехи'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Письмо успешно отправлено!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        server.quit()


if __name__ == '__main__':
    main()