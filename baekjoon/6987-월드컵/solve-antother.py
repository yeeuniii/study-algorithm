import sys

NUMBER_OF_COUNTRY = 6
TESTCASE = 4


def backtracking(win, draw, lose, team1, team2, time):
    if time == 15:
        if sum(win) or sum(draw) or sum(lose):
            return False
        return True

    is_valid = False
    if team2 == NUMBER_OF_COUNTRY:
        team1 += 1
        team2 = team1 + 1

    if win[team1] > 0 and lose[team2] > 0:
        win[team1] -= 1
        lose[team2] -= 1
        if backtracking(win, draw, lose, team1, team2 + 1, time + 1):
            return True
        win[team1] += 1
        lose[team2] += 1
    if draw[team1] > 0 and draw[team2] > 0:
        draw[team1] -= 1
        draw[team2] -= 1
        if backtracking(win, draw, lose, team1, team2 + 1, time + 1):
            return True
        draw[team1] += 1
        draw[team2] += 1

    if lose[team1] > 0 and win[team2] > 0:
        lose[team1] -= 1
        win[team2] -= 1
        if backtracking(win, draw, lose, team1, team2 + 1, time + 1):
            return True
        lose[team1] += 1
        win[team2] += 1
    return is_valid


def main():
    for _ in range(TESTCASE):
        input = list(map(int, sys.stdin.readline().strip().split()))
        win = list()
        draw = list()
        lose = list()
        for idx in range(NUMBER_OF_COUNTRY):
            win.append(input[3 * idx])
            draw.append(input[3 * idx + 1])
            lose.append(input[3 * idx + 2])
        print(1 if backtracking(win, draw, lose, 0, 1, 0) else 0)


if __name__ == "__main__":
    main()