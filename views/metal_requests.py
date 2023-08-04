import sqlite3

METALS = [
    {
        "id": 1,
        "metal": "Sterling Silver",
        "price": 12.42
    },
    {
        "id": 2,
        "metal": "14K Gold",
        "price": 736.4
    },
    {
        "id": 3,
        "metal": "24K Gold",
        "price": 1258.9
    },
    {
        "id": 4,
        "metal": "Platinum",
        "price": 795.45
    },
    {
        "id": 5,
        "metal": "Palladium",
        "price": 1241
    }
]

def get_all_metals():
    return METALS

def create_metal(metal):
    max_id = METALS[-1]["id"]
    
    new_id = max_id + 1
    
    metal["id"] = new_id
    
    METALS.append(metal)
    
    return metal

def delete_metal(id):
    # Initial -1 value for metal index, in case one isn't found
    metal_index = -1

    # Iterate the metalS list, but use enumerate() so that you
    # can access the index value of each item
    for index, metal in enumerate(METALS):
        if metal["id"] == id:
            # Found the metal. Store the current index.
            metal_index = index

    # If the metal was found, use pop(int) to remove it from list
    if metal_index >= 0:
        METALS.pop(metal_index)
# Function with a single parameter
def update_metal(id,new_metal):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Metals
        SET
            metal = ?,
            price = ?
        WHERE id = ?
        """, (new_metal['metal'], new_metal['price'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


def get_single_metal(id):
    # Variable to hold the found metal, if it exists
    requested_metal = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for metal in METALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if metal["id"] == id:
            requested_metal = metal

    return requested_metal