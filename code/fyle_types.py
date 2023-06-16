file_name = input("File name: ").lower()
if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg"):
    print("image/jpg")
elif file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".pdf"):
    print("image/pdf")
elif file_name.endswith(".txt"):
    print("document/pdf")
elif file_name.endswith(".txt"):
    print("document/txt")
elif file_name.endswith(".zip"):
    print(file/zip)
else:
    print("application/octet-stream")
