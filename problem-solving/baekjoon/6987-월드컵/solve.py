import sys

WIN = 0
DRAW = 1
LOSE = 2
NUMBER_OF_COUNTRY = 6
TESTCASE = 4


def backtracking(scores, team1, team2, time):
    if time == 15:
        total = 0
        for country in scores:
            total += sum(country)
        if total:
            return False
        return True

    is_valid = False
    if team2 == NUMBER_OF_COUNTRY:
        team1 += 1
        team2 = team1 + 1
    if scores[team1][WIN] > 0 and scores[team2][LOSE] > 0:
        scores[team1][WIN] -= 1
        scores[team2][LOSE] -= 1
        if backtracking(scores, team1, team2 + 1, time + 1):
            return True
        scores[team1][WIN] += 1
        scores[team2][LOSE] += 1
    if scores[team1][DRAW] > 0 and scores[team2][DRAW] > 0:
        scores[team1][DRAW] -= 1
        scores[team2][DRAW] -= 1
        if backtracking(scores, team1, team2 + 1, time + 1):
            return True
        scores[team1][DRAW] += 1
        scores[team2][DRAW] += 1
    if scores[team1][LOSE] > 0 and scores[team2][WIN] > 0:
        scores[team1][LOSE] -= 1
        scores[team2][WIN] -= 1
        if backtracking(scores, team1, team2 + 1, time + 1):
            return True
        scores[team1][LOSE] += 1
        scores[team2][WIN] += 1
    return is_valid


def main():
    for _ in range(TESTCASE):
        scores = list()
        input = list(map(int, sys.stdin.readline().strip().split()))
        for idx in range(NUMBER_OF_COUNTRY):
            scores.append(input[3*idx:3*(idx + 1)])
        print(1 if backtracking(scores, 0, 1, 0) else 0)


if __name__ == "__main__":
    main()