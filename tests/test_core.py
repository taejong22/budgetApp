"""Tests for budget.core."""

from budget.core import add_transaction, get_balance


def test_add_transaction_increases_length() -> None:
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        }
    ]
    transaction = {
        "date": "2026-01-07",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3500000,
        "memo": "1월급여",
    }

    result = add_transaction(transactions, transaction)

    assert len(result) == len(transactions) + 1


def test_add_transaction_preserves_negative_amount() -> None:
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        }
    ]
    transaction = {
        "date": "2026-01-10",
        "type": "지출",
        "category": "교통",
        "description": "지하철",
        "amount": -1500,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["amount"] == -1500


def test_add_transaction_preserves_positive_amount() -> None:
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        }
    ]
    transaction = {
        "date": "2026-01-07",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3500000,
        "memo": "1월급여",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["amount"] == 3500000


def test_add_transaction_handles_empty_description() -> None:
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        }
    ]
    transaction = {
        "date": "2026-01-12",
        "type": "지출",
        "category": "식비",
        "description": "",
        "amount": -5800,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["description"] == ""


def test_get_balance_returns_zero_for_empty_list() -> None:
    assert get_balance([]) == 0.0


def test_get_balance_matches_step2_transactions_csv() -> None:
    transactions = [
        {
            "date": "2026-01-04",
            "type": "지출",
            "category": "여행",
            "description": "항공권",
            "amount": -979796,
            "memo": "메모_3",
        },
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "의료",
            "description": "한의원",
            "amount": -65990,
            "memo": "카드결제",
        },
        {
            "date": "2026-01-15",
            "type": "수입",
            "category": "기타수입",
            "description": "중고 판매",
            "amount": 135541,
            "memo": "",
        },
        {
            "date": "2026-02-01",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 4358625,
            "memo": "",
        },
        {
            "date": "2026-02-03",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 4629371,
            "memo": "현금",
        },
        {
            "date": "2026-02-24",
            "type": "수입",
            "category": "기타수입",
            "description": "중고 판매",
            "amount": 199790,
            "memo": "",
        },
        {
            "date": "2026-03-25",
            "type": "수입",
            "category": "급여",
            "description": "보너스",
            "amount": 2891172,
            "memo": "",
        },
    ]

    assert get_balance(transactions) == 11168713.0
