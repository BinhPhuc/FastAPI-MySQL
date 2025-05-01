from .hero_controller import router as hero_router
from .team_controller import router as team_router

all_routers = [
    hero_router,
    team_router
]