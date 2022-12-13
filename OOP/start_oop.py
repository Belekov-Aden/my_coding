# dict_note = {
#
# }
#
#
# class Laptop:
#     your_laptop = input('Write name your laptop: ')
#     dict_note['cpu'] = 'intel'
#     dict_note['ram'] = 16
#     dict_note['videcard'] = 'RTX 3050'
#
#
# print(f"{Laptop.your_laptop}:{dict_note}")


# DATA #2:
DATA = {

    "MARKERS": [
        {
            "NAME": "RIXOS THE PALM DUBAI",
            "POSITION": [25.1212, 55.1535],
        },

        {
            "NAME": "SHANGRI-LA HOTEL",
            "LOCATION": [25.2084, 55.2719]
        },

        {
            "NAME": "GRAND HYATT",
            "LOCATION": [25.2285, 55.3273]
        }
    ]
}


class Information:
    def __init__(self, data):
        self.data = data

    # 1 Метод который вернул имена отелей
    def GetName(self):
        name = []
        for i in self.data.values():
            for e in i:
                name.append(e['NAME'])
            print(name)

    # 2 Метод добавить в КОРТЕЖ имена и локацию. Дальше создать два ключя и указать данные
    def Collect_name_location(self):
        d_info = {
        }
        name_t = []
        loc_name = []

        for i in self.data.values():
            for e in i:
                name_t.append(e.get('NAME'))
                loc_name.append(e.get('POSITION') or e.get('LOCATION'))

        d_info['NAME'] = name_t
        d_info['LOCATION'] = loc_name
        print(d_info)

    # 3 метод добавление в словарь id
    def join_name(self):
        for i in self.data.values():
            c = 0
            for r in i:
                c += 1
                r['status id'] = c

        print(self.data)


info = Information(DATA)
info.GetName()
info.Collect_name_location()
info.join_name()
