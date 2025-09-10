# lib/db.py
# lib/db.py
import pymysql


def create_customer(connection, customer_data: dict) -> int:
    """
    Создаёт нового клиента в таблице oc_customer.
    Возвращает ID созданного клиента.
    """
    sql = """
    INSERT INTO oc_customer (
        customer_group_id, store_id, language_id, firstname, lastname,
        email, telephone, password, salt, cart, wishlist,
        newsletter, address_id, ip, status, approved,
        token, code, date_added
    ) VALUES (
        %(customer_group_id)s, %(store_id)s, %(language_id)s, %(firstname)s, %(lastname)s,
        %(email)s, %(telephone)s, %(password)s, %(salt)s, %(cart)s, %(wishlist)s,
        %(newsletter)s, %(address_id)s, %(ip)s, %(status)s, %(approved)s,
        %(token)s, %(code)s, %(date_added)s
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, customer_data)
        customer_id = cursor.lastrowid
    connection.commit()
    return customer_id


def get_customer_by_id(connection, customer_id: int):
    """
    Возвращает данные клиента по ID.
    """
    sql = "SELECT * FROM oc_customer WHERE customer_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (customer_id,))
        return cursor.fetchone()


def update_customer(connection, customer_id: int, update_data: dict):
    """
    Обновляет данные клиента.
    Возвращает количество затронутых строк (0 или 1).
    """
    set_clause = ", ".join([f"{key} = %({key})s" for key in update_data.keys()])
    sql = f"UPDATE oc_customer SET {set_clause} WHERE customer_id = %(customer_id)s"
    update_data['customer_id'] = customer_id

    with connection.cursor() as cursor:
        cursor.execute(sql, update_data)
        affected = cursor.rowcount
    connection.commit()
    return affected


def delete_customer(connection, customer_id: int) -> int:
    """
    Удаляет клиента по ID.
    Возвращает количество удалённых строк (0 или 1).
    """
    sql = "DELETE FROM oc_customer WHERE customer_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (customer_id,))
        affected = cursor.rowcount
    connection.commit()
    return affected

