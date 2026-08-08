
file_location = input("please enter the file location: ")

valid_temperature_log = []

try:
    with open(file_location,"r") as file:
        temperature_log = file.readlines()
        for i in range(len(temperature_log)):
            try :
                valid_temperature_log.append(float(temperature_log[i].strip()))
            except ValueError :
                print("value of the line" , i+1 , "is not valid")

        if len(valid_temperature_log) == 0:
            print("no valid temperature data found")
        else:    

                #length of the temperature log
                temperature_length = len(valid_temperature_log)

                #maximum temperature
                max_temperature = max(valid_temperature_log)

                #minimum temperature
                min_temperature = min(valid_temperature_log)

                #average temerature
                average_temperature = sum(valid_temperature_log) / temperature_length




            with open("summary.txt", "w") as file:
                file.write(f"number of samples: {temperature_length}\n")
                file.write(f"maximum temperature: {max_temperature}\n")
                file.write(f"minimum temperature: {min_temperature}\n")
                file.write(f"average temperature: {average_temperature}\n")


except FileNotFoundError:
    print("file is not found")


finally:
    print("program finished")
