import json
import os
from typing import Any
from datetime import datetime

REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)


def print_dict_pretty(data: Any, indent: int = 0, max_list_items: int = 5) -> None:
    """Красиво выводит любой JSON-ответ в формате ключ: значение"""
    prefix = "  " * indent

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)) and value:
                print(f"{prefix}{key}:")
                print_dict_pretty(value, indent + 1, max_list_items)
            else:
                display_value = value
                if isinstance(value, str) and len(value) > 200:
                    display_value = value[:197] + "..."
                print(f"{prefix}{key}: {display_value}")

    elif isinstance(data, list):
        print(f"{prefix}Список из {len(data)} элементов:")
        for i, item in enumerate(data[:max_list_items]):
            if isinstance(item, (dict, list)):
                print(f"{prefix}  [{i+1}] ->")  # ← Заменил → на ->
                print_dict_pretty(item, indent + 2, max_list_items)
            else:
                print(f"{prefix}  [{i+1}]: {item}")
        if len(data) > max_list_items:
            print(f"{prefix}  ... и ещё {len(data) - max_list_items} элементов")

    else:
        print(f"{prefix}{data}")


def save_response_to_json(
    data: Any,
    filename: str = "api_response.json",
    subdirectory: str | None = None,
    overwrite: bool = True,
    attach_to_allure: bool = True  # ← Новый параметр
) -> str:
    save_dir = REPORTS_DIR
    if subdirectory:
        save_dir = os.path.join(REPORTS_DIR, subdirectory)
        os.makedirs(save_dir, exist_ok=True)

    if not overwrite:
        name, ext = os.path.splitext(filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}{ext}"

    full_path = os.path.join(save_dir, filename)

    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    action = "Перезаписан" if overwrite and os.path.exists(full_path) else "Сохранён"
    print(f"{action} файл: {full_path}")

    # === Автоматически прикрепляем к Allure, если запущен ===
    if attach_to_allure:
        try:
            import allure
            allure.attach.file(
                full_path,
                name=filename,
                attachment_type=allure.attachment_type.JSON
            )
        except ImportError:
            pass  # Allure не установлен — просто пропускаем
        except Exception as e:
            print(f"Не удалось прикрепить к Allure: {e}")

    return full_path