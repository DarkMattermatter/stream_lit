import streamlit as st
import pandas as pd

# Sample data (replace with real data)
data = {
    "Project Name": ["Artemis I", "Mars 2026", "Lunar Gateway", "James Webb Telescope", "Europa Clipper"],
    "Space Agency": ["NASA", "NASA", "ESA", "NASA", "NASA"],
    "Description": [
        "First mission of NASA's Artemis program to return humans to the Moon.",
        "Next rover mission to Mars aimed at searching for signs of life.",
        "Lunar orbit space station as part of the Artemis program.",
        "Space telescope to succeed the Hubble, focusing on infrared astronomy.",
        "Mission to investigate Europa, one of Jupiter's moons, for potential life."
    ],
    "Tentative Timeline": ["2024", "2026", "2028", "2021", "2024"],
    "Tentative Budget": ["$4 Billion", "$2.7 Billion", "$1.5 Billion", "$10 Billion", "$4.25 Billion"],
    "Estimated Completion": ["2024", "2026", "2030", "2023", "2025"],
    "Status": ["In Progress", "Planning", "Development", "Completed", "In Progress"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Streamlit App
def main():
    st.title("Upcoming Space Projects (Next 10 Years)")

    # Filter by Space Agency
    agency = st.selectbox("Select Space Agency", options=["All"] + list(df["Space Agency"].unique()))
    if agency != "All":
        df_filtered = df[df["Space Agency"] == agency]
    else:
        df_filtered = df

    # Display Data
    st.write("### Upcoming Projects")
    st.dataframe(df_filtered)
    
    # Project Details
    st.write("### Project Details")
    for index, row in df_filtered.iterrows():
        with st.expander(row["Project Name"]):
            st.write(f"**Space Agency**: {row['Space Agency']}")
            st.write(f"**Description**: {row['Description']}")
            st.write(f"**Tentative Timeline**: {row['Tentative Timeline']}")
            st.write(f"**Tentative Budget**: {row['Tentative Budget']}")
            st.write(f"**Estimated Completion**: {row['Estimated Completion']}")
            st.write(f"**Status**: {row['Status']}")

if __name__ == "__main__":
    main()
