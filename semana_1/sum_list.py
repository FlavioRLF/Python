def soma_matrizes(m1,m2):
    if len(m1) == len(m2):
        zipped_lists = zip(m1, m2)
#zipped_lists` contains pairs of items from both lists
        sum = [x + y for (x, y) in zipped_lists]
#Create a list with the sum of each pair
        print("soma_matrizes(m1, m2) => ["+str(sum)+"]")
    else:
        print(bool(False))

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1,m2)