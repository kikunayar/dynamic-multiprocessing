

def update(new_entry,key):
    import json
    import os
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "setting.json")
    with open(file_path, 'r+') as file:
        data = json.load(file)
        if key=='upload':
            if new_entry in data['block']:
                data['block'].remove(new_entry)
            if new_entry not in data['ready']:
                data['ready'].append(new_entry)
        if key=='delete':
            data['block'].remove(new_entry)
            data['ready'].remove(new_entry)
        file.seek(0)  # ย้ายตำแหน่งการเขียนไปที่ต้นไฟล์
        json.dump(data, file,indent=1)  # เขียนข้อมูล JSON ใหม่
        file.truncate()  # ลบข้อมูลที่เหลือจากการแก้ไข