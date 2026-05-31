from agents.offline_agent import OfflineAgent


def test_offline_agent_returns_normalized_sequence() -> None:
    agent = OfflineAgent()
    sequence = agent.analyze(
        (
            "Сначала система запускается и получает вход. "
            "Потом состояние стабилизируется и удерживается. "
            "Дальше начинается рост и направленный сдвиг. "
            "После этого происходит переключение режима. "
            "Затем несколько потоков объединяются и наслаиваются. "
            "После пика система снижает интенсивность и сглаживается. "
            "В финале всё фокусируется в устойчивый итог."
        ),
        domain="text",
    )

    assert len(sequence.palette) == 7
    assert len(sequence.phase_matches) == 7
    assert sequence.phase_matches[0].synthetic is False
    assert sequence.phase_matches[-1].operator_id == "focus"


def test_offline_agent_marks_missing_phases_as_synthetic() -> None:
    agent = OfflineAgent()
    sequence = agent.analyze("Короткий текст без явной структуры.", domain="text")
    assert any(match.synthetic for match in sequence.phase_matches)


def test_focus_coordinates_are_not_equal_to_init_coordinates() -> None:
    agent = OfflineAgent()
    sequence = agent.analyze(
        "The system starts with an impulse. Then it becomes stable. Next it shifts. After that it switches. Then it merges layers. Next it relaxes. Finally it converges into focus.",
        domain="text",
    )

    init_coords = sequence.palette[0].coordinates
    focus_coords = sequence.palette[-1].coordinates

    differences = [
        abs(getattr(focus_coords, axis) - getattr(init_coords, axis))
        for axis in ("A", "S", "T", "E")
    ]
    assert sum(diff >= 0.05 for diff in differences) >= 2
