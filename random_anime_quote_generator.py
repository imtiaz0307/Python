import requests as req

# api url
url = "https://animechan.vercel.app/api"

def res_to_str(data):
    character = data["character"]
    anime = data["anime"]
    quote = data["quote"]
    res_string = f"\nQuote by: {character}\nFrom: {anime}\nQuote: {quote}\n"
    return res_string

def get_data(full_url):
    print("Getting the data.\n")
    response = req.get(full_url)
    data = response.json()

    if type(data) == type([]):
        for i in range(len(data)):
            res_string = res_to_str(data[i])
            print(f"{i + 1}. {res_string}")
    elif type(data) == type({}):
        res_string = res_to_str(data)
        print(res_string)

api_options = [ "Get a random quote.", "Get random quote by anime name.", "Get 10 random quotes", "Get 10 quotes by anime name."]

while True:
    for i in range(len(api_options)):
        print(f"{i + 1}. {api_options[i]}")

    user_choice = int(input("Choose an option: "))

    if user_choice == 1:
        get_data(f"{url}/random")
    elif user_choice == 2:
        anime_name = input("Enter Anime name:")
        get_data(f"{url}/random/anime?title={anime_name}")
    elif user_choice == 3:
        get_data(f"{url}/quotes")
    elif user_choice == 4:
        anime_name = input("Enter Anime name:")
        get_data(f"{url}/quotes/anime?title={anime_name}")
    else:
        print("Invalid Choice!")