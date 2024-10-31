import matplotlib.pyplot as plt


def read_values():
    try:
        f = open("config.txt", "r")
        lines = [x for x in f.readlines() if x != "\n"]

        return (
            float(lines[0].strip()),
            [float(x.strip()) for x in lines[1:]]
        )
    except ValueError:
        print('Invalid values found in config.txt')
        quit(1)
    except FileNotFoundError:
        print('No config.txt file found')
        quit(1)


def main():
    time_interval, temps = read_values()
    times = [x * time_interval for x in range(len(temps))]

    plt.plot(times, temps, scalex=False, scaley=False)

    plt.xlabel('Minutes')
    plt.xlim(0, max(times) + 1)

    plt.ylabel('Temperature')
    plt.ylim(0, max(temps) + 100)

    plt.title('Coffee Roast Temp/Time')
    plt.show()


if __name__ == "__main__":
    main()
