from pprint import pprint
import bot
import pandas as pd
import language_processor
import time

start = time.time()
file = pd.read_csv("Names in Google Sheet Test - Sheet1.csv", names=["link", "name", "rating", "a_num", "phone", "addr", "ceo"])
file.dropna(inplace=True)
link_count = len(file.link)
processed_information = []

itr = 0
robot = bot.ReviewBot()
for index, row in file.iterrows():
    robot.get_reviews(index=index, link=row.link, num_of_links=link_count)
    # itr = index
    itr += 1
    if itr > 1:
        robot.destroy()
        break

extractor = language_processor.NameExtractor()
t = []
reviews = robot.business_reviews
for idx in range(itr):
    owner_name = extractor.extract_name(reviews[idx][:5])
    processed_information.append({
        "Link": file.loc[idx]["link"],
        "Business": file.loc[idx]["name"],
        "Address": file.loc[idx]["addr"],
        "Owner": owner_name
    })
    t.append(extractor.extract_name(reviews[idx][:5]))
pprint(t)
file_path = "output3.csv"
df = pd.DataFrame(processed_information)
df.to_csv(file_path)
print("Total time in seconds", start-time.time())

# for i in range(2):
#     print(f"Of length {len(names[i])}")
