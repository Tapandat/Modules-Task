from lucky_draw import draw_lucky_number

try:
    attempts = int(input("Enter number of tries: "))

    if attempts <= 0:
        raise ValueError("Attempts must be greater than 0")

    for i in range(attempts):
        num = draw_lucky_number()
        print("Drawn number:", num)

        if num == 3:
            print("🎉 You won the lucky draw!")
            break
    else:
        print("😢 Better luck next time!")

except ValueError as ve:
    print("Invalid input:", ve)

except Exception as e:
    print("Something went wrong:", e)
