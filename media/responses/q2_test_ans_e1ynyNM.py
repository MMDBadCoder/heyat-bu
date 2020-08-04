def get_correct_answers(cells, answers, height, width):
    cells_by_first = {}
    for cell in cells:
        if not cells_by_first.__contains__(cell[0]):
            cells_by_first[cell[0]] = []

        cells_by_first[cell[0]].append(cell[1])

    cells_by_second = {}
    for cell in cells:
        if not cells_by_second.__contains__(cell[1]):
            cells_by_second[cell[1]] = []

        cells_by_second[cell[1]].append(cell[0])

    correct_answers = []
    for answer in answers:
        certificates = 0
        # up:
        upper_row = answer[0] - 1
        if upper_row is -1:
            certificates += 1
        if cells_by_first.__contains__(upper_row):
            for cell in cells_by_first[upper_row]:
                if cell >= answer[1] and cell <= answer[3]:
                    certificates += 1
                    break

        # bottom:
        bottom_row = answer[2] + 1
        if bottom_row is height:
            certificates += 1
        if cells_by_first.__contains__(bottom_row):
            for cell in cells_by_first[bottom_row]:
                if cell >= answer[1] and cell <= answer[3]:
                    certificates += 1
                    break

        # left:
        left_col = answer[1] - 1
        if left_col is -1:
            certificates += 1
        if cells_by_second.__contains__(left_col):
            for cell in cells_by_second[left_col]:
                if cell >= answer[0] and cell <= answer[2]:
                    certificates += 1
                    break

        # right:
        right_col = answer[3] + 1
        if right_col is width:
            certificates += 1
        if cells_by_second.__contains__(right_col):
            for cell in cells_by_second[right_col]:
                if cell >= answer[0] and cell <= answer[2]:
                    certificates += 1
                    break

        if certificates == 4:
            correct_answers.append(answer)

    return correct_answers
