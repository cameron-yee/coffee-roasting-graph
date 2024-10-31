import matplotlib.pyplot as plt


def read_values():
    f = open("config.txt", "r")
    lines = f.readlines()

    return (
        [float(x.strip()) for x in lines[:1]][0],
        [float(x.strip()) for x in lines[2:]]
    )


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
