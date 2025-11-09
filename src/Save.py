import json
import time
from src.Cookie import Cookie
from src.Buildings import Buildings
from src.Bonus import Bonus

class Save:
    def __init__(self):
        pass

    def save(self, cookie: Cookie, buildings: list[Buildings], bonuses: list[Bonus]):
        data = {
            'timestamp': int(time.time()),
            'cookie': {
                'score': cookie.score,
                'cookies_per_second': cookie.cookies_per_second,
                'cookies_per_click': cookie.cookies_per_click,
                'multiplicator': cookie.multiplicator
            },
            'buildings': [vars(building) for building in buildings],
            'bonuses': [vars(bonus) for bonus in bonuses]
        }

        with open('save.json', 'w') as f:
            json.dump(data, f, indent=4)