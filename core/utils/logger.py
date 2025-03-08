import sys
import re
from datetime import date
from loguru import logger


class QTextEditHandler:
    def __init__(self, *args, **kwargs):
        pass
    def write(self, message):
        print(message)


def logging_setup(gui_mode=False, text_edit=None):
    format_info = "<green>{time:HH:mm:ss.SS}</green> <blue>{level}</blue> <level>{message}</level>"
    format_error = "<green>{time:HH:mm:ss.SS}</green> <blue>{level}</blue> | " \
                   "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>"
    file_path = r"logs/"

    logger.remove()  # Удаляем все предыдущие обработчики
    # if sys.platform == "win32":

    # In console mode, add handlers for both file and stdout
    logger.add(file_path + f"out_{date.today().strftime('%m-%d')}.log", colorize=True,
               format=format_info)
    logger.add(sys.stdout, colorize=True, format=format_info, level="INFO")


def clean_brackets(raw_str):
    clean_text = re.sub(brackets_regex, '', raw_str)
    return clean_text


# Regex pattern for matching HTML-style brackets
brackets_regex = re.compile(r'<.*?>')

# Пример использования (предполагается, что `text_edit` — это ваш экземпляр QTextEdit):
# Example usage (assuming `text_edit` is your QTextEdit instance):
logging_setup(gui_mode=False)
