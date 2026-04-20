from life_demo.life import GameOfLife


def test_block_stays_stable():
    game = GameOfLife(4, 4)
    game.set_pattern([(1, 1), (1, 2), (2, 1), (2, 2)])

    before = game.as_text()
    game.step()
    after = game.as_text()

    assert before == after
