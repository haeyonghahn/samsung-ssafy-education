def star_dist(dist):
  first_line_length = 3 + dist * 2
  print('*' + ' '*dist + '*' + ' '*dist + '*')
  
  if dist % 2 == 0:
    second_side_dist = int((first_line_length - ( 2 + dist - 1 )) / 2)
    print(' '*second_side_dist + '*' + ' '*(dist-1) + '*')
  else:
    second_side_dist = int(((first_line_length) - (2 + dist)) / 2)
    print(' '*second_side_dist + '*' + ' '*dist + '*')
        
    
N = int(input())
star_dist(N)