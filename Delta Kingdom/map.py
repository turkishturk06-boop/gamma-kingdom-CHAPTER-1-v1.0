from core import ekran_temizle, chapter_kontrolü, savas, boss_savas
from library import library
from saving import save_game, load_game, quit_game
from characters import oyuncu_instance as oyuncu
import core
import random as r
import time as t
import builtins

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

alan_deltası = 100

def map():
    ekran_temizle()
    while True:
        menu = f"""    {get_text('map_title')}
                    {get_text('map_1')}
                    {get_text('map_2')}
                    {get_text('map_3')}
                    {get_text('map_4')}
                    {get_text('map_5')}
                    {get_text('map_6')}
                    {get_text('map_7')}
                    {get_text('map_8')}
                    {get_text('map_9')}
                    {get_text('map_10')}
                    {get_text('map_11')}
{get_text('map_choice')}"""
        hinput = input(menu).strip()
        
        # 1) KRALLIĞA GİT
        if hinput == "1":
            kingdom_menu()
        
        # 2) MAĞAZA
        elif hinput == "2":
            shop_menu()
        
        # 3) KAYDET/YÜKLE
        elif hinput == "3":
            save_load_menu()
        
        # 4) GÖREV
        elif hinput == "4":
            quest_menu()
        
        # 5) AKTİVİTE
        elif hinput == "5":
            activity_menu()
        
        # 6) ARENA
        elif hinput == "6":
            print(get_text("arena_title"))
            print(get_text("arena_info"))
            print(get_text("arena_start"))
            savas()
        
        # 7) DELTA MARKETİ
        elif hinput == "7":
            delta_market_menu()
        
        # 8) KÜTÜPHANE
        elif hinput == "8":
            library()
        
        # 9) UZAY LABORATUVARI
        elif hinput == "9":
            laboratory_menu()
        
        # 10) HELİPAD
        elif hinput == "10":
            if chapter_kontrolü():
                ekran_temizle()
                print(get_text("helipad_success"))
                print(get_text("helipad_game_complete"))
                break
            else:
                ekran_temizle()
                print(get_text("helipad_locked"))
        
        # 11) OYUNDAN ÇIK
        elif hinput == "11":
            quit_game(oyuncu)
            
        else:
            print(get_text("invalid_choice_general"))

def kingdom_menu():
    menu = f"""
    {get_text('kingdom_title')}
        {get_text('kingdom_1')}
        {get_text('kingdom_2')}
        {get_text('kingdom_3')}
        {get_text('kingdom_4')}
        {get_text('kingdom_5')}
        {get_text('kingdom_6')}
        {get_text('kingdom_7')}
        {get_text('kingdom_8')}
        {get_text('kingdom_choice')}"""
    h2input = input(menu).strip()
    
    if h2input == "1":
        ekran_temizle()
        core.alan_deltası = 100
        savas()
    elif h2input == "2":
        ekran_temizle()
        core.alan_deltası = 150
        savas()
    elif h2input == "3":
        ekran_temizle()
        core.alan_deltası = 200
        savas()
    elif h2input == "4":
        ekran_temizle()
        core.alan_deltası = 225
        savas()
    elif h2input == "5":
        ekran_temizle()
        core.alan_deltası = 250
        savas()
    elif h2input == "6":
        ekran_temizle()
        core.alan_deltası = 300
        savas()
    elif h2input == "7":
        if oyuncu.seviye >= 15:
            ekran_temizle()
            boss_savas()
        else:
            print(get_text("kingdom_level_required"))
    elif h2input == "8":
        print(get_text("kingdom_exit"))
    else:
        print(get_text("invalid_choice"))

def shop_menu():
    menu = f"""
    {get_text('shop_title')}
        {get_text('shop_armor')}
            {get_text('armor_chain')}
            {get_text('armor_iron')}
            {get_text('armor_delta')}
            {get_text('armor_mithril')}
            {get_text('armor_adamant')}
            {get_text('armor_neo')}
        {get_text('shop_sword')}
            {get_text('sword_copper')}
            {get_text('sword_iron')}
            {get_text('sword_delta')}
            {get_text('sword_mithril')}
            {get_text('sword_adamant')}
            {get_text('sword_neo')}
        {get_text('shop_food')}
        {get_text('shop_potion')}
        {get_text('shop_mystery_box')}
        {get_text('shop_exit')}
        {get_text('shop_choice')}"""
    minput = input(menu).strip().lower()
    
    # ZIRH ALIMLARI
    armor_items = {
        "1a": (50, 5, 1, "bought_armor_chain"),
        "1b": (100, 10, 2, "bought_armor_iron"),
        "1c": (250, 15, 3, "bought_armor_delta"),
        "1d": (300, 20, 4, "bought_armor_mithril"),
        "1e": (500, 30, 5, "bought_armor_adamant"),
        "1f": (750, 50, 6, "bought_armor_neo")
    }
    
    if minput in armor_items:
        cost, defense, level, msg = armor_items[minput]
        if oyuncu.zirh_seviyesi >= level:
            print(get_text("already_have"))
        elif oyuncu.delta < cost:
            print(get_text("not_enough_delta"))
        else:
            oyuncu.delta -= cost
            if hasattr(oyuncu, 'onceki_zirh_defansi'):
                oyuncu.defans -= oyuncu.onceki_zirh_defansi
            oyuncu.defans += defense
            oyuncu.zirh_seviyesi = level
            oyuncu.onceki_zirh_defansi = defense
            print(get_text(msg))
    
    # KILIÇ ALIMLARI
    sword_items = {
        "2a": (25, 5, 1, "bought_sword_copper"),
        "2b": (125, 10, 2, "bought_sword_iron"),
        "2c": (230, 15, 3, "bought_sword_delta"),
        "2d": (260, 20, 4, "bought_sword_mithril"),
        "2e": (460, 30, 5, "bought_sword_adamant"),
        "2f": (700, 50, 6, "bought_sword_neo")
    }
    
    if minput in sword_items:
        cost, power, level, msg = sword_items[minput]
        if oyuncu.kilic_seviyesi >= level:
            print(get_text("already_have_sword"))
        elif oyuncu.delta < cost:
            print(get_text("not_enough_delta"))
        else:
            oyuncu.delta -= cost
            if hasattr(oyuncu, 'onceki_kilic_gucu'):
                oyuncu.guc -= oyuncu.onceki_kilic_gucu
            oyuncu.guc += power
            oyuncu.kilic_seviyesi = level
            oyuncu.onceki_kilic_gucu = power
            print(get_text(msg))
    
    # YEMEK
    elif minput == "3":
        if oyuncu.delta < 30:
            print(get_text("not_enough_delta"))
        else:
            oyuncu.delta -= 30
            oyuncu.envanter["food"] += 1
            print(get_text("bought_food"))
    
    # İKSİR
    elif minput == "4":
        if oyuncu.delta < 60:
            print(get_text("not_enough_delta"))
        else:
            oyuncu.delta -= 60
            oyuncu.envanter["potion"] += 1
            print(get_text("bought_potion"))
    
    # GİZEMLİ KUTU
    elif minput == "5":
        if oyuncu.delta < 150:
            print(get_text("not_enough_delta"))
        else:
            oyuncu.delta -= 150
            sans = r.randint(1, 5)
            if sans == 1:
                oyuncu.delta += 200
                print(get_text("mystery_box_delta", 200))
            elif sans == 2:
                oyuncu.guc += 5
                print(get_text("mystery_box_power", 5))
            elif sans == 3:
                oyuncu.defans += 5
                print(get_text("mystery_box_defense", 5))
            elif sans == 4:
                oyuncu.envanter["potion"] += 1
                print(get_text("mystery_box_potion", 1))
            else:
                oyuncu.maxhp += 10
                oyuncu.hp = min(oyuncu.maxhp, oyuncu.hp + 10)
                print(get_text("mystery_box_hp", 10))
    
    # ÇIKIŞ
    elif minput == "6":
        print(get_text("shop_exit_msg"))
    else:
        print(get_text("invalid_choice"))

def save_load_menu():
    menu = f"""
    {get_text('save_load_title')}
        {get_text('save_game')}
        {get_text('load_game_opt')}
        {get_text('return')}
        {get_text('save_load_choice')}"""
    slinput = input(menu).strip()
    
    if slinput == "1":
        save_game(oyuncu)
    elif slinput == "2":
        loaded_player = load_game()
        # Global oyuncu referansını güncelle
        for key, value in loaded_player.__dict__.items():
            setattr(oyuncu, key, value)
    elif slinput == "3":
        pass
    else:
        print(get_text("invalid_choice"))

def quest_menu():
    menu = f"""
    {get_text('quest_title')}
        {get_text('quest_active')}
        {get_text('quest_new')}
        {get_text('quest_complete')}
        {get_text('quest_exit')}
        {get_text('quest_choice')}"""
    ginput = input(menu).strip()
    
    if ginput == "1":
        # Aktif görevi göster
        if oyuncu.aktif_gorev:
            quest_type = oyuncu.aktif_gorev.get('type', 'unknown')
            progress = oyuncu.aktif_gorev.get('progress', 0)
            target = oyuncu.aktif_gorev.get('target', 0)
            
            # Görev tipini çevir
            if quest_type == 'kill':
                quest_name = get_text('quest_kill')
            elif quest_type == 'collect':
                quest_name = get_text('quest_collect')
            elif quest_type == 'boss':
                quest_name = get_text('quest_boss')
            else:
                quest_name = quest_type
            
            print(get_text('quest_info', quest_name, progress, target))
        else:
            print(get_text('no_active_quest'))
    
    elif ginput == "2":
        # Yeni görev al
        if oyuncu.aktif_gorev:
            print(get_text('quest_already_active'))
        else:
            quest_types = ['kill', 'collect', 'boss']
            quest_type = r.choice(quest_types)
            
            if quest_type == 'kill':
                oyuncu.aktif_gorev = {'type': 'kill', 'target': 5, 'progress': 0}
                print(get_text('quest_received', get_text('quest_kill')))
            elif quest_type == 'collect':
                oyuncu.aktif_gorev = {'type': 'collect', 'target': 1000, 'progress': oyuncu.delta}
                print(get_text('quest_received', get_text('quest_collect')))
            else:
                oyuncu.aktif_gorev = {'type': 'boss', 'target': 1, 'progress': 0}
                print(get_text('quest_received', get_text('quest_boss')))
    
    elif ginput == "3":
        # Görevi tamamla
        if not oyuncu.aktif_gorev:
            print(get_text('no_active_quest'))
        else:
            quest_type = oyuncu.aktif_gorev.get('type')
            progress = oyuncu.aktif_gorev.get('progress', 0)
            target = oyuncu.aktif_gorev.get('target', 0)
            
            # Collect görevi için özel kontrol
            if quest_type == 'collect':
                progress = oyuncu.delta
            
            if progress >= target:
                # Ödüller ver
                delta_reward = 500
                xp_reward = 100
                oyuncu.delta += delta_reward
                oyuncu.xp += xp_reward
                print(get_text('quest_completed', delta_reward, xp_reward))
                oyuncu.tamamlanan_gorevler.append(oyuncu.aktif_gorev)
                oyuncu.aktif_gorev = None
                oyuncu.seviye_atla()
            else:
                print(get_text('quest_not_completed'))
    
    elif ginput == "4":
        print(get_text('quest_exit_msg'))
    else:
        print(get_text('invalid_choice'))

def activity_menu():
    menu = f"""
    {get_text('activity_title')}
        {get_text('activity_fishing')}
        {get_text('activity_mining')}
        {get_text('activity_hunting')}
        {get_text('activity_exit')}
        {get_text('activity_choice')}"""
    ainput = input(menu).strip()
    
    if ainput == "1":
        # Balık tutma
        if oyuncu.seviye >= 2:
            delta_earned = r.randint(20, 50)
            oyuncu.delta += delta_earned
            print(get_text('fishing_success', delta_earned))
        else:
            print(get_text('activity_level_req', 2))
    
    elif ainput == "2":
        # Madencilik
        if oyuncu.seviye >= 3:
            delta_earned = r.randint(30, 70)
            oyuncu.delta += delta_earned
            print(get_text('mining_success', delta_earned))
        else:
            print(get_text('activity_level_req', 3))
    
    elif ainput == "3":
        # Avlanma
        if oyuncu.seviye >= 4:
            delta_earned = r.randint(40, 80)
            oyuncu.delta += delta_earned
            print(get_text('hunting_success', delta_earned))
        else:
            print(get_text('activity_level_req', 4))
    
    elif ainput == "4":
        print(get_text('activity_exit_msg'))
    else:
        print(get_text('invalid_choice'))

def delta_market_menu():
    if oyuncu.seviye >= 10:
        menu = f"""
        {get_text('delta_market_title')}
            {get_text('delta_armor')}
                {get_text('delta_armor_ultra_mithril')}
                {get_text('delta_armor_obsidian')}
                {get_text('delta_armor_neo_mithril')}
                {get_text('delta_armor_ultra_adamant')}
                {get_text('delta_armor_neo_gamma')}
            {get_text('delta_sword')}
                {get_text('delta_sword_ultra_mithril')}
                {get_text('delta_sword_obsidian')}
                {get_text('delta_sword_neo_mithril')}
                {get_text('delta_sword_ultra_adamant')}
                {get_text('delta_sword_neo_gamma')}
            {get_text('delta_food')}
            {get_text('delta_potion')}
            {get_text('delta_ultra_box')}
            {get_text('delta_exit')}
            {get_text('delta_choice')}"""
        dmiinput = input(menu).strip().lower()
        
        # DELTA MARKET ZIRHLARI
        delta_armors = {
            "1a": (600, 40, 7, "bought_armor"),
            "1b": (900, 50, 8, "bought_armor"),
            "1c": (1100, 60, 9, "bought_armor"),
            "1d": (1400, 70, 10, "bought_armor"),
            "1e": (2700, 100, 11, "bought_armor")
        }
        
        if dmiinput in delta_armors:
            cost, defense, level, msg = delta_armors[dmiinput]
            if oyuncu.zirh_seviyesi >= level:
                print(get_text("already_have"))
            elif oyuncu.delta < cost:
                print(get_text("not_enough_delta"))
            else:
                oyuncu.delta -= cost
                if hasattr(oyuncu, 'onceki_zirh_defansi'):
                    oyuncu.defans -= oyuncu.onceki_zirh_defansi
                oyuncu.defans += defense
                oyuncu.zirh_seviyesi = level
                oyuncu.onceki_zirh_defansi = defense
                print(get_text(msg))
        
        # DELTA MARKET KILIÇLARI
        delta_swords = {
            "2a": (550, 60, 7, "bought_sword"),
            "2b": (800, 70, 8, "bought_sword"),
            "2c": (1025, 75, 9, "bought_sword"),
            "2d": (1300, 80, 10, "bought_sword"),
            "2e": (2600, 100, 11, "bought_sword")
        }
        
        if dmiinput in delta_swords:
            cost, power, level, msg = delta_swords[dmiinput]
            if oyuncu.kilic_seviyesi >= level:
                print(get_text("already_have_sword"))
            elif oyuncu.delta < cost:
                print(get_text("not_enough_delta"))
            else:
                oyuncu.delta -= cost
                if hasattr(oyuncu, 'onceki_kilic_gucu'):
                    oyuncu.guc -= oyuncu.onceki_kilic_gucu
                oyuncu.guc += power
                oyuncu.kilic_seviyesi = level
                oyuncu.onceki_kilic_gucu = power
                print(get_text(msg))
        
        # YEMEK+++
        elif dmiinput == "3":
            if oyuncu.delta < 50:
                print(get_text("not_enough_delta"))
            else:
                oyuncu.delta -= 50
                oyuncu.hp = min(oyuncu.maxhp, oyuncu.hp + 50)
                print(get_text("food_plus_bought"))
        
        # İKSİR++
        elif dmiinput == "4":
            if oyuncu.delta < 80:
                print(get_text("not_enough_delta"))
            else:
                oyuncu.delta -= 80
                oyuncu.envanter["potion"] += 2
                print(get_text("potion_plus_bought"))
        
        # ULTRA GİZEMLİ KUTU
        elif dmiinput == "5":
            if oyuncu.delta < 300:
                print(get_text("not_enough_delta"))
            else:
                oyuncu.delta -= 300
                sans = r.randint(1, 5)
                if sans == 1:
                    oyuncu.delta += 500
                    print(get_text("ultra_box_delta", 500))
                elif sans == 2:
                    oyuncu.guc += 10
                    print(get_text("ultra_box_power", 10))
                elif sans == 3:
                    oyuncu.defans += 10
                    print(get_text("ultra_box_defense", 10))
                elif sans == 4:
                    oyuncu.envanter["potion"] += 2
                    print(get_text("ultra_box_potion", 2))
                else:
                    oyuncu.maxhp += 20
                    oyuncu.hp = min(oyuncu.maxhp, oyuncu.hp + 20)
                    print(get_text("ultra_box_hp", 20))
        
        elif dmiinput == "6":
            print(get_text("delta_exit_msg"))
        else:
            print(get_text("invalid_choice"))
    else:
        print(get_text("delta_level_required"))

def laboratory_menu():
    if oyuncu.seviye >= 12:
        menu = f"""
    {get_text('lab_title')}
            {get_text('lab_star_obs')}
            {get_text('lab_planet_obs')}
            {get_text('lab_equipment')}
            {get_text('lab_rocket')}
            {get_text('lab_exit')}
{get_text('lab_choice')}"""
        linput = input(menu).strip()
        
        if linput == "1":
            if oyuncu.seviye >= 3:
                esans = r.randint(1, 1000)
                print(get_text("lab_observed_stars"))
                # Easter egg
                if esans == 1:
                    print(get_text("lab_easter_egg"))
            else:
                print(get_text("activity_level_req", 3))
        
        elif linput == "2":
            if oyuncu.seviye >= 5:
                print(get_text("lab_observed_planets"))
            else:
                print(get_text("activity_level_req", 5))
        
        elif linput == "3":
            if oyuncu.seviye >= 7:
                print(get_text("lab_researched"))
            else:
                print(get_text("activity_level_req", 7))
        
        elif linput == "4":
            if oyuncu.seviye >= 9:
                print(get_text("lab_sent_rocket"))
            else:
                print(get_text("activity_level_req", 9))
        
        elif linput == "5":
            print(get_text("lab_exit_msg"))
        else:
            print(get_text("invalid_choice"))
    else:
        print(get_text("lab_level_required"))

if __name__ == "__main__":
    map()

