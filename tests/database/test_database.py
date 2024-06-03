import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'
   

@pytest.mark.database
def test_text_data_type_insert():
    db = Database()
    db.insert_product(5, 'молоко', 'натуральне згущене', '10')
    milk_qnt = db.select_product_qnt_by_id(5)

    assert milk_qnt[0][0] == 10
            
     
@pytest.mark.database
def test_check_user_stepan():
    db = Database()
    user = db.get_user_address_by_name('Stepan')

    assert user[0][0] == 'Stepana Bandery str, 2'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '2055'
    assert user[0][3] == 'Ukraine'     
    
    
@pytest.mark.database
def test_real_data_type_insert():
    db = Database()
    db.insert_product(7, 'real_product', 'real data type', 3.14)
    product_qnt = db.select_product_qnt_by_id(7)

    assert product_qnt[0][0] == 3.14  
    
    
@pytest.mark.database
def test_null_data_type_insert():
    db = Database()
    db.insert_product(7, 'null_product', 'null data type', 'NULL')
    qnt = db.select_product_qnt_by_id(7)
    
    assert len(qnt) != 0
    
    
@pytest.mark.database
def test_order_date():
    db = Database()
    order_date = db.get_detailed_orders()
    
    assert len(order_date) != '00:00:00'     
