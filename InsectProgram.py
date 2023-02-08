import InsectClass as i


def main():
    house_fly = i.Insect()
    house_fly.setFlight()
    mosquito = i.Insect()
    mosquito.setFlight()

    print("House fly flight length: " + str(house_fly.getFlight()))
    print()
    print("Mosquito flight length: " + str(mosquito.getFlight()))


main()
