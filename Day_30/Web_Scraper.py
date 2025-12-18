import streamlit as st
import requests
from bs4 import BeautifulSoup

# Page config
st.set_page_config(page_title="Web Scraper", page_icon="🌐")

st.title("🌐 Web Scraper – Day 30 of 100 Days of Python")
st.write("Enter a website URL to extract basic information.")

url = st.text_input("🔗 Enter Website URL", placeholder="https://example.com")

if st.button("🔍 Scrape Website"):
    if not url:
        st.error("Please enter a URL!")
    else:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0"
            }
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code != 200:
                st.error("Failed to fetch the website.")
            else:
                soup = BeautifulSoup(response.text, "html.parser")

                # Page title
                st.subheader("📄 Page Title")
                st.write(soup.title.string if soup.title else "No title found")

                # Headings
                st.subheader("🔖 Headings (H1 - H3)")
                for tag in ["h1", "h2", "h3"]:
                    headings = soup.find_all(tag)
                    if headings:
                        st.write(f"**{tag.upper()}**")
                        for h in headings:
                            st.write("-", h.get_text(strip=True))

                # Links
                st.subheader("🔗 Links Found")
                links = soup.find_all("a", href=True)
                for link in links[:10]:  # limit to 10 links
                    st.write(link["href"])

        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.info("Enter a URL and click **Scrape Website**.")
