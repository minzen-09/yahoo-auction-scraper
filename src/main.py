import pandas as pd
from io import StringIO

sample_file_path = "../data/sample_purchase.html"

with open(sample_file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# StringIOでラップする
html_io = StringIO(html_content)

# HTMLテーブルを読み込む
df = pd.read_html(html_io)[0]

print("読み込み成功")
print(df)
