import streamlit as st
import pandas as pd
import os

# App title
st.title("Gemini Code Contact Book")

# CSV file path
CSV_FILE = "contacts.csv"

# --- FUNCTIONS ---
def load_data():
    """Load contacts from CSV or create a new file if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        # Create an empty DataFrame with the correct columns
        df = pd.DataFrame(columns=["Name", "Phone", "Email", "Address"])
        df.to_csv(CSV_FILE, index=False)
        return df
    else:
        # Load the CSV, ensuring that empty files are handled correctly
        try:
            return pd.read_csv(CSV_FILE)
        except pd.errors.EmptyDataError:
            return pd.DataFrame(columns=["Name", "Phone", "Email", "Address"])

def save_data(df):
    """Save the DataFrame to the CSV file."""
    df.to_csv(CSV_FILE, index=False)
    st.rerun() # Rerun the app to reflect changes immediately

# Load initial data
contacts_df = load_data()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Navigation")
page = st.sidebar.radio("Choose an action", ["View All Contacts", "Add Contact", "Search Contacts", "Delete Contact"])

# --- PAGE IMPLEMENTATIONS ---

# 1. View All Contacts
if page == "View All Contacts":
    st.header("All Contacts")
    if contacts_df.empty:
        st.info("No contacts found. Add a new contact using the sidebar menu.")
    else:
        # Display the DataFrame as a sortable table
        st.dataframe(contacts_df, use_container_width=True)

# 2. Add Contact
elif page == "Add Contact":
    st.header("Add a New Contact")
    
    with st.form("add_contact_form", clear_on_submit=True):
        name = st.text_input("Name", placeholder="Enter full name")
        phone = st.text_input("Phone", placeholder="Enter phone number")
        email = st.text_input("Email", placeholder="Enter email address")
        address = st.text_area("Address", placeholder="Enter full address")
        
        submitted = st.form_submit_button("Add Contact")

        if submitted:
            # Basic validation
            if not name or not phone:
                st.error("Name and Phone are required fields.")
            else:
                # Create a new contact as a DataFrame
                new_contact = pd.DataFrame([{
                    "Name": name,
                    "Phone": phone,
                    "Email": email,
                    "Address": address
                }])
                
                # Append the new contact
                updated_df = pd.concat([contacts_df, new_contact], ignore_index=True)
                
                # Save and rerun
                save_data(updated_df)
                st.success(f"Contact '{name}' added successfully!")

# 3. Search Contacts
elif page == "Search Contacts":
    st.header("Search for Contacts")
    
    search_term = st.text_input("Search by Name, Phone, or Email", "")
    
    if search_term:
        # Filter the DataFrame (case-insensitive search)
        search_results = contacts_df[
            contacts_df["Name"].str.contains(search_term, case=False, na=False) |
            contacts_df["Phone"].str.contains(search_term, case=False, na=False) |
            contacts_df["Email"].str.contains(search_term, case=False, na=False)
        ]
        
        st.subheader("Search Results")
        if search_results.empty:
            st.warning(f"No contacts found matching '{search_term}'.")
        else:
            st.dataframe(search_results, use_container_width=True)
    else:
        st.info("Enter a search term to find contacts.")

# 4. Delete Contact
elif page == "Delete Contact":
    st.header("Delete a Contact")

    if contacts_df.empty:
        st.warning("No contacts to delete.")
    else:
        # Create a list of names for the selectbox
        contact_names = contacts_df["Name"].tolist()
        
        # Use a form for the delete operation
        with st.form("delete_contact_form"):
            contact_to_delete = st.selectbox("Select a contact to delete", options=contact_names)
            
            # Add a confirmation checkbox for safety
            confirm_delete = st.checkbox(f"I am sure I want to delete '{contact_to_delete}'.")
            
            submit_button = st.form_submit_button("Delete Contact")

            if submit_button:
                if confirm_delete:
                    # Find the index of the contact to delete
                    # Using .loc to filter and get the index
                    updated_df = contacts_df[contacts_df["Name"] != contact_to_delete]
                    
                    # Save the updated DataFrame
                    save_data(updated_df)
                    st.success(f"Contact '{contact_to_delete}' has been deleted.")
                else:
                    st.error("Please confirm the deletion by checking the box.")
