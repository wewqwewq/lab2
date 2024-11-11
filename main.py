import random

def угадай_число():

  secret_number = random.randint(1, 10)
  attempts = 3

  print("Я загадал число от 1 до 10. Угадай его за 3 попытки!")

  for attempt in range(attempts):
    guess = int(input(f"Попытка {attempt + 1}: Введите число: "))

    if guess == secret_number:
      print(f"Поздравляю! Ты угадал число за {attempt + 1} попытку!")
      return

    elif guess < secret_number:
      print("Загаданное число больше.")

    else:
      print("Загаданное число меньше.")

  print(f"К сожалению, ты не угадал. Загаданное число было {secret_number}.")

if __name__ == "__main__":
  угадай_число()
