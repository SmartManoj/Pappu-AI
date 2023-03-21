hours_colloquial ={
    '01': 'ஒன்னு',
    '02': 'ரெண்டு',
    '03': 'மூனு',
    '04': 'நாலு',
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
    '50' : 'ஐம்பது',
    '55': 'ஐம்பத்தஞ்சு',
    '0': '',
}

from datetime import datetime
def round_to_nearest_5(x):
    a=  str(5 * round(float(x)/5)) 
    if a=='60':
        return '0'
    return a

def time_in_tamil():
    hour, minute = datetime.now().strftime('%I:%M').split(':')
    minute = round_to_nearest_5(minute)

    minute2 = mins_colloquial[minute]
    if minute2 == '00' and minute != minute2:
        hour = hours_colloquial[str(int(hour)+1)]
    else:
        if minute2 in ['15','45']:
            hour = hours_colloquial_15[hour]
        elif minute2 == '30':
            hour = hours_colloquial_15[hour]
            minute2 =''
        else:
            hour = hours_colloquial[hour]
    print(hour + ' ' + minute2)
    return hour + ' ' + minute2
