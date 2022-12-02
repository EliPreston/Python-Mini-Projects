import json
import os



filenames = next(os.walk('Compiled Playlists JSON Files'))[2]
print(filenames)

for fileName in filenames:
    print(fileName)
    start = fileName.index('(') + 1
    end = fileName.index(')')
    userIDfromfileName = fileName[start:end]
    print(userIDfromfileName)


# data = json.load(f)
# # print(data)

# id_list = []
# for playListID in data:
#     # print(playListID)
#     id_list.append(playListID)

# print(id_list)
# f.close()