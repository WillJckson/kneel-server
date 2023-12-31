SIZES = [
    {
        "id": 1,
        "carats": 0.5,
        "price": 405
    },
    {
        "id": 2,
        "carats": 0.75,
        "price": 782
    },
    {
        "id": 3,
        "carats": 1,
        "price": 1470
    },
    {
        "id": 4,
        "carats": 1.5,
        "price": 1997
    },
    {
        "id": 5,
        "carats": 2,
        "price": 3638
    }
]

def get_all_sizes():
    return SIZES

def create_size(size):
    max_id = SIZES[-1]["id"]
    
    new_id = max_id + 1
    
    size["id"] = new_id
    
    SIZES.append(size)
    
    return size

def delete_size(id):
    # Initial -1 value for size index, in case one isn't found
    size_index = -1

    # Iterate the SIZES list, but use enumerate() so that you
    # can access the index value of each item
    for index, size in enumerate(SIZES):
        if size["id"] == id:
            # Found the size. Store the current index.
            size_index = index

    # If the size was found, use pop(int) to remove it from list
    if size_index >= 0:
        SIZES.pop(size_index)
# Function with a single parameter
def update_size(id, new_size):
    # Iterate the SIZES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, size in enumerate(SIZES):
        if size["id"] == id:
            # Found the size. Update the value.
            SIZES[index] = new_size
            break

def get_single_size(id):
    # Variable to hold the found size, if it exists
    requested_size = None

    # Iterate the SIZES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for size in SIZES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if size["id"] == id:
            requested_size = size

    return requested_size