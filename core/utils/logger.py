import sys
import re
from datetime import date
from loguru import logger

def logging_setup(gui_mode=False, text_edit=None):
    """
    Sets up logging configuration for both GUI and console modes.
    
    Args:
        gui_mode (bool): If True, logs will be directed to QTextEdit widget
        text_edit (QTextEdit): Text widget for displaying logs in GUI mode
    """
    format_info = "<green>{time:HH:mm:ss.SS}</green> <blue>{level}</blue> <level>{message}</level>"
    format_error = "<green>{time:HH:mm:ss.SS}</green> <blue>{level}</blue> | " \
                   "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>"
    file_path = r"logs/"

    logger.remove()  # Remove all previous handlers

    # In console mode, add handlers for both file and stdout
    logger.add(file_path + f"out_{date.today().strftime('%m-%d')}.log", colorize=True,
               format=format_info)
    logger.add(sys.stdout, colorize=True, format=format_info, level="INFO")


def clean_brackets(raw_str):
    """
    Removes HTML-style brackets from string.
    
    Args:
        raw_str (str): Input string containing HTML-style brackets
        
    Returns:
        str: Cleaned string without brackets
    """
    clean_text = re.sub(brackets_regex, '', raw_str)
    return clean_text


# Regex pattern for matching HTML-style brackets
brackets_regex = re.compile(r'<.*?>')

# Пример использования (предполага��тся, что `text_edit` — это ваш экземпляр QTextEdit):
# Example usage (assuming `text_edit` is your QTextEdit instance):
logging_setup(gui_mode=False)
