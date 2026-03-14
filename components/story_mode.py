import streamlit as st
import numpy as np
import plotly.express as px


def show_story(data, lat, lon, variable):

    # st.subheader("📖 Climate Story Insights")

    avg = np.mean(data)
    mx = np.max(data)
    mn = np.min(data)

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric("Average", round(float(avg),2))

    with col2:
        st.metric("Maximum", round(float(mx),2))

    with col3:
        st.metric("Minimum", round(float(mn),2))

    st.divider()

    st.markdown("### 🌍 Key Insights")

    if avg > 0:
        st.write("Climate values indicate increasing trend in selected variable.")

    if mx > avg*1.5:
        st.write("Possible extreme climate event detected.")

    if mn < avg*0.5:
        st.write("Unusually low values detected in dataset.")

    st.divider()

    st.markdown("### 📊 Distribution")

    fig = px.histogram(
        data.flatten(),
        nbins=40,
        title="Climate Value Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        This story view highlights climate patterns and anomalies
        within the dataset to help understand climate trends.
        """
    )
