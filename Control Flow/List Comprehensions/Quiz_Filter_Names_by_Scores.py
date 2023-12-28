scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

# passed =  [name for name in scores if scores[name] > 65 ]
passed = [name for name, score in scores.items() if score >= 65]

print(passed)
 # write your list comprehension here