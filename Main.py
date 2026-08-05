from Bootstrap import Bootstrap


def main():

    arg = Bootstrap().build()

    arg.start()

    arg.run()

    arg.stop()


if __name__ == "__main__":

    main()