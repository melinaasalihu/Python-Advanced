import streamlit as st

import requests

import pandas as pd


API_URL = "http://127.0.0.1:8000"


# =====================================
# PAGE SETTINGS
# =====================================

st.set_page_config(

    page_title="TripQuest",

    page_icon="✈️",

    layout="wide"
)


# =====================================
# STYLE
# =====================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title {
    font-size: 50px;
    font-weight: bold;
    color: #2563eb;
}

.subtitle {
    color: #64748b;
    font-size: 20px;
}

</style>
""", unsafe_allow_html=True)


# =====================================
# API FUNCTIONS
# =====================================

def get_destinations():

    try:

        response = requests.get(
            f"{API_URL}/destinations/",
            timeout=5
        )

        if response.status_code == 200:

            return response.json()

        return []

    except requests.RequestException:

        st.error(
            "❌ Could not connect to API."
        )

        return []


def create_destination(data):

    try:

        return requests.post(
            f"{API_URL}/destinations/",
            json=data,
            timeout=15
        )

    except requests.RequestException:

        return None


def update_destination(
    destination_id,
    data
):

    try:

        return requests.put(
            f"{API_URL}/destinations/"
            f"{destination_id}",
            json=data,
            timeout=15
        )

    except requests.RequestException:

        return None


def delete_destination(
    destination_id
):

    try:

        return requests.delete(
            f"{API_URL}/destinations/"
            f"{destination_id}",
            timeout=10
        )

    except requests.RequestException:

        return None


# =====================================
# HEADER
# =====================================

st.markdown(
    '<div class="title">'
    '✈️ TripQuest'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your personal travel bucket list 🌍'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =====================================
# GET DATA
# =====================================

destinations = get_destinations()


# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("✈️ TripQuest")

page = st.sidebar.radio(

    "Choose page:",

    [
        "🏠 Dashboard",
        "🌍 My Destinations",
        "➕ Add Destination",
        "✏️ Edit Destination",
        "🗑️ Delete Destination"
    ]
)


# =====================================
# DASHBOARD
# =====================================

if page == "🏠 Dashboard":

    st.header("🌍 Travel Dashboard")

    total = len(destinations)

    visited = sum(
        1
        for x in destinations
        if x["status"] == "Visited"
    )

    planned = sum(
        1
        for x in destinations
        if x["status"] == "Planned"
    )

    wishlist = sum(
        1
        for x in destinations
        if x["status"] == "Wishlist"
    )

    total_budget = sum(
        x["budget"]
        for x in destinations
    )


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "🌍 Destinations",
        total
    )

    col2.metric(
        "✅ Visited",
        visited
    )

    col3.metric(
        "📅 Planned",
        planned
    )

    col4.metric(
        "💰 Budget",
        f"€{total_budget:,.0f}"
    )


    st.divider()


    if not destinations:

        st.info(
            "Your bucket list is empty. "
            "Add your first destination!"
        )

    else:

        df = pd.DataFrame(
            destinations
        )


        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "📊 Destinations by Status"
            )

            status_data = (
                df["status"]
                .value_counts()
            )

            st.bar_chart(
                status_data
            )


        with col2:

            st.subheader(
                "⭐ Destinations by Priority"
            )

            priority_data = (
                df["priority"]
                .value_counts()
            )

            st.bar_chart(
                priority_data
            )


        st.subheader(
            "💰 Travel Budget"
        )

        st.dataframe(

            df[
                [
                    "country",
                    "city",
                    "budget",
                    "status",
                    "priority"
                ]
            ],

            use_container_width=True
        )


# =====================================
# MY DESTINATIONS
# =====================================

elif page == "🌍 My Destinations":

    st.header(
        "🌍 My Travel Bucket List"
    )


    if not destinations:

        st.info(
            "No destinations yet."
        )

    else:

        search = st.text_input(
            "🔍 Search by country or city"
        )


        status_filter = st.selectbox(

            "Filter by status",

            [
                "All",
                "Wishlist",
                "Planned",
                "Visited"
            ]
        )


        filtered = destinations


        if search:

            filtered = [

                x
                for x in filtered

                if search.lower()
                in (
                    x["country"]
                    + " "
                    + x["city"]
                ).lower()
            ]


        if status_filter != "All":

            filtered = [

                x
                for x in filtered

                if x["status"]
                == status_filter
            ]


        for destination in filtered:

            with st.container():

                col1, col2, col3 = st.columns(
                    [1, 5, 2]
                )


                with col1:

                    if destination["flag"]:

                        st.image(
                            destination["flag"],
                            width=80
                        )


                with col2:

                    st.subheader(
                        f"{destination['city']}, "
                        f"{destination['country']}"
                    )

                    st.write(
                        f"🏛️ Capital: "
                        f"{destination['capital'] or 'Unknown'}"
                    )

                    st.write(
                        f"🌎 Region: "
                        f"{destination['region'] or 'Unknown'}"
                    )

                    st.write(
                        f"💰 Currency: "
                        f"{destination['currency'] or 'Unknown'}"
                    )

                    st.write(
                        f"📝 "
                        f"{destination['notes'] or 'No notes'}"
                    )


                with col3:

                    st.write(
                        f"**Status:** "
                        f"{destination['status']}"
                    )

                    st.write(
                        f"**Priority:** "
                        f"{destination['priority']}"
                    )

                    st.write(
                        f"**Budget:** "
                        f"€{destination['budget']:,.0f}"
                    )


                st.divider()


# =====================================
# ADD DESTINATION
# =====================================

elif page == "➕ Add Destination":

    st.header(
        "➕ Add New Destination"
    )


    with st.form(
        "add_form"
    ):

        country = st.text_input(
            "🌍 Country",
            placeholder="Example: Japan"
        )

        city = st.text_input(
            "🏙️ City",
            placeholder="Example: Tokyo"
        )

        budget = st.number_input(
            "💰 Estimated Budget (€)",
            min_value=0.0,
            step=50.0
        )

        priority = st.selectbox(

            "⭐ Priority",

            [
                "Low",
                "Medium",
                "High"
            ]
        )

        status = st.selectbox(

            "📌 Status",

            [
                "Wishlist",
                "Planned",
                "Visited"
            ]
        )

        travel_date = st.date_input(
            "📅 Travel Date"
        )

        notes = st.text_area(
            "📝 Notes",
            placeholder=
            "What do you want to do there?"
        )


        submit = st.form_submit_button(
            "🚀 Add Destination"
        )


        if submit:

            if not country.strip():

                st.error(
                    "Country is required."
                )

            elif not city.strip():

                st.error(
                    "City is required."
                )

            else:

                data = {

                    "country": country,

                    "city": city,

                    "budget": budget,

                    "priority": priority,

                    "status": status,

                    "travel_date":
                        str(travel_date),

                    "notes": notes
                }


                response = create_destination(
                    data
                )


                if response:

                    if response.status_code == 200:

                        st.success(
                            "🎉 Destination added!"
                        )

                        st.balloons()

                        st.rerun()

                    else:

                        st.error(
                            response.text
                        )


# =====================================
# EDIT DESTINATION
# =====================================

elif page == "✏️ Edit Destination":

    st.header(
        "✏️ Edit Destination"
    )


    if not destinations:

        st.info(
            "No destinations available."
        )

    else:

        options = {

            f"{x['id']} - "
            f"{x['city']}, "
            f"{x['country']}":
            x

            for x in destinations
        }


        selected = st.selectbox(
            "Choose destination",
            list(options.keys())
        )


        destination = options[
            selected
        ]


        with st.form(
            "edit_form"
        ):

            country = st.text_input(
                "🌍 Country",
                value=destination["country"]
            )

            city = st.text_input(
                "🏙️ City",
                value=destination["city"]
            )

            budget = st.number_input(
                "💰 Budget (€)",
                min_value=0.0,
                value=float(
                    destination["budget"]
                ),
                step=50.0
            )


            priorities = [
                "Low",
                "Medium",
                "High"
            ]

            priority = st.selectbox(

                "⭐ Priority",

                priorities,

                index=priorities.index(
                    destination["priority"]
                )
            )


            statuses = [
                "Wishlist",
                "Planned",
                "Visited"
            ]

            status = st.selectbox(

                "📌 Status",

                statuses,

                index=statuses.index(
                    destination["status"]
                )
            )


            travel_date = st.text_input(

                "📅 Travel Date",

                value=
                destination["travel_date"]
                or ""
            )


            notes = st.text_area(

                "📝 Notes",

                value=
                destination["notes"]
                or ""
            )


            submit = st.form_submit_button(
                "💾 Save Changes"
            )


            if submit:

                data = {

                    "country": country,

                    "city": city,

                    "budget": budget,

                    "priority": priority,

                    "status": status,

                    "travel_date":
                        travel_date,

                    "notes": notes
                }


                response = update_destination(

                    destination["id"],

                    data
                )


                if response:

                    if response.status_code == 200:

                        st.success(
                            "✅ Destination updated!"
                        )

                        st.rerun()

                    else:

                        st.error(
                            response.text
                        )


# =====================================
# DELETE DESTINATION
# =====================================

elif page == "🗑️ Delete Destination":

    st.header(
        "🗑️ Delete Destination"
    )


    if not destinations:

        st.info(
            "No destinations available."
        )

    else:

        options = {

            f"{x['id']} - "
            f"{x['city']}, "
            f"{x['country']}":
            x["id"]

            for x in destinations
        }


        selected = st.selectbox(

            "Choose destination",

            list(options.keys())
        )


        destination_id = options[
            selected
        ]


        st.warning(
            "⚠️ This action cannot be undone."
        )


        confirm = st.checkbox(
            "I confirm that I want to delete it."
        )


        if st.button(
            "🗑️ Delete Destination",
            type="primary"
        ):

            if not confirm:

                st.error(
                    "Please confirm deletion."
                )

            else:

                response = delete_destination(
                    destination_id
                )


                if response:

                    if response.status_code == 200:

                        st.success(
                            "🗑️ Destination deleted!"
                        )

                        st.rerun()

                    else:

                        st.error(
                            response.text
                        )