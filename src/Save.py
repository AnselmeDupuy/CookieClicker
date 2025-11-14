import json
import time
from src.Cookie import Cookie
from src.Buildings import Buildings
from src.Bonus import Bonus

class Save:
    def __init__(self):
        pass

    def save(self, cookie: Cookie, buildings: list[Buildings], bonuses: list[Bonus] = []):
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

        
    def load(self, cookie: Cookie, buildings: list[Buildings], bonuses: list[Bonus] = []):
        try:
            with open('save.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print("No save file found ('save.json').")
            return False
        except json.JSONDecodeError:
            print("Save file is invalid (could not decode JSON).")
            return False

        cookie_data = data.get('cookie', {})
        if cookie_data:
            if 'score' in cookie_data:
                setattr(cookie, 'score', cookie_data.get('score', getattr(cookie, 'score', 0)))
            if 'cookies_per_second' in cookie_data:
                setattr(cookie, 'cookies_per_second', cookie_data.get('cookies_per_second', getattr(cookie, 'cookies_per_second', 0)))
            if 'cookies_per_click' in cookie_data:
                setattr(cookie, 'cookies_per_click', cookie_data.get('cookies_per_click', 0))
            if 'multiplicator' in cookie_data:
                setattr(cookie, 'multiplicator', cookie_data.get('multiplicator', getattr(cookie, 'multiplicator', 1)))

        saved_buildings = data.get('buildings', [])
        if saved_buildings:
            for idx, sb in enumerate(saved_buildings):
                target = None
                sb_name = sb.get('name')
                if sb_name:
                    for b in buildings:
                        if getattr(b, 'name', None) == sb_name:
                            target = b
                            break
                        get_name = getattr(b, 'get_name', None)
                        try:
                            if callable(get_name) and get_name() == sb_name:
                                target = b
                                break
                        except Exception:
                            pass

                if target is None and idx < len(buildings):
                    target = buildings[idx]

                if target is None:
                    continue

                for key, value in sb.items():
                    if hasattr(target, key) and not callable(getattr(target, key)):
                        try:
                            setattr(target, key, value)
                        except Exception:
                            pass

        saved_bonuses = data.get('bonuses', [])
        if saved_bonuses and bonuses is not None:
            for idx, sb in enumerate(saved_bonuses):
                target = None
                sb_name = sb.get('name')
                if sb_name:
                    for b in bonuses:
                        if getattr(b, 'name', None) == sb_name:
                            target = b
                            break

                if target is None and idx < len(bonuses):
                    target = bonuses[idx]

                if target is None:
                    continue

                for key, value in sb.items():
                    if hasattr(target, key) and not callable(getattr(target, key)):
                        try:
                            setattr(target, key, value)
                        except Exception:
                            pass

        return True
