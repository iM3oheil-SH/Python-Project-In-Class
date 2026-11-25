films = ["F1", "F2", "F3", "F4"]

votes = [
    ("S01", "F2"),
    ("S02", "F1"),
    ("S01", "F2"),
    ("S01", "F1"),
    ("S03", "F1"),
    ("S04", "F2"),
    ("S02", "F3"),
    ("S05", "F2"),
]

accepted = set()
rejected = []

counts = {}
students = {}
first_vote = {}

for film in films:
    counts[film] = 0
    students[film] = set()

for i, vote in enumerate(votes):

    student, film = vote

    if (student, film) not in accepted:

        accepted.add((student, film))
        counts[film] += 1
        students[film].add(student)

        if film not in first_vote:
            first_vote[film] = i

    else:
        rejected.append(vote)


results = sorted(
    films,
    key=lambda film: (
        counts[film] == 0,
        -counts[film],
        first_vote.get(film, len(votes) + films.index(film))
    )
)

print("Rejected Votes:")
for vote in rejected:
    print(vote)

print("Results:")
for film in results:
    print(film, ":", counts[film])

first = students[results[0]]
second = students[results[1]]

common = first.intersection(second)

print("Common Students:")
print(common)