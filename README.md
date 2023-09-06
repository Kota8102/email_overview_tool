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

以下はプロジェクトの主要なディレクトリ構造と各ディレクトリ/ファイルの説明です。

```
.
├── .devcontainer
│   └── devcontainer.json          # 開発コンテナの設定ファイル
├── .env                          # 環境変数を設定するためのファイル
├── .gitignore                    # gitで無視するファイル/ディレクトリのリスト
├── Makefile                      # セットアップや依存関係のインストールのためのMakefile
├── README.md                     # プロジェクトの説明と使用方法を記載したドキュメント
├── output
│   └── output.md                 # 生成されたメールの概要を保存するMarkdownファイル
├── requirements.txt              # プロジェクトの依存関係をリスト化したファイル
└── src
    ├── main.py                   # 主要な実行ファイル
    └── modules
        ├── get_overview.py       # OpenAIを使用してメールの概要を生成するモジュール
        └── output_markdown.py    # 生成された概要をMarkdown形式で保存するモジュール

```

## Troubleshooting

### .env: no such file or directory

.env ファイルがないので環境変数の一覧を参考に作成しましょう