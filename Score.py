import os
from Utils import SCORES_FILE_NAME
from e2e import main_function


def add_score(difficulty):
    folder = os.path.dirname(__file__)
    path = os.path.join(folder, SCORES_FILE_NAME)
    points = (difficulty * 3) + 5

    if os.path.exists(path):
        with open(SCORES_FILE_NAME, "r") as score:
            for lines in score.readlines():
                current_point = int(lines)
                points += current_point
            score.close()

        with open(SCORES_FILE_NAME, "w") as score:
            score.write(str(points))
    else:
        with open(SCORES_FILE_NAME, "w") as score:
            score.write(str(points))

    score.close()
    main_function()
