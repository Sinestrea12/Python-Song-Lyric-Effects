import sys
from time import sleep
# Code by Kuroneko
def print_lyrics():
    lines = [
        (" ผ่อนลมหายใจตามเสียงดนตรีบรรเลง", 0.1, "\033[34m"),  # สีน้ำเงิน
        (" จังหวะหัวใจสั่นไหวพวกเรามาร้องเพลง ", 0.1, "\033[34m"),  # สีน้ำเงิน
        (" ส่งไปให้ถึงความนัยที่เคยปิดบัง ", 0.1, "\033[34m"),  # สีน้ำเงิน
        (" ตัวฉันอยากจะรัก อยากจะรักเเค่เธอผู้เดียว ", 0.1, "\033[34m"),  # สีน้ำเงิน
        (" ช่วยตอบหน่อยได้ไหม ว่าเธอคิดยังไง ", 0.1, "\033[34m"),  # สีน้ำเงิน
        (" แค่ตอบหน่อยได้ไหม เรื่องราวของฉันและเธอ ", 0.1, "\033[34m"),  # สีน้ำเงิน
        (" ขยับเข้ามาอีกนิด ถ้อยคำที่ฉันอยากเจอ ", 0.1, "\033[34m"),  # สีน้ำเงิน
        (" แค่สองเราอยู่ด้วยกันเสมอ ", 0.1, "\033[34m"),  # สีน้ำเงิน
        (" รักเธอ ", 0.1, "\033[1;31m"), # สีแดงหนา
    ]
# Code by Kuroneko
    delays = [1, 1, 1, 1, 0.8, 0.5, 0.3, 1.5] #ดีเลย์หาเอง

    for i, (line, char_delay, color) in enumerate(lines):
        print(color, end='')
# Code by Kuroneko
        for char in line:
            print(char, end='', flush=True)
            sleep(char_delay)

        print("\033[0m", end='') # สีแดงหนา

        if i < len(delays):
            sleep(delays[i])

        print('')

print_lyrics()
