import streamlit as st
import pickle


from PIL import Image
model = pickle.load(open('lppmodel.sav', 'rb'))

st.title('Laptop Price Prediction')
st.sidebar.header('Laptop Data')
image = Image.open('laptops.jpg')
st.image(image, '')





# Define dictionaries to map category codes to category names
Brand_mapping = {0: 'Lenovo', 1:'ASUS',2: 'HP', 3:'DELL', 4:'RedmiBook', 5:'realme', 6:'acer',
       7: 'MSI', 8: 'APPLE', 9:'Infinix', 10:'SAMSUNG', 11:'Ultimus', 12:'Vaio',
       13:'GIGABYTE', 14:'Nokia',15: 'ALIENWARE'}
RAM_mapping = {0: '8 GB', 1:'16 GB', 2:'4 GB', 3:'32 GB'}
Storage_mapping = {0:'256 GB', 1:'512 GB', 2:'1 TB ', 3:'128 GB', 4:'64 GB', 5:'32 GB', 6:'2 TB'}
Drive_mapping = {0:'SSD', 1:'HDD', 2:'EMMC'}
OS_mapping = {0: 'Windows 11 Home', 1:'Windows 10 Home', 2:'Mac OS ', 3:'Chrome OS',
       4:'DOS', 5:'Windows 10 Inspiron ',6:  'Windows 10 Pro',
       7:'Windows 10 Vostro'}
Warrantytype_mapping = {0: 'Year Onsite Warranty', 1:'Onsite Warranty',
       2:'Display 1 YEAR Warranty',3: 'Year Domestic Warranty',
       4:'Years Onsite Warranty', 5:'Travelers Warranty (ITW)',
       6:'Year Limited Warranty', 7:'Accidental Damage Protection',
       8:'International Travelers Warranty',9: 'Onsite Hardware Service',
      10: 'Carry-In Warranty Term',11: 'Year Carry-in Warranty',
       12:'Content Creation (EU-WE)', 13:'Year Premium Support',
       14:'Legion Ultimate Support', 15:'Year Manufacturer Warranty',
       16:'site Manufacturing warranty', 17:'Date of Purchase',
       18:'Warranty by MSI', 19:'year Manufacturer Warranty', 20:'1 Year ADP',
      21: 'Year Warranty Term', 22:'Term for Gaming',
      23: 'Year International Warranty', 24:'Plus (Includes ADP)',
       25:'Diagnosis - Retail', 26:'Complete Cover Warranty'}
size_mapping = {0: '14.' , 1: '15.6', 2: '13.3', 3: '14.2', 4: '16.' , 5: '16.1', 6: '16.2', 7: '17.3', 8: '14.1', 9: '11.6',10: '15.' ,
       11: '13.' , 12: '13.5', 13: '16.6'}
# Define a function to get user input and encode it
def get_user_input():
    Brand_options = list(Brand_mapping.values())
    Brand = st.sidebar.selectbox('Brand', Brand_options)
    Brand_code = list(Brand_mapping.keys())[list(Brand_mapping.values()).index(Brand)]

    RAM_options = list(RAM_mapping.values())
    RAM = st.sidebar.selectbox('RAM', RAM_options)
    RAM_code = list(RAM_mapping.keys())[list(RAM_mapping.values()).index(RAM)]

    Storage_options  = list(Storage_mapping.values())
    Storage = st.sidebar.selectbox('Storage', Storage_options)
    Storage_code = list(Storage_mapping.keys())[list(Storage_mapping.values()).index(Storage)]

    Drive_options = list(Drive_mapping.values())
    Drive = st.sidebar.selectbox('Drive', Drive_options)
    Drive_code = list(Drive_mapping.keys())[list(Drive_mapping.values()).index(Drive)]

    OS_options = list(OS_mapping.values())
    OS = st.sidebar.selectbox('OS', OS_options)
    OS_code = list(OS_mapping.keys())[list(OS_mapping.values()).index(OS)]

    Warrantytype_options = list(Warrantytype_mapping.values())
    Warrantytype = st.sidebar.selectbox('Warrantytype', Warrantytype_options)
    Warrantytype_code = list(Warrantytype_mapping.keys())[list(Warrantytype_mapping.values()).index(Warrantytype)]

    size_options = list(size_mapping.values())
    size = st.sidebar.selectbox('Size', size_options)
    size_code = list(size_mapping.keys())[list(size_mapping.values()).index(size)]
    
    Rating = st.sidebar.slider('Rating', 4.0, 5.0, 4.0)
    
    categorical_data = {'Brand': Brand_code,'RAM':RAM_code,'Storage': Storage_code,'Drive':Drive_code,'OS':OS_code,'Warranty type':Warrantytype_code,'size': size_code}
    numerical_data = {'Rating': Rating}
    features = {**categorical_data, **numerical_data}
    return features

# Get user input and make prediction
user_input = get_user_input()
prediction = model.predict([list(user_input.values())])[0]

# Display the prediction
st.write('The predicted price is Rupees', prediction.round())