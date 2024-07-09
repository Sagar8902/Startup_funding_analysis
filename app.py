import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="startup_analysis")

df = pd.read_csv("startup_cleaned-1.csv")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month

def load_overall_analysis():
    # st.title("Overall Analysis")

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        # total funding
        total = round(df["amount"].sum())
        st.metric("Total Funding",str(total) + " Cr")

    with col2:
        # max funding
        max = round(df.groupby("startup")["amount"].sum().sort_values(ascending=False).head(1).values[0])
        st.metric("Max Funding", str(max) + " Cr")

    with col3:
        # avg funding
        avg = round(df.groupby("startup")["amount"].sum().mean())
        st.metric("Average Funding", str(avg) + " Cr")

    with col4:
        # mumber of startup
        number = df["startup"].nunique()
        st.metric("Total Funded Startup",number)

    col01,col02 = st.columns(2)
    # MoM total funding
    with col01:
        temp_df = df.groupby((df["year"].astype(str) + "-" + df["month"].astype(str)))["startup"].count().reset_index()

        st.subheader("MoM funded startups")
        fig4, ax4 = plt.subplots()
        ax4.plot(temp_df["index"], temp_df["startup"])
        st.pyplot(fig4)

    # MoM no. funding
    with col02:
        temp_df = df.groupby((df["year"].astype(str) + "-" + df["month"].astype(str)))["amount"].sum().reset_index()

        st.subheader("MoM startups funding")
        fig5, ax5 = plt.subplots()
        ax5.plot(temp_df["index"], temp_df["amount"])
        st.pyplot(fig5)

def load_startup_detail(startup):
    st.title("Startup Analysis")

    col11, col12 = st.columns(2)

    # total funding
    with col11:
        total_funding = round(df[df["startup"].str.lower().str.contains(startup)]["amount"].sum())
        st.metric("Total Funding",str(total_funding) + " Cr")

    with col12:
        no_of_round = df[df["startup"].str.lower().str.contains(startup)]["round"].count()
        st.metric("Total Rounds",no_of_round)

    col001,col002= st.columns(2)
    # funding by year
    with col001:
        funding_year = df[df["startup"].str.lower().str.contains(startup)][["year", "amount"]]
        st.subheader("funding by year")
        fig6, ax6 = plt.subplots()
        ax6.bar(funding_year["year"], funding_year["amount"])
        st.pyplot(fig6)

    with col002:
        funding_round = df[df["startup"].str.lower().str.contains(startup)][["round","amount"]]
        st.subheader("funding by round")
        fig7, ax7 = plt.subplots()
        ax7.pie(funding_round["amount"],labels=funding_round["round"], autopct="%0.01f%%")
        st.pyplot(fig7)


    funding_investor = df[df["startup"].str.lower().str.contains(startup)][["investors","amount"]]
    st.subheader("funding by investor")
    fig8, ax8 = plt.subplots()
    ax8.pie(funding_investor["amount"],labels=funding_investor["investors"], autopct="%0.01f%%")
    st.pyplot(fig8)

def load_investors_details(investor):
    st.title("Investor Analysis")

    col101,col102 = st.columns(2)
    # total funding by investor
    with col101:
        investor_funding = round(df[df["investors"].str.lower().str.contains(investor)]["amount"].sum())
        st.metric("Total Funding",str(investor_funding) + " Cr")

    with col102:
        funded_startup = df[df["investors"].str.lower().str.contains(investor)]["startup"].count()
        st.metric("Funded Startups",funded_startup)

    # recent investments
    recent_top_5 = df[df["investors"].str.lower().str.contains(investor)].head()[
        ["date", "startup", "vertical", "city", "round", "amount"]]
    st.subheader("Most Recent Investments")
    st.dataframe(recent_top_5)

    col1, col2= st.columns(2)
    with col1:
        # biggest investments
        total_investment = df[df["investors"].str.lower().str.contains(investor)].groupby("startup")["amount"].sum().sort_values(
            ascending=False).head()
        st.subheader("Major Investment")
        fig, ax = plt.subplots()
        ax.bar(total_investment.index, total_investment.values)
        # ax.bar_label(fig)
        st.pyplot(fig)

    with col2:
        # investment by round
        total_round = df[df["investors"].str.lower().str.contains(investor)].groupby("round")["amount"].sum().sort_values(
            ascending=False).head()

        st.subheader("Investment by rounds")
        fig2, ax2 = plt.subplots()
        ax2.pie(total_round, labels=total_round.index, autopct="%0.01f%%")
        st.pyplot(fig2)


    # YoY investment
    year = df["year"]
    investment = df[df["investors"].str.lower().str.contains("investors")].groupby(df["year"])["amount"].sum()

    st.subheader("YoY Investment")
    fig3, ax3 = plt.subplots()
    ax3.plot(investment.index,investment.values)
    st.pyplot(fig3)


# st.title("startup funding")
st.sidebar.title("Indian startup ecosystem 2015-2019")
select = st.sidebar.selectbox("select anyone", ["Overall Analysis", "Startup Analysis", "Investor Analysis"])

if select == "Overall Analysis":
    st.title("Overall Analysis")
    # st.sidebar.button("find overall analysis")
    # if btn0:
    load_overall_analysis()

elif select == "Startup Analysis":
    # st.title("Startup Analysis")
    select_startup = st.sidebar.selectbox("list of startup", sorted(set(df["startup"].str.lower().unique().tolist())))
    btn1 = st.sidebar.button("find startup detail")
    if btn1:
        load_startup_detail(select_startup)


elif select == "Investor Analysis":
    # st.title("Investor Analysis")
    select_investor = st.sidebar.selectbox("list of investor", sorted(set(df["investors"].str.lower().str.split(",").sum())))
    btn2 = st.sidebar.button("find investor detail")
    if btn2:
        load_investors_details(select_investor)
