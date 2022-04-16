def main():
    time = input("What time is it? ")
    hours = convert(time)
    #print(hours)
    if hours >= 7 and hours <= 8:
        print("breakfast time")
    elif hours >= 12 and hours <= 13:
        print("lunch time")
    elif hours >= 18 and hours <= 19:
        print("dinner time")


def convert(time):
    time = time.split(":")
    minutes = float(time[1]) / 60
    return(float(time[0]) + minutes)


if __name__ == "__main__":
    main()
