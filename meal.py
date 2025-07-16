def main():
    user_input = input("what time is it? ")
    time = convert(user_input)

def convert(time):
    no_surfix = time.replace(' a.m.', '').replace(' p.m','')
    time_split = no_surfix.split(':')
    new_time = eval(time_split[0]) + eval(time_split[1]+'/60')
    if time == "12:00 a.m.":
        new_time = 0.0
    elif time.endswith("p.m."):
        new_time += 12.0
    if 7.00 <= new_time <= 8.00:
        print("breakfast time")
    elif 12.00 <= new_time <= 13.00:
        print("lunch time")
    elif 18.00 <= new_time <= 19.00:
        print("dinner time")
    return new_time
if __name__ == "__main__":
    main()
