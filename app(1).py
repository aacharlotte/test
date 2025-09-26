import streamlit as st

import joblib
import tensorflow as tf

# preprocessor and model loading
preprocessor = joblib.load("/content/drive/MyDrive/preprocessor.pkl")
model = tf.keras.models.load_model("/content/drive/MyDrive/NN_MPI_model1.keras")

st.title("Neural Network MPI Status Prediction App")

st.write("Enter details to predict poverty status for individual")


education_options = [
    "Some schooling but not completed P.1",
    "Completed P.1",
    "Completed P.2",
    "Completed P.3",
    "Completed P.4",
    "Completed P.5",
    "Completed P.6",
    "Completed P.7",
    "Completed J.1",
    "Completed J.2",
    "Completed J.3",
    "Completed S.1",
    "Completed S.2",
    "Completed S.3",
    "Completed S.4",
    "Completed S.5",
    "Completed S.6",
    "Completed post primary/junior specialized training/certificate/diploma",
    "Completed Post secondary Specialized training or diploma",
    "Completed Degree and above"
]

consultation_place = [
    "Gov’t Hospital",
    "Gov’t Health Centre",
    "Outreach Service(Public sector)",
    "Fieldworker/VHT",
    "Other Public Sector",
    "Private Hospital/Clinic",
    "Pharmacy/Drug shop",
    "Private Doctor",
    "Outreach service(Private Medical Sector)",
    "Other private medical sector",
    "Shop",
    "Traditional practitioner",
    "Market",
    "Other"
]

water_source = [
    "Piped water into dwelling",
    "Piped water to the yard",
    "Public taps",
    "Borehole in yard/plot",
    "Public borehole",
    "Protected well/spring",
    "Unprotected well/spring",
    "River/stream/lake",
    "Vendor",
    "Tanker Truck",
    "Gravity Flow Scheme",
    "Rain water",
    "Bottled water",
    "Other (specify)"
]

toilet_type = [
    "Flush Toilet",
    "VIP Latrine",
    "Covered Pit Latrine with a slab",
    "Covered Pit Latrine without a slab",
    "Uncovered Pit Latrine with a slab",
    "Uncovered Pit Latrine without a slab",
    "Ecosan (compost toilet)",
    "No facility/bush/ polythene bags/ bucket/ etc",
    "Other (specify)"
]

energy_source = [
    "Electricity-National grid",
    "Solar Home System",
    "Electricity- Personal Generator",
    "Electricity – Community/ thermal plant",
    "Gas",
    "Biogas",
    "Paraffin lantern",
    "Paraffin Tadooba",
    "Candles",
    "Firewood",
    "Cow dung",
    "Grass (reeds)",
    "Dry Cells",
    "Solar Lantern/Solar Lighting Systemh",
    "Car Battery",
    "Phone torch",
    "Disposable torch",
    "Old car battery",
    "Rechargeable lamp",
    "Other (specify)"
]

roofing_material = [
    "Iron sheets",
    "Tiles",
    "Asbestos",
    "Concrete",
    "Tins",
    "Thatch",
    "Other (specify)"
]

wall_material = [
    "Concrete/ stones",
    "Cement blocks",
    "Burnt stabilized bricks",
    "Unburnt bricks with cement",
    "Unburnt bricks with mud",
    "Wood",
    "Mud and Poles",
    "Tin/Iron sheets",
    "Other (specify)"
]
floor_material = [
    "Earth",
    "Rammed earth",
    "Cement screed",
    "Concrete",
    "Tiles",
    "Brick",
    "Stone",
    "Wood",
    "Other (specify)"
]

employment_type = [
    "Onfarm employment",
    "farm wage employment",
    "nonfarm self employment",
    "nonfarm wage employment",
    "Subsistence onfarm employment"
]



# Inputs (dataset features)

E05 = st.selectbox("Highest grade", education_options)
age = st.number_input("Age", 0, 120, 25)
E03 = st.selectbox("School attence", ["Never attended", "Attended school in the past", "Currently attending school"])
HE02 = st.selectbox("Illness in last 30 days", ["Yes", "No"])
HE07 = st.selectbox("Consultation for illness", ["Yes", "No"])
HE09 = st.selectbox("Place of consultation", consultation_place)
HE11 = st.selectbox("Distance to place of consultation", ["0 to &lt;3kms", "3 to &lt;5kms", "5 to &lt;8kms", "8 or more Kms"])
HC07 = st.selectbox("Househol's source of water", water_source)
HC08a = st.number_input("Time taken to and from the source (minutes)", 0, 120, 25)
HC14 = st.selectbox("Type of toilet", toilet_type)
HC15 = st.selectbox("Is toilet shared ", ["Yes", "No", "N/A"])
hsize = st.number_input("Household size", 0, 25)
HC03 = st.number_input("Number of rooms", 0, 25)
HC18 = st.selectbox("Source of energy", energy_source)
HC04 = st.selectbox("Roofing material", roofing_material)
HC05 = st.selectbox("Wall material", wall_material)
HC06 = st.selectbox("Floor material", floor_material)
HA0318 = st.selectbox("Any household member owns Bicycle", ["Yes,individually", "No", "Yes,jointly with hh member", "Yes, jointly with non-hh member"])
HA0317 = st.selectbox("Any household member owns Motor cycle", ["Yes,individually", "No", "Yes,jointly with hh member", "Yes, jointly with non-hh member"])
HA0316 = st.selectbox("Any household member owns Car", ["Yes,individually", "No", "Yes,jointly with hh member", "Yes, jointly with non-hh member"])
HA0320 = st.selectbox("Any household member owns Boat/Canoe", ["Yes,individually", "No", "Yes,jointly with hh member", "Yes, jointly with non-hh member"])
HA039 = st.selectbox("Any household member owns Radio", ["Yes,individually", "No", "Yes,jointly with hh member", "Yes, jointly with non-hh member"])
HA0311 = st.selectbox("Any household member owns Mobile phone", ["Yes,individually", "No", "Yes,jointly with hh member", "Yes, jointly with non-hh member"])
HA038 = st.selectbox("Any household member owns Television", ["Yes,individually", "No", "Yes,jointly with hh member", "Yes, jointly with non-hh member"])
Working = st.selectbox("Engaged in work ", ["Working", "Not working"])
employment = st.radio("Household head employed", ["Yes", "No"])
employment = 1 if employment == "Yes" else 0
wage_st = st.selectbox("Type of employment ", employment_type)
access_financial_account_any = st.radio("Uses any financial product", ["Yes", "No"])
access_financial_account_any = 1 if access_financial_account_any == "Yes" else 0
digital_reg_financial = st.radio("Uses mobile money", ["Yes", "No"])
digital_reg_financial = 1 if digital_reg_financial == "Yes" else 0
HHhead = st.radio("Household head", ["Yes", "No"])
HHhead = 1 if HHhead == "Yes" else 0



if st.button("Predict MPI Status"):
    # Create dataframe from user input
    data = pd.DataFrame([{

        "Highest grade":E05,
        "Age": age,
        "School attence": E03,
        "Illness in last 30 days": HE02,
        "Consultation for illness": HE07,
        "Place of consultation": HE09,
        "Distance to place of consultation": HE11,
        "Househol's source of water": HC07,
        "Time taken to and from the source (minutes)": HC08a,
        "Type of toilet": HC14,
        "Is toilet shared ": HC15,
        "Household size": hsize,
        "Number of rooms": HC03,
        "Source of energy": HC18,
        "Roofing material": HC04,
        "Wall material": HC05,
        "Floor material": HC06,
        "Any household member owns Bicycle": HA0318,
        "Any household member owns Motor cycle": HA0317,
        "Any household member owns Car": HA0316,
        "Any household member owns Boat/Canoe": HA0320,
        "Any household member owns Radio": HA039,
        "Any household member owns Mobile phone": HA0311,
        "Any household member owns Television": HA038,
        "Engaged in work ": Working,
        "Household head employed": employment,
        "Type of employment ": wage_st,
        "Uses any financial product": access_financial_account_any,
        "Uses mobile money": digital_reg_financial,
        "Household head": HHhead

    }])

    # Apply preprocessing
    X = preprocessor.transform(data)

    # Predict with Keras model
    prediction = model.predict(X)
    st.success(f"Prediction: {prediction}")


