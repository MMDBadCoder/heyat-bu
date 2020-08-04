line = input()
words = line.split(" ")
height = int(words[0])
width = int(words[1])

# s = int(input())

broken_cells_number = int(input())

# get broken cells from input
broken_cells = []
for i in range(broken_cells_number):
    line = input()
    words = line.split(" ")
    broken_cells.append([int(words[0]) - 1, int(words[1]) - 1])

# initialize table
table = []
for i in range(height):
    table.append([])
    for j in range(width):
        table[i].append(
            {
                'broken': False,
                'up_left_corners': []
            }
        )

# pick broken cells in table
for broken_cell in broken_cells:
    table[broken_cell[0]][broken_cell[1]]['broken'] = True

# set left space of each cell
for i in range(height):
    left_broken = -1
    for j in range(width):
        cell = table[i][j]
        cell['left_broken'] = left_broken

        if cell['broken']:
            left_broken = j

# set up space of each cell
for i in range(width):
    up_broken = -1
    for j in range(height):
        cell = table[j][i]
        cell['up_broken'] = up_broken

        if cell['broken']:
            up_broken = j

# set up_left_corner of up and left border cells
for i in range(height):
    cell = table[i][0]
    cell['up_left_corners'].append(
        [cell['up_broken'] + 1, 0]
    )
for i in range(1, width):
    cell = table[0][i]
    cell['up_left_corners'].append(
        [0, cell['left_broken'] + 1]
    )

for i in range(1, height):
    for j in range(1, width):
        cell = table[i][j]
        up_cell = table[i - 1][j]
        left_cell = table[i][j - 1]

        if up_cell['broken']:
            cell['up_left_corners'] = [[i, cell['left_broken'] + 1]]
            continue

        if left_cell['broken']:
            cell['up_left_corners'] = [[cell['up_broken'] + 1, j]]
            continue

        new_up_left_corners = []

        for up_left_corner in up_cell['up_left_corners'] + left_cell['up_left_corners']:
            new_up_left_corners.append(
                [max(cell['up_broken'] + 1, up_left_corner[0]), max(cell['left_broken'] + 1, up_left_corner[1])]
            )

        # cleaning list and remove repeated items
        for cell1 in new_up_left_corners:
            for cell2 in new_up_left_corners:
                if cell1 != cell2 and cell2[0] <= cell1[0] and cell2[1] <= cell1[1]:
                    new_up_left_corners.remove(cell2)

        for up_left_corner in new_up_left_corners:
            if not cell['up_left_corners'].__contains__(up_left_corner):
                cell['up_left_corners'].append(up_left_corner)

# clear broken cells
for broken_cell in broken_cells:
    table[broken_cell[0]][broken_cell[1]]['up_left_corners'] = []


# special operand of question 3 of contest

def get_answers():
    answers = []
    for i in range(height):
        for j in range(width):
            cell = table[i][j]

            if cell['broken']:
                continue

            bottom_cell = None
            right_cell = None

            if i + 1 != height:
                bottom_cell = table[i + 1][j]

            if j + 1 != width:
                right_cell = table[i][j + 1]

            for up_left_corner in cell['up_left_corners']:
                if (not right_cell or not right_cell['up_left_corners'].__contains__(up_left_corner)) and \
                        (not bottom_cell or not bottom_cell['up_left_corners'].__contains__(up_left_corner)):
                    answers.append([up_left_corner[0], up_left_corner[1], i, j])
    return answers


answers = get_answers()
print(answers.__len__())

from q2_test_ans import get_correct_answers
correct_answers = get_correct_answers(cells=broken_cells, answers=answers, height=height, width=width)
print(correct_answers.__len__())