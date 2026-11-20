"""
(Mastermind)
نام: محمد افتخاری
شماره دانشجویی: 404130383
"""

import random  # فقط برای ساختن رمز تصادفی استفاده شده


def show_info():
    
    print("Guess the 4-digit code (digits 1 to 6, no repeats).")
    print("You have 10 tries.\n")


def make_secret():
    # ساخت رمز چهار رقمی تصادفی بدون رقم تکراری
    secret = ""
    while len(secret) < 4:
        d = str(random.randrange(1, 7))
        # اگر رقم قبلا در رمز نیامده باشد اضافه میشود
        if d not in secret:
            secret = secret + d
    return secret


def is_valid(guess):
    # بررسی تعداد ارقام
    if len(guess) != 4:
        print("Error: enter exactly 4 digits.")
        return False

    # بررسی اینکه همه کاراکترها بین 1 تا 6 باشند
    for ch in guess:
        if ch not in "123456":
            print("Error: only digits 1 to 6 are allowed.")
            return False

    # بررسی رقم تکراری: هر رقم را با ارقام بعدی مقایسه میکنیم
    for i in range(4):
        for j in range(i + 1, 4):
            if guess[i] == guess[j]:
                print("Error: digits must not repeat.")
                return False

    return True


def correct_place(secret, guess):
    # شمردن ارقام درست در مکان درست
    count = 0
    for i in range(4):
        if secret[i] == guess[i]:
            count += 1
    return count


def wrong_place(secret, guess):
    # شمردن ارقامی که در رمز هستند ولی مکانشان اشتباه است
    count = 0
    for i in range(4):
        if secret[i] != guess[i] and guess[i] in secret:
            count += 1
    return count


def play():
    # یک دور کامل بازی
    secret = make_secret()
    tries = 0

    while tries < 10:
        print("Tries left:", 10 - tries)
        guess = input("Your guess: ")

        # ورودی نامعتبر از فرصت ها کم نمیکند
        if not is_valid(guess):
            continue

        tries += 1
        a = correct_place(secret, guess)
        b = wrong_place(secret, guess)
        print("Correct digit, correct place:", a)
        print("Correct digit, wrong place  :", b)
        print()

        # اگر هر چهار رقم درست بود بازیکن برنده است
        if a == 4:
            print("You won! Number of tries:", tries)
            return

    # فرصت ها تمام شد: بازیکن باخته و رمز نمایش داده میشود
    print("You lost! The secret code was:", secret)


def PlayGame():
    # برنامه اصلی: نمایش اطلاعات و اجرای بازی (با امکان بازی دوباره)
    show_info()
    again = "y"
    while again == "y":
        play()
        again = input("Play again? (y/n): ")
        print()

PlayGame()