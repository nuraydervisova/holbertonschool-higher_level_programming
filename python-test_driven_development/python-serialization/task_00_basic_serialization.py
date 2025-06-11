import json

def serialize_and_save_to_file(data, filename):
    """Python lüğətini JSON formatında fayla yazır."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Verilənlər '{filename}' faylına yazıldı.")

def load_and_deserialize(filename):
    """JSON faylını oxuyur və Python lüğətinə çevirir."""
    with open(filename, 'r') as f:
        data = json.load(f)
    print(f"'{filename}' faylı oxundu və verilənlər deserializasiya edildi.")
    return data

if __name__ == "__main__":
    # Seriyalaşdırılacaq nümunə verilənlər
    data_to_serialize = {
        "ad": "John Doe",
        "yas": 30,
        "seher": "New York"
    }

    # Verilənləri JSON formatında fayla yazırıq
    serialize_and_save_to_file(data_to_serialize, 'data.json')

    # JSON faylından verilənləri oxuyuruq və deserializasiya edirik
    deserialized_data = load_and_deserialize('data.json')

    # Deserializasiya olunmuş verilənləri çap edirik
    print("Deserializasiya olunmuş verilənlər:")
    print(deserialized_data)
