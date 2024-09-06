from project import submit_score, detect_collision


def main():
    test_submit()


def test_submit():
    assert submit_score("10","Harry") == "Harry,10"
    assert submit_score("150","JACK") == "JACK,150"


def test_collision():
    assert detect_collision(480,100,483,95) == True
    assert detect_collision(480,190,500,95) == False


if __name__ == "__main__":
    main()