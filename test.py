import streamlit as st
from streamlit import session_state as ss
import pandas as pd
import time
from datetime import datetime as dt
time_start = time.time()
# start = dt.now()
time.sleep(6)
# end = dt.now()
time_end = time.time()
# print(start)
# print(end-start)
print(time_end-time_start)

# print(f"Abeg: {'browse_clicked' in st.session_state}")
#
# st.title("File Uploading and Processing")
# uploaded_file = st.file_uploader("Upload CSV file", type=["csv"], disabled=False)
#
# if uploaded_file:
#     disable = True
#     ss["fg"] = False
#     print(f"at here {ss['fg']}")
#     print(f"Disable is now: {disable}")
#     # disable()
# #     ss['file'] = uploaded_file  # backup the file
# #     t = uploaded_file
# #     print(ss['file'])
# #     ss['show_uploader'] = False
# #     st.rerun()
# # print("this is ss", ss["file"])
# # print("this is t", t)
# # if ss["file"]:
#     print("in body")
#     # uploaded_file = ss["file"]
#     df = pd.read_csv(uploaded_file)
#
#     # Display the uploaded data
#     st.write("Uploaded Data:")
#     st.write(df)
#
#     f"File is of type {type(uploaded_file)}"
#
#     def generate_csv_content():
#         # Your CSV generation code here
#         data = {
#             'Column1': [1, 2, 3],
#             'Column2': ['A', 'B', 'C']
#         }
#         df = pd.DataFrame(data)
#         csv_content = df.to_csv(index=False)
#         return csv_content.encode()
#
#     if st.button("Generate and Download CSV"):
#             csv_content = generate_csv_content()
#             st.download_button(
#                 label="Download CSV",
#                 data=csv_content,
#                 file_name="generated_file.csv",
#                 mime="text/csv"
#             )


# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)