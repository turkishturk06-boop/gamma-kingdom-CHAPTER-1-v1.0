import builtins
from core import ekran_temizle

def get_text(key, *args):
    """Dil dosyasından metni al"""
    try:
        text_dict = getattr(builtins, 'text', {})
        text = text_dict.get(key, key)
        if args:
            return text.format(*args)
        return text
    except Exception:
        return key

def library():
    while True:
        ekran_temizle()
        menu = f"""
{get_text("library_welcome")}

    {get_text("library_book_1")}
    {get_text("library_book_2")}
    {get_text("library_book_3")}
    {get_text("library_book_4")}
    {get_text("library_book_5")}
    {get_text("library_book_6")}
    {get_text("library_book_7")}
    {get_text("library_book_8")}
    {get_text("library_book_9")}
    {get_text("library_book_10")}
    {get_text("library_book_11")}
    {get_text("library_book_12")}
    {get_text("library_book_13")}
    {get_text("library_exit")}

{get_text("library_choice")}"""
        
        khninput = input(menu).strip()
        
        if khninput == "1":
            ekran_temizle()
            ksinput = input(get_text("library_book_1_content"))
            if ksinput == "":
                ekran_temizle()
                continue
                
        elif khninput == "14":
            ekran_temizle()
            print(get_text("library_exit_msg"))
            break
            
        else:
            ekran_temizle()
            print(get_text("library_book_locked"))
            input("\n[ENTER] " + get_text("library_choice").replace(":", ""))
            continue
