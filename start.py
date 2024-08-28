import multiprocessing
import os
import json
import time
import importlib.util
process=[]
name_process=[]
def run_script(script_path,shared_dict):
    try:
    spec = importlib.util.spec_from_file_location("module.name", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.start(shared_dict)
    except Exception as e:
        print(e)
def run(setting_file_path,pool_folder_path,shared_dict):
    global process,name_process
    with open(setting_file_path, 'r+') as file:
        data = json.load(file)
        for e,name in data["block"]:
            if name not in name_process:
                if name in data["block"]:
                    data["block"].remove(name)
        for e,name in enumerate(name_process):
            if name not in data["ready"]:
                process[e].terminate()
                if name in data["block"]:
                    data["block"].remove(name)
        if len(data["ready"])!=0:
            for r in data["ready"]:
                if r not in data['block']:
                    if r in name_process:
                        ridx=name_process.index(r)
                        process[ridx].terminate()
                    data['block'].append(r)
                    script_path = os.path.join(pool_folder_path, r)
                    p = multiprocessing.Process(target=run_script, args=(script_path,shared_dict,))
                    p.start()
                    process.append(p)
                    name_process.append(r)
        file.seek(0)
        json.dump(data, file,indent=1)
        file.truncate()
    time.sleep(shared_dict["run_rate"])
def rewrite(file_path,shared_dict):
    while True:
        time.sleep(shared_dict["rewrite_rate"])
        with open(file_path, 'w') as file:
            json.dump(dict(shared_dict), file)
if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    shared_dict_file_path = os.path.join(current_directory, "shared_dict.json")
    setting_file_path = os.path.join(current_directory, "pool\\engine\\setting.json")
    pool_folder_path = os.path.join(current_directory, "pool")
    with open(shared_dict_file_path, 'r') as file:
        data = json.load(file)
    shared_dict = multiprocessing.Manager().dict(data)
    p = multiprocessing.Process(target=rewrite, args=(shared_dict_file_path,shared_dict,))
    p.start()
    process.append(p)
    name_process.append('rewrite')
    while True:
        run(setting_file_path,pool_folder_path,shared_dict)
    
    
