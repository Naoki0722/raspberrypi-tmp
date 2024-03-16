from src import Dht, Line


def main():
    line = Line()
    dht = Dht()
    line.send(dht.get_message())


if __name__ == "__main__":
    main()
