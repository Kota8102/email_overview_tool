from tqdm import tqdm

from modules.get_mail import get_emails
from modules.get_overview import LLMOverview
from modules.output_markdown import save_to_markdown


def main():

    # メールのフォルダ名とモデル名を指定
    folder_name = "マーケティングメール"
    model_name = "gpt-3.5-turbo"

    print("\nFetching emails...")
    input_mails = get_emails(folder_name)
    print(f"Fetched {len(input_mails)} emails.\n")

    print("Initializing LLMOverview...")

    overview_obj = LLMOverview(model_name=model_name)
    print("LLMOverview initialized.\n")

    summaries = []
    print("Generating summaries for emails...")

    for mail in tqdm(input_mails, desc="Summarizing", ncols=100):
        summarized_content = overview_obj.generate_overview(mail["本文"])
        summaries.append({
            "件名": mail["件名"],
            "要約": summarized_content
        })

    print("Saving summaries to markdown...")
    save_to_markdown(summaries)
    print("Summaries saved successfully.\n")

if __name__ == '__main__':
    main()
