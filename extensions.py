def main():
    user_input = input("File name: ").lower().strip()
    print(file_type(user_input))

def file_type(string):
    string = string.split(".")
    types = {"gif":'image/gif',"jpg":"image/jpeg","jpeg":"image/jpeg","pdf":"application/pdf","png":"image/png","zip":"application/zip","txt":"text/plain"}
    return types.get(string[-1], "application/octet-stream")

if __name__ == "__main__":
    main()
