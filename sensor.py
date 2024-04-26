import time

def get_temp():
    #call api to get temp from sensor
    pass
    return(Temperature)
#user_comfort = int(input("How much temperature do you want? "))
def AC_signal(comfort_temp):
    current_temp = get_temp()
    AC_control_u = comfort_temp - current_temp  # Adjust AC based on the difference between comfort and current temp
    ####Record for dashboard ###
    print(AC_control_u)
    return AC_control_u

#connect with api ACcontrol to AC
def main():
    comfort_temp = 20
    #cunning continiously
    while True:
        AC_signal(comfort_temp)
        time.sleep(1800)
    
if __name__ == "__main__":
    main()
