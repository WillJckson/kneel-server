import sqlite3
from models import Order
from models import Size
from models import Style
from models import Metal

def get_all_orders():

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Write the SQL query to get the information you want
        db_cursor.execute("""
            SELECT
                o.id,
                o.size_id,
                o.style_id,
                o.metal_id,
                m.metal AS metal_metal,
                m.price AS metal_price,
                st.style AS style_style,
                st.price AS style_price,
                si.carats AS size_carats,
                si.price AS size_price
            FROM Orders o
            JOIN Metals m 
                ON  m.id = o.metal_id
            JOIN Styles st 
                ON st.id = o.style_id
            JOIN Size si 
                ON si.id = o.size_id
        """)

        orders = []

        dataset = db_cursor.fetchall()
        for row in dataset:

            order = Order(row['id'], row['metal_id'], row['size_id'], row['style_id'])
            metal = Metal(row['id'], row['metal_metal'], row['metal_price'])
            style = Style(row['id'], row['style_style'], row['style_price'])
            size = Size(row['id'], row['size_carats'], row['size_price'])
            
            # Add the dictionary representation of the order to the list
            order.metal = metal.__dict__
            order.style = style.__dict__
            order.size = size.__dict__
            
            orders.append(order.__dict__)

    return orders


def create_order(new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            ( metal_id, size_id, style_id )
        VALUES
            ( ?, ?, ?);
        """, (new_order['metal_id'], new_order['size_id'], new_order['style_id'] ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_order['id'] = id

    return new_order


def delete_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            DELETE FROM Orders
            WHERE id = ?
            """, (id, ))


def update_order(order_id, new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Orders
        SET
            metal_id = ?,
            size_id = ?,
            style_id = ?
        WHERE id = ?
        """, (new_order['metal_id'], new_order['size_id'], new_order['style_id'], order_id))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def get_single_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM Orders o
        WHERE o.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an order instance from the current row
        order = Order(data['id'], data['metal_id'],
                    data['size_id'], data['style_id'])

    return order.__dict__
