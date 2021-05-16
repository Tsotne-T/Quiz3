# import requests
# import json
# import sqlite3


# ## Get()
# r =  requests.get('https://animechan.vercel.app/api/quotes')
# res = r.json()
# # print(json.dumps(res,indent=4))

# ## Status Code 
# # r =  requests.get('https://animechan.vercel.app/api/random')
# # print(r)

# ## Header 
# # r =  requests.get('https://animechan.vercel.app/api/random')
# # print(r.headers)


# with open("Anime.json","w") as f:
#     json.dump(res, f, indent=4)

# with open('Anime.json') as json_file:
#     data = json.load(json_file)

#     # print(data[1]['quote'])

# conn = sqlite3.connect("anime_quote.sqlite")
# c = conn.cursor()



# c.execute('''CREATE TABLE IF NOT EXISTS Anime
#             (id INTEGER PRIMARY KEY AUTOINCREMENT,
#             character VARCHAR(50),
#             quote VARCHAR(1000));''')

# Characters = data[1]['character']
# Quotes = data[1]['quote']
# AQ = (Characters, Quotes)

# c.execute("INSERT INTO Anime(character, quote) VALUES(?,?)", (Characters, Quotes))
# conn.commit()

# conn.close
