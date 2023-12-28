# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
count_char = 0
for handlie in headlines:

    if (len(news_ticker) + len(handlie)) > 140:
        for char in handlie:
            if len(news_ticker) == 140:
                break
            news_ticker += char

        print(handlie)
        break
    news_ticker += handlie
    

  
print((news_ticker))
# write your loop here





# headlines = ["Local Bear Eaten by Man",
#              "Legislature Announces New Laws",
#              "Peasant Discovers Violence Inherent in System",
#              "Cat Rescues Fireman Stuck in Tree",
#              "Brave Knight Runs Away",
#              "Papperbok Review: Totally Triffic"]

# news_ticker = ""
# for headline in headlines:
#     news_ticker += headline + " "
#     if len(news_ticker) >= 140:
#         news_ticker = news_ticker[:140]
#         break

# print(news_ticker)