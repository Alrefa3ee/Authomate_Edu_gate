import main
from dotenv import load_dotenv
import os

load_dotenv()
# 501293 رقم ماده تصميم المنطق الرقمي
# 3 رقم شعبة الدكتور معن
clase_number, subject_id = 3, "501293"

status = main.main(clase_number, subject_id)

print(status)
