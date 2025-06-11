from custom_object import CustomObject
from task_01_pickle import serialize_and_save_to_file, load_and_deserialize

if __name__ == "__main__":
    obj = CustomObject(name="John", age=25, is_student=True)
    obj.display()
    serialize_and_save_to_file(obj, "object.pkl")
    new_obj = load_and_deserialize("object.pkl")
    if new_obj:
        new_obj.display()
