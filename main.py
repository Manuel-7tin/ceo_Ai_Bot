import bot
import time
import pandas as pd
import streamlit as st
import language_processor




def start():
    start_time = time.time()
    file = pd.read_csv(csv_file, names=["link", "name", "rating", "a_num", "phone", "addr", "ceo"])
    file.dropna(inplace=True)
    link_count = len(file.link)
    processed_information = []

    itr = 0
    robot = bot.ReviewBot()
    for index, row in file.iterrows():
        robot.get_reviews(index=index, link=row.link, num_of_links=link_count)
        itr = index

    extractor = language_processor.NameExtractor()
    reviews = robot.business_reviews
    for idx in range(itr):
        owner_name = extractor.extract_name(reviews[idx][:5])
        st.write(f"Processing link {idx + 1} of {itr + 1}")
        processed_information.append({
            "Link": file.loc[idx]["link"],
            "Business": file.loc[idx]["name"],
            "Address": file.loc[idx]["addr"],
            "Owner": owner_name
        })

    file_path = "output.csv"
    df = pd.DataFrame(processed_information)
    output_file = df.to_csv()
    end_time = time.time()
    return output_file.encode(), end_time - start_time

st.title("Business Owner Name Extractor")
csv_file = st.file_uploader("Upload CSV file", type=["csv"], disabled=False)
if csv_file:
    if st.button("Run Bot"):
        st.write("Bot running...")
        output = start()
        csv_content = output[0]
        st.write(f"Total time spent in seconds: {output[1]}")
        st.download_button(
            label="Download CSV",
            data=csv_content,
            file_name="generated_file.csv",
            mime="text/csv"
        )

