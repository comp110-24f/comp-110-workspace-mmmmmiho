"""This is a practice of elif"""


def get_weather_report() -> str:  # coron
    weather = str(input("What is the weather? "))  # input
    if weather == "rainy" or "cold":  # 普通のorを使える、not = but ==
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recogniza this weather.")

    return weather  # defの中に入れる


get_weather_report()  # 呼び出しがないと"What is the weather?"はきいてくれない
