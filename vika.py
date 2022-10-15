import pandas as pd
from vika import Vika

vika = Vika("usk6PShPgcDnhYTCrPnpYkC")
# 通过 datasheetId 来指定要从哪张维格表操作数据。
datasheet = vika.datasheet("dstlX7v5C4YqPpWNue", field_key="name")

# 返回所有记录的集合
records = datasheet.records.all()
x = []
for record in records:
    dc = record.json()
    x.append(dc)
print(x)

# 创建单条记录
row = datasheet.records.create({
    "员工号": 34459,
    "姓名": "大国",
    "渝康码状态": "绿码",
    "管控状态": "没有管控",
    "北京健康宝": "正常",
    "健康码截图": [
        {
            "id": "atcM6lyhrjH89",
            "name": "IMG_20221007_170227.jpg",
            "token": "space/2022/10/15/55de283e7d0d4e4cae47540785f6ef00",
        }
    ],
 })

