import os
from datetime import datetime

import pytz


def save_to_markdown(texts, directory="output"):
    # 現在の日付と時間を取得
    tokyo_timezone = pytz.timezone('Asia/Tokyo')
    now = datetime.now(tokyo_timezone).strftime("%Y%m%d_%H%M%S")
    current_date = datetime.now(tokyo_timezone).strftime("%Y年%m月%d日")
    filename = f"{directory}/{now}_output.md"

    # outputディレクトリが存在しない場合、ディレクトリを作成
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as file:

        file.write(f"# {current_date}のメール一覧\n\n")
        # 合計の件数を記載
        file.write(f"## 合計件数: {len(texts)} 件\n\n")

        # 要約のリストを記載
        file.write("## 要約\n")
        for text_dict in texts:
            file.write(f"- **件名**: {text_dict['件名']}\n")
            file.write(f"  - **要約**: {text_dict['要約']}\n\n")


if __name__ == '__main__':
    texts_to_summarize = [
        {"件名": "サンプル1", "要約": "ここには第一のメールのサンプルテキストや要約したい内容を入力します。"},
        {"件名": "サンプル2", "要約": "次のテキストは異なる内容を持っています。それに関する概要も取得したい。"},
        {"件名": "サンプル3", "要約": "最後のテキストサンプル。これも要約します。"}
    ]

    save_to_markdown(texts_to_summarize)
