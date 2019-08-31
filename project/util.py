import json

from project.settings.base import BASE_DIR


def get_server_info_value(key: str):
    """서버 정보 취득"""

    with open(BASE_DIR +'/server_info.json', mode='rt', encoding='utf-8') as file:
        data = json.load(file)
        for k, v in data.items():
            if k == key:
                return v
        raise ValueError('서버정보를 확인할 수 없습니다.')
