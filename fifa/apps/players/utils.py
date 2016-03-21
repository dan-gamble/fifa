def build_querystring(items):
    # Map the possible querystring items to their database lookup
    filter_possibilities = {
        'sm': 'skill_moves__gte',
        'wf': 'weak_foot__gte',
        'awr': 'workrate_att',
        'dwr': 'workrate_def',
        'sf': 'foot',
        'pos': 'position',
        'age': 'age',
        'type': 'player_type',
        'color': 'color'
    }

    built_filters = {}

    for k, v in items:
        if k in filter_possibilities:
            built_filters[filter_possibilities[k]] = v

    return built_filters
