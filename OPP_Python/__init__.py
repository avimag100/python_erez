"""
חבילה לניהול מערכת תחבורה חכמה.
מודול זה כולל את כל המחלקות והאלגוריתמים הדרושים לניהול רכבים, חישוב מסלולים אופטימליים, ומיון רכבים.
המערכת כוללת את המחלקות:
- Vehicle, Bus, Train, Tram
- Route
- Dijkstra, A* (אלגוריתמים למסלולים)
- QuickSortStrategy, MergeSortStrategy (אסטרטגיות מיון)
- RoutePlanner (תכנון מסלולים)

החבילה תומכת בשימוש בממשק שורת פקודה (CLI) לניהול הרכבים והמסלולים.
"""

from .vehicle import Vehicle, Bus, Train, Tram
from .route import Route
from .algorithm import dijkstra, a_star
from .sort_strategy import QuickSortStrategy, MergeSortStrategy
from .route_planner import RoutePlanner

__all__ = ["Vehicle", "Bus", "Train", "Tram", "Route", "dijkstra", "a_star", "QuickSortStrategy", "MergeSortStrategy", "RoutePlanner"]
