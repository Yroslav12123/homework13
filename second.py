def unique_items(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))

items = ('table table')
result = unique_items(items)
print(result)