def main():
    print(outdated())

def outdated():
    months = [
		"January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
		"August",
		"September",
		"October",
		"November",
		"December"
        ]
    while True:
         date1 = input("Date: ")
         try:
            date = date1.split("/") if "/" in date1 else date1.split()
            if len(date) != 3:
                raise ValueError(1)
            elif "/" in date1 and not all(i.isnumeric() for i in date):
                raise ValueError(2)
            elif "/" not in date1 and date[0].title() not in months:
                raise ValueError(3)
            elif "/" not in date1 and (date1.count(",") != 1 or date[1][-1] != ","):
                raise ValueError(4)
            elif not (0 <= int(date[2]) <= 10000 and 0< int(date[1].replace(",","")) < 32):
                raise ValueError(5)
            elif "/" in date1 and not (0 < int(date[0]) < 13):
                raise ValueError(6)
         except ValueError:
             pass
         else:
            if "/" not in date1:
                month = months.index(date[0].title()) + 1
                return f"{int(date[2]):04}-{int(month):02}-{int(date[1][:-1]):02}"
            elif "/" in date1:
                return f"{int(date[2]):04}-{int(date[0]):02}-{int(date[1]):02}"

if __name__ == "__main__":
	main()
