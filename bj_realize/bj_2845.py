people, area = input().split(" ")
count = int(people) * int(area)
papers = [int(paper) for paper in input().split()]

for i in range(len(papers)):
    print(papers[i] - count, end=" ")


