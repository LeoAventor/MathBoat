from user_data import USER_DATA
import json


class USER_ENCODER(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, USER_DATA):
            return {"username": o.username,
                    "password": o.password,
                    "user_win_count": o.user_win_count,
                    "user_lose_count": o.user_lose_count,
                    "user_current_attempts": o.user_current_attempts,
                    "user_current_streak": o.user_current_streak,
                    "user_current_difficulty": o.user_current_difficulty}
        return super().default(o)
