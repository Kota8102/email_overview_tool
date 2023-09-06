from modules.get_overview import LLMOverview
from modules.output_markdown import save_to_markdown


def main():

    input_mails = [
        {"件名": "aaa", "本文": "bbb"},
        {"件名": "ccc", "本文": "ddd"},
        {"件名": "eee", "本文": "fff"},
    ]

    model_name = "gpt-3.5-turbo"

    # LLMOverviewのインスタンスを作成
    overview_obj = LLMOverview(model_name=model_name)

    summaries = []
    for mail in input_mails:
        summarized_content = overview_obj.generate_overview(mail["本文"])
        summaries.append({
            "件名": mail["件名"],
            "要約": summarized_content
        })

    save_to_markdown(summaries)


if __name__ == '__main__':
    main()
