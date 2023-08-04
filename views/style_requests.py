STYLES = [
    {
        "id": 1,
        "style": "Classic",
        "price": 500
    },
    {
        "id": 2,
        "style": "Modern",
        "price": 710
    },
    {
        "id": 3,
        "style": "Vintage",
        "price": 965
    }
]

def get_all_styles():
    return STYLES

def create_style(style):
    max_id = STYLES[-1]["id"]
    
    new_id = max_id + 1
    
    style["id"] = new_id
    
    STYLES.append(style)
    
    return style

def delete_style(id):
    # Initial -1 value for style index, in case one isn't found
    style_index = -1

    # Iterate the STYLES list, but use enumerate() so that you
    # can access the index value of each item
    for index, style in enumerate(STYLES):
        if style["id"] == id:
            # Found the style. Store the current index.
            style_index = index

    # If the style was found, use pop(int) to remove it from list
    if style_index >= 0:
        STYLES.pop(style_index)
# Function with a single parameter
def update_style(id, new_style):
    # Iterate the STYLES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, style in enumerate(STYLES):
        if style["id"] == id:
            # Found the style. Update the value.
            STYLES[index] = new_style
            break

def get_single_style(id):
    # Variable to hold the found style, if it exists
    requested_style = None

    # Iterate the STYLES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for style in STYLES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if style["id"] == id:
            requested_style = style

    return requested_style