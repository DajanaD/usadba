from docx import Document
import re

def read_docx(file_path):
    """Зчитує текст із .docx файлу та повертає список абзаців."""
    doc = Document(file_path)
    return [para.text.strip() for para in doc.paragraphs if para.text.strip()]

def parse_text(paragraphs):
    """Розбирає текст на структуру сорту яблуні."""
    results = []
    current_sort = {}
    
    for para in paragraphs:
        # Якщо це назва сорту (вона перша і зазвичай без двокрапки)
        if not re.search(r'\b(Підщепа|Період споживання|Дерево|Цвітіння|Кращі запилювачі|Плоди|М\'якуш|Дегустаційна оцінка|Стійкість до хвороб|Зимостійкість|Основне призначення)\b', para):
            if current_sort:
                results.append(current_sort)  # Зберігаємо попередній сорт
            current_sort = {"Назва": para}
        else:
            match = re.match(r'([^—]+)—\s*(.*)', para)
            if match:
                key, value = match.groups()
                current_sort[key.strip()] = value.strip()
    
    if current_sort:
        results.append(current_sort)  # Додаємо останній сорт
    
    return results

def generate_html(sorts):
    """Генерує HTML для кожного сорту яблуні."""
    html_output = ""
    for sort in sorts:
        html_output += f'\n<p style="text-align: justify;"><strong>Яблуня «{sort.get("Назва", "Невідомий сорт") }» &mdash; </strong>'
        html_output += f'{sort.get("Опис", "Опис відсутній")}.</p>'
        
        for key, value in sort.items():
            if key != "Назва" and value:
                html_output += f'\n<p style="text-align: justify;"><strong>{key} </strong>&mdash; {value}</p>'
    return html_output

def main():
    file_path = "Сорта яблони.docx"  # Замінити на свій файл
    paragraphs = read_docx(file_path)
    sorts = parse_text(paragraphs)
    html_result = generate_html(sorts)
    
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html_result)
    
    print("HTML файл успішно створено!")

if __name__ == "__main__":
    main()
