import datetime

# ユーザーの予約情報（この部分は実際にはウェブサーバから取得されるでしょう）
reservations = {
    'user1': [
        {'start': '2024-04-08 09:00', 'end': '2024-04-08 09:30'},
        {'start': '2024-04-08 13:00', 'end': '2024-04-08 14:00'}
    ]
}

def check_reservation(user_id):
    now = datetime.datetime.now()
    for reservation in reservations.get(user_id, []):
        start = datetime.datetime.strptime(reservation['start'], '%Y-%m-%d %H:%M')
        end = datetime.datetime.strptime(reservation['end'], '%Y-%m-%d %H:%M')
        if start <= now <= end:
            return True
    return False

def main():
    user_id = input("ユーザーIDを入力してください: ")
    if check_reservation(user_id):
        print(f"{user_id} は現在、ログイン可能です。")
    else:
        print(f"{user_id} は現在、ログイン不可能です。時間外です。")

if __name__ == "__main__":
    main()
