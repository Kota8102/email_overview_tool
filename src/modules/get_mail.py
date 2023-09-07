import pprint
from datetime import datetime

import win32com.client


def search_folder_for_today_emails(target_folder_name, folder, emails_list):
    """指定したフォルダ名に一致するフォルダを探して、そのフォルダ内の今日のメールを取得します。"""
    if folder.Name == target_folder_name:
        today = datetime.today().date()
        
        # フォルダ名が一致した場合、そのフォルダ内のメールを取得
        for message in folder.Items:
            if hasattr(message, "ReceivedTime") and message.ReceivedTime.date() == today:
                email_data = {
                    "件名": message.Subject,
                    "本文": message.Body
                }
                emails_list.append(email_data)
    else:
        # フォルダ名が一致しない場合、サブフォルダを探索
        for subfolder in folder.Folders:
            search_folder_for_today_emails(target_folder_name, subfolder, emails_list)

def get_today_emails_from_specific_folder(target_folder_name):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    
    emails_list = []

    # すべてのアカウントを探索
    for account_folder in outlook.Folders:
        search_folder_for_today_emails(target_folder_name, account_folder, emails_list)

    return emails_list

def get_emails(folder_name):

    emails = get_today_emails_from_specific_folder(folder_name)

    return emails



if __name__ == '__main__':

    folder_name = "マーケティングメール"  # こちらに検索したいフォルダ名を入力してください
    result = get_emails(folder_name)

    pprint.pprint(result)