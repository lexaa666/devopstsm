import subprocess
import json
import os
import re
regular = '(HEAD -> \w+)'
save_container = '/home/ubuntu/TSM/nginx'
path_dockerfile = '/home/ubuntu/TSM/33lesson'
file_path = "/home/ubuntu/TSM/json_for_build.json"
_json = {}
app = 'nginx'
branch_names = ['deploy','prod']
def check_json_file():
    if os.path.exists(file_path) == True:
        print('Файл есть')
    else:
        json_object = json.dumps(_json, indent=4)
        with open(file_path, "w") as outfile:
            outfile.write(json_object)

def last_commit_create_dict(name_branch,last_commit):   
    _json[name_branch] = last_commit

def build_docker_container(name_branch,last_commit):
    os.system(f'docker build -t {app}:{name_branch}_{last_commit} -f {path_dockerfile}/Dockerfile {path_dockerfile}')

def save_continer(name_branch,last_commit):
    os.system(f'docker save --output {save_container}/{app}-{name_branch}_{last_commit}.tar {app}:{name_branch}_{last_commit}')


def log_commit_branch_last(branch):
    subprocess.check_output(['git', 'switch' , f'{branch}']).strip().decode("utf-8")
    last_commit= subprocess.check_output(['git', 'log', f'{branch}','-1', '--format=%ad.%h', '--date=format:%Y%m%d-%H%M']).strip().decode("utf-8")
    name_branch= subprocess.check_output(['git', 'log', f'{branch}','-1', '--format=%d']).strip().decode("utf-8").split(' ')[2].split(')')[0]
    return name_branch, last_commit

for branch in branch_names:
    lcb = log_commit_branch_last(branch)
    name_branch = lcb[0]
    last_commit = lcb[1]
    last_commit_create_dict(name_branch,last_commit)
check_json_file()
print(_json)

with open(file_path, 'r')as openfile:
    json_object = json.load(openfile)
    if json_object[branch_names[0]] == _json[branch_names[0]]:
        print(f'Ветка {branch_names[0]} без изменений')
    else:
        lcb = log_commit_branch_last(branch_names[0])
        name_branch = lcb[0]
        last_commit = lcb[1]
        build_docker_container(name_branch,last_commit)
        save_continer(name_branch,last_commit)
        last_commit_create_dict(name_branch,last_commit)
        json_object = json.dumps(_json, indent=4)
        with open(file_path, "w") as outfile:
            outfile.write(json_object)
        print(f'Файл {file_path} был измене т.к. были новые коммиты в ветке {name_branch}')
    if json_object[branch_names[1]] == _json[branch_names[1]]:
        print(f'Ветка {branch_names[1]} без изменений')
    else:
        lcb = log_commit_branch_last(branch_names[1])
        name_branch = lcb[0]
        last_commit = lcb[1]
        build_docker_container(name_branch,last_commit)
        save_continer(name_branch,last_commit)
        last_commit_create_dict(name_branch,last_commit)
        json_object = json.dumps(_json, indent=4)
        with open(file_path, "w") as outfile:
            outfile.write(json_object)
        print(f'Файл {file_path} был измене т.к. были новые коммиты в ветке {name_branch}')