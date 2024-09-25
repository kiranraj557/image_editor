import streamlit as st 
from PIL import Image
from PIL.ImageFilter import *
import requests
from io import BytesIO

# Page Title
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🖼️ Image Editor</h1>", 
    unsafe_allow_html=True
)
st.markdown("<hr style='border: 1px solid #4CAF50;'>", unsafe_allow_html=True)

# Layout: Sidebar for image upload and filters, main content for the image
with st.sidebar:
    st.header("🛠️ Image Settings")
    
    # Add an option to upload by URL or file
    upload_option = st.selectbox("Select Image Source", options=("Upload File", "Enter Image URL"))

    # Initialize the image variable as None
    img = None

    # Image file uploader
    if upload_option == "Upload File":
        image = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
        if image:
            img = Image.open(image)

    # Image URL uploader
    elif upload_option == "Enter Image URL":
        url = st.text_input("Enter Image URL")
        if url:
            try:
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))
                st.image(img, caption="Image from URL", use_column_width=True)
            except:
                st.error("Invalid URL or unable to load image")

    # Display image settings only when an image is uploaded
    if img:
        st.markdown("<h3 style='color: #4CAF50;'>Edit Image</h3>", unsafe_allow_html=True)
        
        # Resizing
        st.markdown("<h4>🔄 Resize Image</h4>", unsafe_allow_html=True)
        width = st.number_input("Width", value=img.width, min_value=1)
        height = st.number_input("Height", value=img.height, min_value=1)

        # Rotation
        st.markdown("<h4>↩️ Rotate Image</h4>", unsafe_allow_html=True)
        degree = st.slider("Rotate (Degrees)", min_value=0, max_value=360, value=0, step=1)

        # Filters
        st.markdown("<h4>🎨 Apply Filter</h4>", unsafe_allow_html=True)
        filters = st.selectbox("Choose a Filter", options=("None", "Blur", "Detail", "Emboss", "Smooth"))

        # Submit button to apply changes
        s_btn = st.button("Apply Changes")

if img:
    # Main content area: Display image and its details
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h2 style='color: #4CAF50;'>📊 Image Info</h2>", unsafe_allow_html=True)
        st.markdown(f"**Size**: {img.size}")
        st.markdown(f"**Mode**: {img.mode}")
        st.markdown(f"**Format**: {img.format}")

    with col2:
        # Show the image before editing
        st.markdown("<h2 style='color: #4CAF50;'>🖼️ Original Image</h2>", unsafe_allow_html=True)
        st.image(img, caption="Original Image", use_column_width=True)

    # Process and display the final edited image
    if s_btn:
        edited = img.resize((width, height)).rotate(degree)
        filtered = edited

        # Apply selected filter
        if filters == "Blur":
            filtered = edited.filter(BLUR)
        elif filters == "Detail":
            filtered = edited.filter(DETAIL)
        elif filters == "Emboss":
            filtered = edited.filter(EMBOSS)
        elif filters == "Smooth":
            filtered = edited.filter(SMOOTH)

        # Show the edited image
        st.markdown("<h2 style='color: #4CAF50;'>✨ Edited Image</h2>", unsafe_allow_html=True)
        st.image(filtered, caption="Edited Image", use_column_width=True)

# Footer
st.markdown("<hr style='border: 1px solid #4CAF50;'>", unsafe_allow_html=True)

