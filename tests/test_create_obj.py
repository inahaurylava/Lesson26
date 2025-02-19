from endpoints.create_obj import CreateObj
from payload.payload import valid_create_payload
import pytest


def test_create_obj():
    new_obj = CreateObj()
    new_obj.new_obj(valid_create_payload)
    new_obj.check_response_is_200()
    new_obj.validate(new_obj.get_data())
    #print(new_obj.get_data())
    new_obj.check_all_fields(valid_create_payload)

    # assert new_obj.get_year() == 2019
    # assert new_obj.get_price() == 1849.99
    # assert new_obj.get_cpu() == 'Intel Core i9'
    # assert new_obj.get_disk_size() == '1 TB', f"{new_obj} Неверно! Сервер вернул {new_obj.get_disk_size()}"




