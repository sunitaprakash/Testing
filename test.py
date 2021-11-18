import os
  
print(os.getenv('GRID_URL:' "GRID_URL"))
print('testing env')
print('List of file in current direcoty"')
path ='.'
dir_list= os.listdir(path)
print(dir_list)
