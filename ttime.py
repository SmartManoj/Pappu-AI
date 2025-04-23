hours_colloquial ={
    '01': 'ஒன்னு',
    '02': 'ரெண்டு',
    '03': 'மூனு',
    '04': 'நால்',
    '05': 'அஞ்சு',
    '06': 'ஆறு',
    '07': 'ஏழு',
    '08': 'எட்டு',
    '09': 'ஒம்போது',
    '10': 'பத்து',
    '11': 'பதனொன்னு',
    '12': 'பன்னண்டு',
}

hours_colloquial_15 =  {
    '01': 'ஒன்னே',
    '02': 'ரெண்டே',
    '03': 'மூனே',
    '04': 'நாலே',
    '05': 'அஞ்சே',
    '06': 'ஆறே',
    '07': 'ஏழே',
    '08': 'எட்டே',
    '09': 'ஒம்போதே',
    '10': 'பத்தே',
    '11': 'பதனொன்னே',
    '12': 'பன்னண்டே'
}
hours_colloquial_30 =  {
    '01': 'ஒன்ர',
    '02': 'ரெண்ர',
    '03': 'மூன்ர',
    '04': 'நால்ர',
    '05': 'அஞ்ர',
    '06': 'ஆர்ர',
    '07': 'ஏழ்ர',
    '08': 'எட்ர',
    '09': 'ஒம்போதர',
    '10': 'பத்தர',
    '11': 'பதனொன்ர',
    '12': 'பன்னண்ர'
}
mins_colloquial ={
    '5': 'அஞ்சு',
    '10': 'பத்து',
    '15' : 'கால்',
    '20': 'இருபது',
    '25': 'இருபத்தஞ்சு',
    '30' : 'அரை',
    '35': 'முப்பத்தஞ்சு',
    '40' : 'நாப்பது',
    '45' : 'முக்கால்',
    '50' : 'அம்பது',
    '55': 'அம்பத்தஞ்சு',
    '0': '',
}

from datetime import datetime, timedelta
import sys
def round_to_nearest_5(x):
    a=  str(5 * round(float(x)/5)) 
    if a=='60':
        return '0'
    return a

def exact_time_in_tamil():
    hour, minute =(datetime.utcnow()+timedelta(hours=5,minutes=30)).strftime('%I:%M').split(':')
    hour, minute = hour.lstrip('0'), minute.lstrip('0')
    return f'சரியான நேரம் "{hour}" "{minute}"'

def time_in_tamil():
    hour, minute =(datetime.utcnow()+timedelta(hours=5,minutes=30)).strftime('%I:%M').split(':')
    minute2 = round_to_nearest_5(minute)

    if int(minute) > 55:
        hour = f'{(int(hour)+1):02}'
    minute3 = mins_colloquial[minute2]
    if minute2 in ['15','45']:
        hour = hours_colloquial_15[hour]
    elif minute2 == '30':
        hour = hours_colloquial_30[hour]
        minute3 =''
    elif minute2 == '10':
        hour = hours_colloquial[hour] + 'ம்'
    else:
        hour = hours_colloquial[hour]
    print(hour + '' + minute3)
    return hour + '' + minute3

if __name__ == '__main__':
    from pyperclip import copy
    if sys.argv[1:]:
        time=(exact_time_in_tamil())
    else:
        time = (time_in_tamil())
    copy(time)
    print(time)
    print(exact_time_in_tamil())
    