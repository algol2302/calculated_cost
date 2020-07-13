from decimal import Decimal
from typing import Dict

from schemas import CostRequest


def calculate_cost(cost_request: CostRequest, rate: str) -> Dict:
    """The method of the final cost calculation

    :param cost_request: CostRequest
    :param rate: str
    :return: response dict. When error case it contains an error text.
    """

    try:
        return {
            "calculated_cost": round(
                Decimal(float(rate) * float(cost_request.declared_value)),
                2
            )
        }
    except TypeError:
        return {
            "error": (
                "Check your request data. It isn't comparable with "
                "`tarif.json`"
            )
        }
