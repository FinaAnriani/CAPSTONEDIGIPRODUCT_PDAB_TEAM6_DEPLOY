import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# from sklearn.preprocessing import MinMaxScaler


def enter1():
    st.write("<br>", unsafe_allow_html=True)

def enter2():
    st.write("<br><br>", unsafe_allow_html=True)

def main_title():
    st.title("❝Analisis Data Starbucks untuk Memprediksi Retensi Pelanggan (Starbucks Customers Survey)❞")

# data awal
def data():
    return pd.read_csv('dataSB.csv')

# data clean
def data2():
    return pd.read_csv('Data Cleaned SB.csv')

def visualisasi1(df):
    df_temp = df.copy()
    df_temp['age'] = df_temp['age'].replace({0: "<20", 1: "20-29", 2: "30-39", 3: ">40"})
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data=df_temp, x='age', bins=4, kde=False, color='pink', ax=ax)
    ax.set_title('Distribusi Umur')
    ax.set_xlabel('Umur')
    ax.set_ylabel('Jumlah')
    st.pyplot(fig)

def visualisasi2(df):
    df_temp = df.copy()
    df_temp['gender'] = df_temp['gender'].replace({0: 'Male', 1: 'Female'})
    df_temp['visitNo'] = df_temp['visitNo'].replace({0: 'Daily', 1: 'Weekly', 2: 'Monthly', 3: 'Never'})
    visitNo_gender_counts = df_temp.groupby(['visitNo', 'gender']).size().unstack(fill_value=0)
    visitNo_gender_counts.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'])
    plt.title('Perbandingan Frekuensi Kunjungan Berdasarkan Gender')
    plt.xlabel('Frekuensi Kunjungan')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=45)
    plt.legend(title='Gender')
    st.pyplot() 

def visualisasi3(df):
    df_temp = df.copy()
    df_temp['loyal'] = df_temp['loyal'].replace({0: 'Loyal', 1: 'Tidak Loyal'})
    loyal_counts = df_temp['loyal'].value_counts()

    # Mengatur warna yang diinginkan
    custom_colors = ['green', 'lightgrey']

    plt.figure(figsize=(6, 6))
    plt.pie(loyal_counts, labels=loyal_counts.index, autopct='%1.1f%%', startangle=90, colors=custom_colors)
    plt.title('Komposisi Loyalitas Pelanggan')
    plt.axis('equal')
    st.pyplot()

def visualisasi4(df):
    # Relationship (Hubungan)
    df_temp = df.copy()
    df_temp['gender'] = df_temp['gender'].replace({0: 'Male', 1: 'Female'})
    df_temp['visitNo'] = df_temp['visitNo'].replace({0: 'Daily', 1: 'Weekly', 2: 'Monthly', 3: 'Never'})
    df_temp['spendPurchase'] = df_temp['spendPurchase'].replace({0: 'Zero', 1: '<RM20', 2: 'RM20 - RM40', 3: '>RM40'})
    df_temp['loyal'] = df_temp['loyal'].replace({0: 'Loyal', 1: 'Tidak Loyal'})
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        x='loyal',
        y='spendPurchase',
        hue='gender',
        palette='Set3',
        data=df_temp,
        ax=ax)
    ax.set_title('Hubungan Loyalitas Pelanggan dengan Total Pengeluaran')
    ax.set_xlabel('Loyalitas Pelanggan')
    ax.set_ylabel('Total Pengeluaran (RM)')
    ax.set_xticks([0, 1])  # Label untuk sumbu x
    ax.set_xticklabels(['Loyal', 'Tidak Loyal'])  
    ax.set_yticks([0, 1, 2, 3])  # Label untuk sumbu y
    ax.set_yticklabels(['Zero', '<RM20', 'RM20 - RM40', '>RM40'])  
    st.pyplot(fig)

def visualisasi5(df):
    # Composition (Komposisi)
    # lebih banyak pelanggan perempuan atau laki-laki?
    df_temp = df.copy()
    df_temp['gender'] = df_temp['gender'].replace({0: "male", 1: "female"})
    Transportation_counts = df_temp['gender'].value_counts()

    colors = ['skyblue', 'gray']
    fig, ax = plt.subplots()
    Transportation_counts.plot.pie(autopct='%1.1f%%', startangle=140, colors=colors, ax=ax)
    ax.set_ylabel('')
    plt.title('Komposisi Pelanggan Berdasarkan Gender')
    plt.axis('equal')
    st.pyplot(fig)

def visualisasi6(df):
    # Composition (Komposisi)
    # dari keseluruhan pelanggan, lebih banyak dari kalangan apa?

    status_labels = {
        0: 'Student',
        1: 'Self-Employed',
        2: 'Employed',
        3: 'Housewife'
    }
    status_counts = df['status'].value_counts()

    # Buat pie chart
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(status_counts, labels=[status_labels[i] for i in status_counts.index], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral', 'pink'])
    ax.set_title('Pie Chart Status Pelanggan', fontsize=16)
    ax.axis('equal')  # Agar pie chart menjadi lingkaran
    ax.legend(title='Status', loc='upper right')
    st.pyplot(fig)  # Menggunakan st.pyplot() untuk menampilkan plot di Streamlit

def visualisasi7(df):
    # Composition (Komposisi)
    # Seberapa sering pelanggan starbucks mengunjungi starbucks?

    visit_labels = {
        0: 'Daily',
        1: 'Weekly',
        2: 'Monthly',
        3: 'Never'}

    visit_counts = df['visitNo'].value_counts()

    # Buat pie chart dengan label yang sudah diganti
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(visit_counts, labels=[visit_labels[i] for i in visit_counts.index], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
    ax.set_title('Pie Chart Frekuensi Kunjungan', fontsize=16, color='navy')
    ax.axis('equal')
    ax.legend(title='Frekuensi', loc='upper right')
    st.pyplot(fig)

def visualisasi8(df):
    # Composition (Komposisi)
    # Berapa banyak pengeluaran pelanggan ketika mengunjungi starbucks?

    spend_labels = {
        0: 'Zero',
        1: 'Less than RM20',
        2: 'RM20 to RM40',
        3: 'More than RM40'
    }
    spend_counts = df['spendPurchase'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(spend_counts, labels=[spend_labels[i] for i in spend_counts.index], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
    ax.set_title('Pie Chart Pengeluaran Pelanggan', fontsize=16, color='navy')
    ax.axis('equal')
    ax.legend(title='Pengeluaran', loc='upper right')
    st.pyplot(fig)

def visualisasi9(df):
    df_temp = df.copy()
    df_temp['age'] = df_temp['age'].replace({0: "<20", 1: "20-29", 2: "30-39", 3: ">40"})
    df_temp['loyal'] = df_temp['loyal'].replace({0: 'Loyal', 1: 'Tidak Loyal'})
    
    # Mengatur palet warna yang diinginkan
    custom_palette = {'Loyal': 'green', 'Tidak Loyal': 'lightgrey'}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='age', hue='loyal', palette=custom_palette, data=df_temp, ax=ax)
    ax.set_title('Perbandingan Loyalitas Berdasarkan Usia')
    ax.set_xlabel('Usia')
    ax.set_ylabel('Jumlah')
    
    st.pyplot(fig)

def visualisasi10(df):
    # Comparison (Perbandingan)

    df_new = df.copy()
    df_new['gender'] = df_new['gender'].replace({0: 'male', 1: 'female'})
    df_new['loyal'] = df_new['loyal'].replace({0: 'iya', 1: 'tidak'})
    
    # Mengatur palet warna yang diinginkan
    custom_palette = {'iya': 'green', 'tidak': 'lightgrey'}

    fig, ax = plt.subplots()
    sns.countplot(x="gender",
                  hue="loyal",
                  palette=custom_palette,
                  data=df_new,
                  order=['male', 'female'],
                  hue_order=['iya', 'tidak'])

    plt.title('Loyalty by gender')
    plt.xlabel('gender')
    plt.ylabel('Count')
    plt.legend(title='Loyal', bbox_to_anchor=(1, 1))
    st.pyplot(fig)

def visualisasi11(df):
    # Comparison (Perbandingan)
    plt.figure(figsize=(10, 6))
    sns.countplot(x='age', hue='loyal', palette='vlag', data=df)
    plt.title('Perbandingan Loyalitas Berdasarkan Usia')
    plt.xlabel('Usia')
    plt.ylabel('Jumlah')
    plt.legend(title='Loyal')
    st.pyplot()

def visualisasi12(df):
    # Relationship (Hubungan)
    # apakah pelanggan yang mempunyai membership sudah pasti loyal?
    df_new = df.copy()
    df_new['membershipCard'] = df_new['membershipCard'].replace({0: 'punya', 1: 'tidak'})
    df_new['loyal'] = df_new['loyal'].replace({0: 'iya', 1: 'tidak'})

    # Mengatur palet warna yang diinginkan
    custom_palette = {'iya': 'green', 'tidak': 'lightgrey'}

    fig, ax = plt.subplots()
    sns.countplot(x="membershipCard",
                  hue="loyal",
                  palette=custom_palette,
                  data=df_new,
                  order=['punya', 'tidak'],
                  hue_order=['iya', 'tidak'])

    plt.title('Count of Membership Card by Loyal')
    plt.xlabel('Membership Card')
    plt.ylabel('Count')
    plt.legend(title='Loyal', bbox_to_anchor=(1, 1))
    st.pyplot(fig)

def visualisasi13(df):
    # Composition (Komposisi)
    plt.figure(figsize=(8, 8))
    df['membershipCard'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'grey'])
    plt.title('Komposisi Kepemilikan Kartu Keanggotaan')
    plt.ylabel('')
    st.pyplot()

def relationship(df2):
    df2_corr = df2.corr(numeric_only=True)
    fig = px.imshow(df2_corr)
    st.plotly_chart(fig)




df = data()
df2 = data()
def main():
    main_title()
    st.subheader('Subheader')
    st.caption("Caption")

    st.header('COMPARISON')
    st.caption('visualisasi 9')
    visualisasi9(df)

    st.caption('visualisasi 10')
    visualisasi10(df)

    st.caption('visualisasi 11')
    visualisasi11(df)

    st.caption('visualisasi 12')
    visualisasi12(df)




    st.header('COMPOSITION')
    st.caption('Visualisasi 2')
    visualisasi2(df)

    st.caption('visualisasi 3')
    visualisasi3(df)

    st.caption('visualisasi 5')
    visualisasi5(df)

    st.caption('visualisasi 6')
    visualisasi6(df)

    st.caption('visualisasi 7')
    visualisasi7(df)

    st.caption('visualisasi 8')
    visualisasi8(df)

    st.caption('visualisasi 13')
    visualisasi13(df)



    st.header('DISTRIBUTION')
    st.caption('visualisasi 4')
    visualisasi4(df)



    st.header('RELATIONSHIP')
    relationship(df2)



    # distri atau relation
    st.caption('Visualisasi 1, ini gatau masuk mana')
    visualisasi1(df)  


    

    

    

    

    

    

    

    
    




if __name__ == "__main__":
    st.set_option('deprecation.showPyplotGlobalUse', False)
    main()

