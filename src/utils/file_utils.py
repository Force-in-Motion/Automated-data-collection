
from pathlib import Path
import json

class FileUtils:
    
    
    @staticmethod
    def get_token_path():
        return Path('src/telegram/settings/token.json').resolve()
    
    
    @staticmethod
    def get_token() -> str:
        """
        Получает токен по указанному пути
        :return: Токен в виде строки
        """
        with open(FileUtils.get_token_path(), 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['TOKEN']