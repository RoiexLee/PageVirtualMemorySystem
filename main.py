import os

import pandas as pd
import streamlit as st

st.sidebar.title("页式虚拟存储器模拟")

system_policy = st.sidebar.selectbox("系统策略", [0, 1, 2])
if st.sidebar.button("创建系统"):
    with open("input_codes.csv", "ab") as f:
        f.write(f"{system_policy}\n".encode("utf-8"))
    ret = os.system("CMain.exe input_codes.csv output_phy_pages.csv output_logic_pages.csv output_access.csv output_records.csv")
    if ret == 0:
        st.sidebar.success("创建成功")
    else:
        st.sidebar.error("创建失败")

pid_new = st.sidebar.text_input("进程标识", key="pid_new", value="0")
process_size = st.sidebar.text_input("进程大小", value="00100000")
if st.sidebar.button("添加进程"):
    with open("input_codes.csv", "ab") as f:
        f.write(f"0 {pid_new} {process_size}\n".encode("utf-8"))
    ret = os.system("CMain.exe input_codes.csv output_phy_pages.csv output_logic_pages.csv output_access.csv output_records.csv")
    if ret == 0:
        st.sidebar.success("添加成功")
    else:
        st.sidebar.error("添加失败")

pid_get = st.sidebar.text_input("进程标识", key="pid_get", value="0")
logical_address = st.sidebar.text_input("逻辑地址", value="00000000")
if st.sidebar.button("访问"):
    with open("input_codes.csv", "ab") as f:
        f.write(f"1 {pid_get} {logical_address}\n".encode("utf-8"))
    ret = os.system("CMain.exe input_codes.csv output_phy_pages.csv output_logic_pages.csv output_access.csv output_records.csv")
    if ret == 0:
        st.sidebar.success("访问成功")
    else:
        st.sidebar.error("访问失败")

pid_del = st.sidebar.text_input("进程标识", key="pid_del", value="0")
if st.sidebar.button("删除进程"):
    with open("input_codes.csv", "ab") as f:
        f.write(f"2 {pid_del}\n".encode("utf-8"))
    ret = os.system("CMain.exe input_codes.csv output_phy_pages.csv output_logic_pages.csv output_access.csv output_records.csv")
    if ret == 0:
        st.sidebar.success("删除成功")
    else:
        st.sidebar.error("删除失败")

if st.sidebar.button("重置"):
    with open("input_codes.csv", "w") as f:
        f.write("")
    with open("output_phy_pages.csv", "w") as f:
        f.write("")
    with open("output_logic_pages.csv", "w") as f:
        f.write("")
    with open("output_access.csv", "w") as f:
        f.write("")
    with open("output_records.csv", "w") as f:
        f.write("")
    st.sidebar.success("重置成功")

st.write("物理页信息")
output_page_table = pd.read_csv("output_phy_pages.csv", sep=" ", names=["物理页号", "状态", "进程标识"])
st.dataframe(output_page_table)

st.write("逻辑页信息")
output_phy_address = pd.read_csv("output_logic_pages.csv", sep=" ", names=["进程标识", "逻辑页号", "状态", "物理页号", "访问次数", "修改"])
st.dataframe(output_phy_address)

st.write("缺页率")
output_access = pd.read_csv("output_access.csv", sep=" ", names=["进程标识", "访问失败次数", "访问总次数"])
st.dataframe(output_access)

st.write("地址转换记录")
output_records = pd.read_csv("output_records.csv", sep=" ", names=["进程标识", "逻辑地址", "物理地址"])
st.dataframe(output_records)
