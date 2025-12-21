import streamlit as st
import json
import os
from datetime import datetime

NOTES_FILE = 'notes.json'

def load_notes():
    """Loads notes from the JSON file."""
    if not os.path.exists(NOTES_FILE):
        return {}
    try:
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_notes(notes):
    """Saves notes to the JSON file."""
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=4)

def main():
    """Main function to run the Streamlit app."""
    st.title("Day_32 Notes App")

    notes = load_notes()

    st.sidebar.title("Menu")
    menu_choice = st.sidebar.radio("Go to", ["Add Note", "View Notes", "Edit Note", "Delete Note"])

    if menu_choice == "Add Note":
        st.header("Add a New Note")
        title = st.text_input("Title")
        content = st.text_area("Content")

        if st.button("Add Note"):
            if title and content:
                note_id = str(int(max(notes.keys())) + 1) if notes else "1"
                notes[note_id] = {
                    "title": title,
                    "content": content,
                    "creation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                save_notes(notes)
                st.success("Note added successfully!")
            else:
                st.warning("Please enter a title and content for the note.")

    elif menu_choice == "View Notes":
        st.header("Your Notes")
        if not notes:
            st.info("No notes found. Add a new note to get started.")
        else:
            for note_id, note_data in sorted(notes.items(), key=lambda item: item[1]['creation_date'], reverse=True):
                with st.expander(f"{note_data['title']} (Created: {note_data['creation_date']})"):
                    st.write(note_data['content'])

    elif menu_choice == "Edit Note":
        st.header("Edit a Note")
        if not notes:
            st.info("No notes to edit.")
            return

        note_to_edit_id = st.selectbox("Select a note to edit", options=list(notes.keys()), format_func=lambda note_id: notes[note_id]['title'])

        if note_to_edit_id:
            note_data = notes[note_to_edit_id]
            new_title = st.text_input("New Title", value=note_data['title'])
            new_content = st.text_area("New Content", value=note_data['content'])

            if st.button("Update Note"):
                if new_title and new_content:
                    notes[note_to_edit_id]['title'] = new_title
                    notes[note_to_edit_id]['content'] = new_content
                    save_notes(notes)
                    st.success("Note updated successfully!")
                    st.experimental_rerun()
                else:
                    st.warning("Title and content cannot be empty.")


    elif menu_choice == "Delete Note":
        st.header("Delete a Note")
        if not notes:
            st.info("No notes to delete.")
            return

        note_to_delete_id = st.selectbox("Select a note to delete", options=list(notes.keys()), format_func=lambda note_id: notes[note_id]['title'])

        if note_to_delete_id:
            st.warning(f"Are you sure you want to delete the note: **{notes[note_to_delete_id]['title']}**?")
            if st.button("Delete Note"):
                del notes[note_to_delete_id]
                save_notes(notes)
                st.success("Note deleted successfully!")
                st.experimental_rerun()


if __name__ == "__main__":
    main()
