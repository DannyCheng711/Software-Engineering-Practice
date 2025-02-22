from app import process_query


def test_knows_about_dinosaurs():
    # if condition returns True, then nothing happens
    # if condition returns False, AssertionError is raised
    assert (
        process_query("dinosaurs")
        == "Dinosaurs ruled the Earth 200 million years ago"
    )


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_my_name():
    assert process_query("What is your name?") == "Computing genius"


def test_plus():
    assert process_query("What is 67 plus 86?") == "153"


def test_3plus():
    assert process_query("What is 12 plus 62 plus 27?") == "101"


def test_largest():
    assert (
        process_query(
            "Which of the following numbers is the largest: 96, 93, 37?"
        )
        == "96"
    )


def test_power():
    assert (
        process_query("What is 88 to the power of 25?")
        == "4093236175904463085683654411954642528654818541568"
    )


def test_multiplied():
    assert process_query("What is 26 multiplied by 72?") == "1872"


def test_square_cube():
    assert (
        process_query(
            "both a square and a cube: 3329, 64, 1, 65, 1972, 1000, 2712, 80??"
        )
        == "1, 64"
    )


def test_prime():
    assert (
        process_query(
            "Which of the following numbers are primes: 31, 65, 2, 27, 88?"
        )
        == "2, 31"
    )


def test_minus():
    assert process_query("What is 66 minus 5?") == "61"
