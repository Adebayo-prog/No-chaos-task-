for hundredunit in range(1, 10):
    for tensdigit in range(0, 10):
        for unitsdigit in range(0, 10):
            number = hundredunit * 100 + tensdigit * 10 + unitsdigit
            sum = (hundredunit * hundredunit) + (tensdigit * tensdigit) + (unitsdigit * unitsdigit)
            
            if sum == number:
                print("weldone great work")

print("please try again")

