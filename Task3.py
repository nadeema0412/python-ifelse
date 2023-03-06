# Write a function that takes two arrays and prints the members of the first
# array that are present in the second array.
def TakeTwoArrays(A, B):
    for i in A:
        if i in B:
            print(i)

Score_A = [12, 13, 23, 43]
Score_B = [13, 18, 17, 23]
print(TakeTwoArrays(Score_A, Score_B))
