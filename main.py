from house_builder import HouseBuilder

if __name__ == "__main__":
    builder = HouseBuilder()
    house = (builder
             .build_walls("brick")
             .build_roof("slate")
             .build_windows(4)
             .build_doors(2)
             .build())

    print(house.display())
