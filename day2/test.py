from main import is_game_possible, solve
from parse_input import parse_input_file


TEST_BOUNDARIES = {
    "red": 12,
    "green": 13,
    "blue": 14
}
TEST_GAMES_SOLUTION = {
    1: True,
    2: True,
    3: False,
    4: False,
    5: True
}
TEST_SOLUTION = 8


def test_is_game_possible():
    games = parse_input_file("day2/test_input.txt")
    print(games)
    try:
        for id, game_extractions_list in games.items():
            actual = is_game_possible(game_extractions_list, TEST_BOUNDARIES)
            expected = TEST_GAMES_SOLUTION[id]
            print(f"{actual=} == {expected=}")
            assert actual == expected
        print("TEST PASSED")
    except:
        print("TEST FAILED")


def test_solve():
    games = parse_input_file("day2/test_input.txt")
    actual_solution = solve(games, boundaries=TEST_BOUNDARIES)
    expected_solution = TEST_SOLUTION
    try:
        assert actual_solution == expected_solution
        print("TEST_PASSED")
    except:
        print("TEST_FAILED")


def run_tests():
    test_is_game_possible()
    test_solve()


if __name__ == '__main__':
    run_tests()
