import tkinter as tk
import random
import time

# Список случайных слов
words = ["Понос будит", "Да", "Нет", "Не знаю", "Я думаю ты дебил", "GMiR...", "Загрузка....................................."]

def start_loading():
    # Скрыть кнопку и поле ввода
    entry.pack_forget()
    submit_button.pack_forget()
    
    # Показать анимацию загрузки
    loading_label.pack()
    loading_animation()

def loading_animation():
    # Анимация загрузки
    for i in range(10):
        loading_label.config(text="Загрузка" + "." * (i % 3 + 1))
        root.update()
        time.sleep(0.3)
    
    # После завершения загрузки показать случайные слова
    loading_label.pack_forget()
    show_random_words()

def show_random_words():
    # Генерация и отображение случайных слов
    random_words = random.sample(words, 1)
    result_label.config(text=", ".join(random_words))
    result_label.pack(pady=20)

# Создание главного окна
root = tk.Tk()
root.title("СВЯЗЬ С ТАРАКАНОМ ОРАКУЛОМ")
root.geometry("400x300")
root.configure(bg="#e0f7fa")  # Устанавливаем светло-голубой фон

# Стиль шрифта
font_style = ("Helvetica", 14)

# Рамка для ввода и кнопки
frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.GROOVE)
frame.pack(pady=20, padx=20, fill=tk.BOTH)

# Поле ввода
entry = tk.Entry(frame, font=font_style, width=30, bd=2, relief=tk.SUNKEN)
entry.pack(pady=10, padx=10)

# Кнопка отправки
submit_button = tk.Button(frame, text="Отправить", command=start_loading, font=font_style, bg="#00796b", fg="white", bd=0)
submit_button.pack(pady=10)

# Метка для анимации загрузки
loading_label = tk.Label(root, text="", font=font_style, bg="#e0f7fa", fg="#00796b")
result_label = tk.Label(root, text="", font=font_style, bg="#e0f7fa", fg="#00796b")

# Запуск главного цикла
root.mainloop()
