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
