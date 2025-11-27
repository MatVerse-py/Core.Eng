"""Maintain global cognitive state coherence."""
global_state = {"entropy": 0, "coherence": 1.0}


def sync_states():
    global_state["entropy"] *= 0.99
    global_state["coherence"] = 1 - global_state["entropy"]
