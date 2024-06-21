from numpy import *
from matplotlib.pyplot import *

file = loadtxt('numbers.txt')
real_results = loadtxt('real_scores.txt', dtype=int)
#games = loadtxt('games.txt')
#print(real_results)
ng_so_far = len(real_results)
print('So far there were ', ng_so_far, ' games. \n')

names = ['Götz', 'Michael', 'Rodica', 'Ion', 'Sergej', 'Ulrich', 'Marius', 'Franz', 'Marvin']
nn = len(names)
ng = len(file)

xy_matrix = zeros((ng, nn, 2), dtype=int)
for i in range(ng):
    for j in range(nn):
        string_score = str(file[i, j])
        xy_matrix[i, j] = [int(string_score[0]), int(string_score[2])]



def points(x, y, x0, y0):
    distance = sqrt((x - x0) ** 2 + (y - y0) ** 2)
    if (x0>y0 and x>y) or (x0<y0 and x<y):
        points = 10 - distance**2
    elif x0 == y0 and x == y:
        points = 10 - distance**2
    else:
        points = 0
    return points

total_points = zeros(nn, dtype=int)

for j in range(nn):
    for i in range(ng_so_far):
        points_of_person = points(xy_matrix[i, j, 0], xy_matrix[i, j, 1], real_results[i][0], real_results[i][1])
        #print(xy_matrix[i, j, 0], xy_matrix[i, j, 1], ', ', real_results[i][0], real_results[i][1], ', ', points_of_person)
        #print('Points of ', names[j], ' in game ', i, ' is ', points_of_person, ' points!', '\n')
        total_points[j] += round(points_of_person)
    total_points[j] = total_points[j]
    print(names[j], ' has ', total_points[j], ' points!')
savetxt('total_points.txt', total_points)