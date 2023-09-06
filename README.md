# email_overview_tool


## Description

OpenAI API を利用して、メールの概要を生成するツールです。


## Installation

make コマンドを利用して初期化を行います。
```bash
make init
```

makeコマンドが利用不可の場合は以下のコマンドを実行してください。
```bash
pip install -r requirements.txt

echo 'OPENAI_API_KEY="ここにAPIキーを記載してください"' > .env
```

## Configuration

.env ファイルに以下の環境変数を記載してください。
```bash
OPENAI_API_KEY="ここにAPIキーを記載してください"
```

## Usage

このツールを使用するための基本的な手順は以下のとおりです。
1. まず、必要なライブラリをインストールしてください。詳細は[Installation](#Installation)を参照してください。
2. 次に、.envファイルを作成し、OpenAI APIキーを設定してください。[Configuration](#Configuration)に詳しい手順が記載されています。
3. すべての設定が完了したら、以下のコマンドを実行して、メールの概要を生成します。

```python
python src/main.py
```

このコマンドは、設定されたOpenAIモデルを使用して、指定されたメールの概要を生成し、結果をMarkdown形式でoutputディレクトリのoutput.mdファイルに保存します。

## Directory
```
.
├── .devcontainer
│   └── devcontainer.json
├── .env
├── .gitignore
├── Makefile
├── README.md
├── output
    └── output.md
├── requirements.txt
└── src
    ├── main.py
    └── modules
        ├── get_overview.py
        └── output_markdown.py
```

## Troubleshooting

### .env: no such file or directory

.env ファイルがないので環境変数の一覧を参考に作成しましょう