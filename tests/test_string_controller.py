from app.controllers.string_controller import StringController

def test_get_current_string():
    controller = StringController()
    assert controller.get_current_string() == "dynamic string"

def test_update_string():
    controller = StringController()
    new_string = "test string"
    response = controller.update_string(new_string)
    assert response["new_string"] == new_string
    assert controller.get_current_string() == new_string 