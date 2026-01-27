from boss import kral1

def chapter_kontrolü():
    try:
        return bool(kral1.bitirme_durumu)
    except Exception:
        return False
