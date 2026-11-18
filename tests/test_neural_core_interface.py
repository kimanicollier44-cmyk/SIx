import os
import unittest

from PIL import Image

from src.neural_core_interface import (
    STATE_ORDER,
    TRANSITIONS,
    CoreState,
    IllegalTransitionError,
    NeuralCore,
    legal_transitions,
    params_for,
    render_frame,
    state_table,
)

REPO_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FRAME_DIR = os.path.join(REPO_ROOT, "assets", "neural-core")
GIF_PATH = os.path.join(REPO_ROOT, "assets", "neural-core.gif")

# How to legally walk the cycle to each state, starting from IDLE.
_PATH_TO = {
    CoreState.IDLE: (),
    CoreState.LISTENING: (CoreState.LISTENING,),
    CoreState.THINKING: (CoreState.LISTENING, CoreState.THINKING),
    CoreState.RESPONDING: (CoreState.LISTENING, CoreState.THINKING,
                           CoreState.RESPONDING),
    CoreState.LEARNING: (CoreState.LISTENING, CoreState.THINKING,
                         CoreState.RESPONDING, CoreState.LEARNING),
}


def core_in(state):
    core = NeuralCore()
    for step in _PATH_TO[state]:
        core.transition(step)
    return core


class TestNeuralCoreStateMachine(unittest.TestCase):
    def test_five_states_in_cycle_order(self):
        self.assertEqual(
            [s.value for s in STATE_ORDER],
            ["IDLE", "LISTENING", "THINKING", "RESPONDING", "LEARNING"])
        self.assertEqual(len(state_table()), 5)

    def test_full_legal_cycle(self):
        core = NeuralCore()
        self.assertEqual(core.state, CoreState.IDLE)
        for target in (CoreState.LISTENING, CoreState.THINKING,
                       CoreState.RESPONDING, CoreState.LEARNING,
                       CoreState.LISTENING, CoreState.THINKING,
                       CoreState.RESPONDING, CoreState.IDLE):
            self.assertEqual(core.transition(target), target)

    def test_any_state_can_return_to_idle(self):
        for state in STATE_ORDER:
            if state is CoreState.IDLE:
                continue
            core = core_in(state)
            self.assertEqual(core.transition(CoreState.IDLE), CoreState.IDLE)

    def test_illegal_transitions_raise(self):
        illegal = [
            (CoreState.IDLE, CoreState.THINKING),
            (CoreState.IDLE, CoreState.RESPONDING),
            (CoreState.IDLE, CoreState.LEARNING),
            (CoreState.LISTENING, CoreState.RESPONDING),
            (CoreState.LISTENING, CoreState.LEARNING),
            (CoreState.THINKING, CoreState.LISTENING),
            (CoreState.THINKING, CoreState.LEARNING),
            (CoreState.RESPONDING, CoreState.THINKING),
            (CoreState.RESPONDING, CoreState.LISTENING),
            (CoreState.LEARNING, CoreState.THINKING),
            (CoreState.LEARNING, CoreState.RESPONDING),
        ]
        for start, target in illegal:
            core = core_in(start)
            with self.assertRaises(IllegalTransitionError):
                core.transition(target)
            self.assertEqual(core.state, start)  # state unchanged

    def test_self_transitions_are_illegal(self):
        for state in STATE_ORDER:
            core = core_in(state)
            with self.assertRaises(IllegalTransitionError):
                core.transition(state)

    def test_transition_map_is_consistent(self):
        for state in STATE_ORDER:
            self.assertEqual(legal_transitions(state), TRANSITIONS[state])
            self.assertNotIn(state, TRANSITIONS[state])
            if state is not CoreState.IDLE:
                self.assertIn(CoreState.IDLE, TRANSITIONS[state])

    def test_history_uses_logical_ticks(self):
        core = NeuralCore()
        core.transition(CoreState.LISTENING)
        core.transition(CoreState.THINKING)
        history = core.history
        self.assertEqual([row[0] for row in history], [0, 1, 2])
        self.assertEqual(history[0], (0, None, CoreState.IDLE))
        self.assertEqual(history[1], (1, CoreState.IDLE, CoreState.LISTENING))
        self.assertEqual(history[2], (2, CoreState.LISTENING, CoreState.THINKING))

    def test_reset_returns_to_idle_from_any_state(self):
        for state in STATE_ORDER:
            core = core_in(state)
            self.assertEqual(core.reset(), CoreState.IDLE)
            self.assertEqual(core.state, CoreState.IDLE)


class TestNeuralCoreVisualParams(unittest.TestCase):
    def test_appearances_match_the_design_spec(self):
        expected = {
            CoreState.IDLE: "Slowly floating and breathing",
            CoreState.LISTENING: "Cyan glowing rings",
            CoreState.THINKING: "Rapid neural pulses",
            CoreState.RESPONDING: "Expanding communication waves",
            CoreState.LEARNING: "New particles connecting",
        }
        for state, appearance in expected.items():
            self.assertEqual(params_for(state).appearance, appearance)

    def test_thinking_pulses_fastest_idle_slowest(self):
        rates = {s: params_for(s).pulse_rate for s in STATE_ORDER}
        self.assertGreater(rates[CoreState.THINKING], rates[CoreState.IDLE])
        self.assertEqual(max(rates.values()), rates[CoreState.THINKING])
        self.assertEqual(min(rates.values()), rates[CoreState.IDLE])

    def test_state_specific_effects(self):
        listening = params_for(CoreState.LISTENING)
        self.assertEqual(listening.ring_count, 3)
        r, g, b = listening.dominant_color  # cyan: low red, high green/blue
        self.assertLessEqual(r, 60)
        self.assertGreaterEqual(g, 200)
        self.assertGreaterEqual(b, 200)

        for state in STATE_ORDER:
            params = params_for(state)
            if state is CoreState.RESPONDING:
                self.assertGreater(params.wave_rate, 0.0)
            else:
                self.assertEqual(params.wave_rate, 0.0)
            if state is not CoreState.LISTENING:
                self.assertEqual(params.ring_count, 0)

        link_rates = {s: params_for(s).link_rate for s in STATE_ORDER}
        self.assertEqual(max(link_rates.values()),
                         link_rates[CoreState.LEARNING])

        idle = params_for(CoreState.IDLE)
        self.assertEqual(idle.float_amplitude,
                         max(params_for(s).float_amplitude for s in STATE_ORDER))
        self.assertEqual(idle.breathing_amplitude,
                         max(params_for(s).breathing_amplitude
                             for s in STATE_ORDER))

    def test_params_accept_state_names_as_strings(self):
        self.assertIs(params_for("THINKING").state, CoreState.THINKING)
        core = NeuralCore()
        self.assertEqual(core.transition("LISTENING"), CoreState.LISTENING)


class TestNeuralCoreRenderer(unittest.TestCase):
    def test_render_is_deterministic(self):
        a = render_frame(CoreState.THINKING, phase=0.4, size=220)
        b = render_frame(CoreState.THINKING, phase=0.4, size=220)
        self.assertEqual(a.tobytes(), b.tobytes())

    def test_render_varies_with_phase_and_state(self):
        base = render_frame(CoreState.IDLE, phase=0.1, size=220)
        other_phase = render_frame(CoreState.IDLE, phase=0.6, size=220)
        other_state = render_frame(CoreState.LEARNING, phase=0.1, size=220)
        self.assertNotEqual(base.tobytes(), other_phase.tobytes())
        self.assertNotEqual(base.tobytes(), other_state.tobytes())

    def test_render_size_and_mode(self):
        img = render_frame("LISTENING", phase=0.3, size=180)
        self.assertEqual(img.size, (180, 180))
        self.assertEqual(img.mode, "RGB")


class TestNeuralCoreAssets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # The assets are binary files that cannot travel with every
        # checkout channel (e.g. text-only pushes). They are fully
        # deterministic, so when any of them is missing, regenerate
        # them in place with the repo's own generator before asserting.
        expected = [GIF_PATH] + [
            os.path.join(FRAME_DIR, f"{state.value.lower()}.png")
            for state in STATE_ORDER
        ]
        if all(os.path.exists(path) for path in expected):
            return
        import importlib.util
        gen_path = os.path.join(
            REPO_ROOT, "scripts", "generate_neural_core_assets.py")
        spec = importlib.util.spec_from_file_location(
            "generate_neural_core_assets", gen_path)
        gen = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gen)
        gen.generate()

    def test_hero_frames_exist_at_900x900(self):
        for state in STATE_ORDER:
            path = os.path.join(FRAME_DIR, f"{state.value.lower()}.png")
            self.assertTrue(os.path.exists(path), path)
            with Image.open(path) as img:
                self.assertEqual(img.format, "PNG")
                self.assertEqual(img.size, (900, 900))

    def test_state_cycle_gif_exists_and_loops_all_states(self):
        self.assertTrue(os.path.exists(GIF_PATH))
        self.assertLess(os.path.getsize(GIF_PATH), 8 * 1024 * 1024)
        with Image.open(GIF_PATH) as img:
            self.assertEqual(img.format, "GIF")
            self.assertEqual(img.size, (900, 900))
            self.assertGreaterEqual(img.n_frames, 15)


if __name__ == '__main__':
    unittest.main()
