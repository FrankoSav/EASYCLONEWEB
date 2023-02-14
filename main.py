import requests


def clonar(url):
    try:
        datos = requests.get(url)
        with open("file.html", "wb") as guarda:
            guarda.write(datos.content)
        return "Done..."
    except Exception as e:
        return f"Error: {str(e)}"

def banner():
    banner = "EASYCLONEWEB"
        print(banner)
        print("By:FrankoSav")


            banner()

while True:
    print("Choose Option?")
    print("1 - Clone")
    print("2 - Exit")

    choice = input("Enter the number: ")

    if choice == "1":
        # Prompt the user to enter a URL to clone
        url = input("Enter the URL of the page you want to clone: ")

        datos = clonar(url)
        print(datos)

    elif choice == "2":
        print("Goodbye")
        break

    else:
        print("Invalid input.")
