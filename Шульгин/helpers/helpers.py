import pandas as pd

df = pd.read_excel('helpers/profiles.xlsx')
df_progress = pd.read_excel('helpers/09.04 ИС УРФУ (1).xlsx')

# df = pd.read_excel('profiles.xlsx')
# df_progress = pd.read_excel('diagnostics.xlsx')


def get_profile(username):
    user_frame = df.loc[df['Username'].str.lower() == username.lower()]
    if user_frame.empty:
        user_frame = df.loc[df['email'].str.lower() == username.lower()]

    if user_frame.empty:
        print("User not found: " + username)
        return {}
    else:
        if user_frame.shape[0] > 1:
            print("Duplicate user in profile: " + username)
        user = user_frame.iloc[0]
        if pd.isna(user['leader_id']):
            print("User have empty leader_id: " + username)
            return {}
        else:
            return user.to_dict()


def get_leader_id(username):
    user_frame = df.loc[df['Username'].str.lower() == username.lower()]
    if user_frame.empty:
        user_frame = df.loc[df['email'].str.lower() == username.lower()]

    if user_frame.empty:
        print("User not found: " + username)
        return ""
    else:
        if user_frame.shape[0] > 1:
            print("Duplicate user in profile: " + username)
        user = user_frame.iloc[0]
        if pd.isna(user['leader_id']):
            print("User have empty leader_id: " + username)
            return ""
        else:
            return str(user['leader_id'].lower().replace("id", ""))


def get_leader_id_progress(username):
    # print(df_progress)
    df_progress['Leader ID'] = df_progress['Leader ID'].astype(str)
    # print(df_progress['Leader ID'])
    leader_id = get_leader_id(username)
    # print(leader_id)
    if len(leader_id) > 0:
        user_progress_frame = df_progress.loc[df_progress['Leader ID'] == leader_id]
        # print("!!!!", user_progress_frame)
        if user_progress_frame.shape[0] == 0:
            print("Activities not found: ", username)
            return 0
        else:
            user_progress = user_progress_frame.iloc[0]
            if pd.isna(user_progress['Прогресс прохождения обязательных активностей']):
                print("Activities progress error: ", username)
                return 0
            else:
                return user_progress['Прогресс прохождения обязательных активностей'].astype(int)
    else:
        return 0


def leader_id_progress(leader_id):
    # print(leader_id)
    df_progress['Leader ID'] = df_progress['Leader ID'].astype(str)

    if len(leader_id) > 0:
        user_progress_frame = df_progress.loc[df_progress['Leader ID'] == leader_id]
        # print("!!!!", user_progress_frame)
        if user_progress_frame.shape[0] == 0:
            print("Activities not found: ", leader_id)
            return 0
        else:
            user_progress = user_progress_frame.iloc[0]
            if pd.isna(user_progress['Прогресс прохождения обязательных активностей']):
                print("Activities progress error: ", username)
                return 0
            else:
                return user_progress['Прогресс прохождения обязательных активностей'].astype(int)
    else:
        return 0

# get_leader_id_progress("Balakin_Sergei")