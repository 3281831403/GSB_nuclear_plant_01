import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_load(self):
        state = core.new_game()
        self.assertTrue(core.load_fuel(state, 1))
        self.assertFalse(core.load_fuel(state, 1))

    def test_02_core_capacity(self):
        state = core.new_game()
        state["core_load"] = 2
        result = core.load_fuel(state, 1)
        self.assertFalse(result)

    def test_03_temp_boundary(self):
        state = core.new_game()
        self.assertEqual(core.check_temp(state, 35), "over")

    def test_04_cancel_releases_core(self):
        state = core.new_game()
        core.load_fuel(state, 1)
        core.cancel(state, 1)
        self.assertEqual(state["core_load"], 0)

    def test_05_no_produce_on_fault(self):
        state = core.new_game()
        state["cooling_fault"] = True
        result = core.produce(state, 5)
        self.assertFalse(result)

    def test_06_leak_once(self):
        state = core.new_game()
        core.leak(state)
        self.assertEqual(state["safety"], 90)

    def test_07_no_generate_without_pressure(self):
        state = core.new_game()
        state["pressure"] = 0
        result = core.generate(state, 5)
        self.assertFalse(result)

    def test_08_load_preserves_batch(self):
        state = core.new_game()
        state["batch_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["batch_id"], 4)


if __name__ == "__main__":
    unittest.main()
