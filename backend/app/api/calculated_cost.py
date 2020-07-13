import fastapi_plugins
import aioredis
from typing import Dict
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from schemas import CostRequest as CostRequestSchema
from models import CostRequest as CostRequestModel
from services.calculate_cost import calculate_cost
from api.deps import get_db
from api.auth import fastapi_users

router = APIRouter()


@router.post("/", dependencies=[Depends(fastapi_users.get_current_user)])
async def calculated_cost(
    cost_request: CostRequestSchema,
    cache: aioredis.Redis = Depends(fastapi_plugins.depends_redis),
    db: Session = Depends(get_db),
) -> Dict:

    rate = await cache.hget(str(cost_request.date), cost_request.cargo_type)
    calculated_res = calculate_cost(cost_request=cost_request, rate=rate)
    calculated_value = calculated_res.get("calculated_cost")

    if calculated_value:
        db_obj = CostRequestModel(
            **cost_request.dict(),
            calculated_value=calculated_value
        )
    else:
        db_obj = CostRequestModel(**cost_request.dict(), succeed=False)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return calculated_res
