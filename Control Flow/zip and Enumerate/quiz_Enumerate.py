cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]


for i , cast2 in enumerate(cast):
    cast[i] = cast2 + " "+ str(heights[i])


print(cast)