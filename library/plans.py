def get_plans(user_id, day = None):
    if day is None:
        day = get_to_day()