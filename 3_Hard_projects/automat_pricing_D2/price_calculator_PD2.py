
class RuneCalculator:
    def __init__(self, wss):
        self.wss = wss
        self.runes = {
            'lum' : {'hr_rate' : 0.01},
            'ko' : {'hr_rate' : 0.01},
            'fal' : {'hr_rate' : 0.02},
            'lem' : {'hr_rate' : 0.02},
            'pul' : {'hr_rate' : 0.03},
            'um' : {'hr_rate' : 0.05},
            'mal' : {'hr_rate' : 0.1},
            'ist' : {'hr_rate' : 0.15},
            'gul' : {'hr_rate' : 0.25},
            'vex' : {'hr_rate' : 0.5},
            'ohm' : {'hr_rate' : 0.75},
            'lo' : {'hr_rate' : 1},
            'sur' : {'hr_rate' : 1.3},
            'ber' : {'hr_rate' : 2.6},
            'jah' : {'hr_rate' : 1.25},
            'cham' : {'hr_rate' : 1},
            'zod' : {'hr_rate' : 1.5}
        }
        
    def calculate_prices(self, rune):
        if rune in self.runes:
            rune_info = self.runes[rune]
            hr_rate = rune_info['hr_rate']
            wss_price = round(hr_rate * self.wss)
            pgem_price = wss_price * 7
            reroll_price = round(pgem_price * (2/3))
            print()
            print(f'### {rune} ###')
            print(f'{rune} / {hr_rate} HR / {(wss_price)} wss / {pgem_price} pgems / {reroll_price} reroll runes' )
            print()
        
        else:
            print('Wrong input')

while True:        
    try:        
        wss_input = int(input('What is the ammount of WSS in HR: '))
        
    except ValueError:
        print('Please input correct value')
        continue
    
    break

while True:
    rune_input = input('Input rune name: ')
    
    
    calculator = RuneCalculator(wss_input)
    calculator.calculate_prices(rune_input.lower())