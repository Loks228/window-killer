import pygetwindow as gw
import sys
import codecs
from win10toast_click import ToastNotifier

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def close_windows(window_titles):
    closed_windows = []
    not_found_windows = []

    for title in window_titles:
        # Получаем список окон с указанным заголовком
        windows = gw.getWindowsWithTitle(title)
        print(windows)

        if windows:
            for window in windows:
                window.close()  # Закрываем окно
                closed_windows.append(window.title)
                print(f"Закрыто окно: {window.title}")
                toaster = ToastNotifier()
                toaster.show_toast(
                    "Еще раз Здарова выбледок!",
                    f"ТЫ пошел нахуй с этим окном: {window.title}",
                threaded=True,
                duration=20,
                )    
        else:
            not_found_windows.append(title)

    # Проверяем, были ли закрыты окна
    if closed_windows:
        print(f"Закрыты окна: {', '.join(closed_windows)}")
        toaster = ToastNotifier()
        toaster.show_toast(
            "Пупсик!",
            f"Тебе закрыли эти окна что бы хуйнёй не страдал: {closed_windows}",
        threaded=True,
        duration=20,
        )  
    
    # Проверяем, были ли не найдены окна
    if not_found_windows:
        print(f"Окна не найдены: {', '.join(not_found_windows)}")
        toaster = ToastNotifier()
        toaster.show_toast(
            "Здарова выбледок!",
            "какого хуя ты не ИГРАЕШЬ на ИГРОВО ПК)",
        duration=20,
        )            

if __name__ == "__main__":
    # Укажите названия окон, которые хотите закрыть
    window_titles = [
        "Counter-Strike",  # Замените на нужные заголовки
        "Dota 2",
        "Rust",
        "Steam"
    ]

    close_windows(window_titles)
