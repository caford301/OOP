import InsectClass as i


def main():
    house_fly = i.Insect("House Fly", 2, 4)
    house_fly.setFlight()
    mosquito = i.Insect("Mosquito", 2, 4)
    mosquito.setFlight()

    print(house_fly.getName() + " flight length: " + str(house_fly.getFlight()))
    print()
    print(mosquito.getName() + " flight length: " + str(mosquito.getFlight()))


main()
