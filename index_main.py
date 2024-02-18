from openai import OpenAI
# 2/18追加
import openai

import streamlit as st
from PIL import Image
import os

client = OpenAI()

# 2/18追加
openai.api_key = st.secrets["OPENAI_API_KEY"]

# # OpenAI APIキーを環境変数から取得
# api_key = os.environ.get('OPENAI_API_KEY')

# # OpenAI APIキーが設定されていない場合の処理
# if api_key is None:
#     st.error("OpenAI APIキーが設定されていません。")
#     st.stop()

# # OpenAI API初期化
# openai.api_key = api_key

# Streamlitアプリケーションのタイトル
st.title("OpenAIのmessage修正機能")

image = Image.open('./pc.png')
st.image(image, width=150)

st.text('エコチャンバー化しやすい環境に包まれて、思わず、私たちが言い過ぎたり、憎悪を煽動したり、軽蔑の眼差しを向けてしまわないようにmessageをChatGPTに修正してもらうプログラムを作りました。庶民の私は、APIの使用料が月10ドルを超えないように設定しました。入力文章は200字以内、連続3回くらいまでの使用で試してください。ご利用くださると、庶民オーナーは喜びます。')

st.text('入力例文：私は、ある国を旅行した時に、その国の人から嫌味を言われました。その国はひどい国なので、天罰が当たるように祈っています。')

st.text('返答例文：私は、ある国を旅行した際に、その国の人から嫌な言葉を言われました。私はその国の人々全体を非難するわけではありませんが、その経験によりその国のイメージが悪くなってしまいました。ただし、過度な軽蔑や憎悪を抱くことは良い解決策ではありません。私は個々の行動や言動に対して批判的になり、相互理解と共存を目指すよう努力します。')
# ユーザー入力のテキストボックス
user_input = st.text_input("ユーザーの文章")

# OpenAIによる返答
if st.button("送信"):
    # OpenAI ChatCompletion.create()の呼び出し
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful ethicist. Please, correct user's message."},
            {"role": "user", "content": user_input}],
        temperature = 0.2,
        max_tokens=600
    )
    # 返答の取得と出力
    bot_response = completion.choices[0].message.content
    st.write("AIの返答:", bot_response)

    
    