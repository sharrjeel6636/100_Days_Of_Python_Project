import streamlit as st
import requests

st.set_page_config(page_title="URL Shortener (API)", page_icon="✂️", layout="centered")

st.title("✂️ URL Shortener using Free API")
st.markdown("### Day 37 Project – Shorten URLs instantly using TinyURL's free API (no key required!)")

st.info("This app uses the unofficial TinyURL API endpoint: `http://tinyurl.com/api-create.php?url=LONG_URL`. "
        "It works without any API key and is completely free. Note: It may return the existing short URL if the link was shortened before.")

# Input for long URL
long_url = st.text_input("Enter a long URL to shorten:", placeholder="https://example.com/very/long/url/with/parameters")

if st.button("Shorten URL"):
    if long_url:
        if not long_url.startswith(("http://", "https://")):
            st.error("Please enter a valid URL starting with http:// or https://")
        else:
            with st.spinner("Shortening..."):
                try:
                    response = requests.get(f"http://tinyurl.com/api-create.php?url={long_url}")
                    if response.status_code == 200:
                        short_url = response.text.strip()
                        if short_url.startswith("http"):
                            st.success("Short URL generated successfully!")
                            st.markdown(f"**Short URL:** [{short_url}]({short_url})")
                            st.code(short_url, language=None)
                        else:
                            st.warning("Received unexpected response. Try again.")
                    else:
                        st.error(f"Error: {response.status_code} – Unable to shorten URL.")
                except Exception as e:
                    st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter a URL.")

st.markdown("---")
st.caption("Built with Streamlit ❤️ | Uses TinyURL free endpoint | No API key needed")