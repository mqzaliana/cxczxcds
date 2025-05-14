# # 'Угадай число'
# import random

# def get_user_guess():
#     """Запрашивает ввод пользователя и обрабатывает ошибки."""
#     while True:
#         try:
#             guess = int(input("Введите число от 1 до 100: "))
#             if 1 <= guess <= 100:
#                 return guess
#             else:
#                 print("Число должно быть от 1 до 100.")
#         except ValueError:
#             print("Ошибка: пожалуйста, введите целое число.")

# def play_game():
#     """Основная логика игры 'Угадай число'."""
#     secret_number = random.randint(1, 100)
#     attempts = 0
#     max_attempts = 10

#     print("Я загадал число от 1 до 100. Угадай его!")

#     while attempts < max_attempts:
#         guess = get_user_guess()
#         attempts += 1

#         if guess < secret_number:
#             print("Загаданное число больше.")
#         elif guess > secret_number:
#             print("Загаданное число меньше.")
#         else:
#             print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
#             break
#     else:
#         print(f"Вы проиграли. Загаданное число было: {secret_number}")

# def main():
#     """Запуск игры и предложение сыграть снова."""
#     while True:
#         play_game()
#         again = input("Хотите сыграть ещё раз? (да/нет): ").strip().lower()
#         if again != "да":
#             print("Спасибо за игру! До свидания.")
#             break

# if __name__ == "__main__":
#     main()


# Генерация случайной истории 

import random

def initialize_data():
    """Создаёт списки с элементами для генерации истории."""
    heroes = [
        "смелый рыцарь", "хитрый вор", "волшебник",
        "отважный пират", "дерзкий исследователь"
    ]
    places = [
        "в далёком королевстве", "на заброшенной фабрике",
        "в густом лесу", "на просторах космоса", "у подножия гор"
    ]
    events = [
        "победил дракона", "обнаружил сокровища",
        "выиграл битву", "устроил бал", "раскрыл древнюю тайну"
    ]
    details = [
        "с волшебным мечом", "на летающем ковре",
        "под звуки волшебной музыки", "с удивительной силой",
        "в сопровождении магического существа"
    ]
    return heroes, places, events, details

def generate_story(heroes, places, events, details):
    """Генерирует случайную историю из переданных списков."""
    hero = random.choice(heroes)
    place = random.choice(places)
    event = random.choice(events)
    detail = random.choice(details)

    story = f"📖 История:\n{'-'*40}\n{hero} {place} {event} {detail}.\n{'-'*40}"
    return story

def save_story(story, filename="stories.txt"):
    """Сохраняет историю в текстовый файл."""
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(story + "\n\n")
        print("✅ История сохранена в файл.")
    except IOError:
        print("❌ Ошибка при сохранении истории в файл.")

def ask_play_again():
    """Спрашивает, хочет ли пользователь сгенерировать новую историю."""
    answer = input("Хотите сгенерировать новую историю? (да/нет): ").strip().lower()
    return answer == "да"

def main():
    print("🎲 Добро пожаловать в Генератор Историй!")
    heroes, places, events, details = initialize_data()

    while True:
        story = generate_story(heroes, places, events, details)
        print("\n" + story)

        save = input("Хотите сохранить эту историю в файл? (да/нет): ").strip().lower()
        if save == "да":
            save_story(story)

        if not ask_play_again():
            print("👋 Спасибо за игру! До встречи.")
            break

if __name__ == "__main__":
    main()