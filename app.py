import streamlit as st

st.set_page_config(page_title="Renal Dose Calculator")

st.title("💊 Renal Dose Calculator")

age = st.number_input("Age (years)", min_value=1)

weight = st.number_input("Weight (kg)", min_value=1.0)

scr = st.number_input(
    "Serum Creatinine (mg/dL)",
    min_value=0.1,
    step=0.1
)

sex = st.selectbox(
    "Sex",
    ["Male","Female"]
)

drug = st.selectbox(
    "Drug",
    [
        "Meropenem",
        "Piperacillin-Tazobactam",
        "Levofloxacin"
    ]
)

if st.button("Calculate"):

    crcl = ((140-age)*weight)/(72*scr)

    if sex=="Female":
        crcl *= 0.85

    st.success(
        f"Creatinine Clearance = {crcl:.1f} mL/min"
    )

    if drug=="Meropenem":

        if crcl >= 50:
            dose="1 g q8h"

        elif crcl >=25:
            dose="1 g q12h"

        elif crcl >=10:
            dose="500 mg q12h"

        else:
            dose="500 mg q24h"

        st.info(f"Recommended Dose: {dose}")

    elif drug=="Levofloxacin":

        if crcl >50:
            dose="500 mg q24h"

        elif crcl>=20:
            dose="500 mg initial then 250 mg q24h"

        else:
            dose="500 mg initial then 250 mg q48h"

        st.info(f"Recommended Dose: {dose}")
