import processing

def test_results():
    assert processing.run_processes(['realmadrid', 'Nationals', 'Cristiano', 'BU_Tweets']) == 0


if __name__ == "__main__":
    test_results()