# Extract links from html file

# with open("exercise.html", "r") as rf:
#     with open("links.txt", "a") as wf:
#         for line in rf.readlines():
#             if '<a href=' in line:
#                 pos = line.find('<a href=')
#                 first_quote = line.find('\"', pos)
#                 second_quote = line.find('\"', first_quote+1)
#                 url = line[first_quote+1:second_quote]
#                 wf.write(url + '\n')


with open("exercise.html", "r") as rf:
    with open("links.txt", "a") as wf:
        line = rf.read()
        link_exist = True
        while link_exist:
            pos = line.find('<a href=')
            if pos == -1:
                link_exist = False
            else:
                first_quote = line.find('\"', pos)
                second_quote = line.find('\"', first_quote+1)
                url = line[first_quote+1:second_quote]
                wf.write(url + '\n')
                line = line[second_quote:]