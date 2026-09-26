import streamlit as st

# Configure the Streamlit page layout
st.set_page_config(page_title="hungry zone",  layout="centered")

# App Header
st.title("hungry zone")
st.write("Welcome to hungry zone! Browse our categories and pick your favorite treats.")

# Mock Data: List of dictionaries holding menu item details
menu_items = [
    {
        "category": "Appetizers",
        "name": "Crispy Mozzarella Sticks",
        "price": "350",
        "description": "Golden fried mozzarella cheese served with a side of warm marinara sauce.",
        "image_url": "https://images.themodernproper.com/production/posts/2021/Homemade-Mozzarella-Sticks-9.jpeg?w=800&q=82&auto=format&fit=crop&dm=1638935116&s=5bb4d3bca782e98bb068c4a7d10d4c9d"
    },
    {
        "category": "Mains",
        "name": "Classic Cheeseburger",
        "price": "250",
        "description": "Juicy beef patty topped with cheddar cheese, fresh lettuce, tomato, and our signature burger sauce.",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrL-pjKfbgzSPkSCwto1Y0XvFCuyNsYE5XMEqxcJmPR9qA03xtW7_aksg&s=10"
    },
    {
        "category": "Mains",
        "name": "Wood-Fired Margherita Pizza",
        "price": "400",
        "description": "Fresh mozzarella cheese, aromatic tomato sauce, and fresh basil leaves on a crispy, blistered crust.",
        "image_url": "https://www.alfrescochef.co.uk/cdn/shop/articles/Untitled_design_4.png?v=1709212012&width=973"
    },
    {
        "category": "Desserts",
        "name": "Molten Chocolate Lava Cake",
        "price": "200",
        "description": "Rich chocolate cake with a warm, gooey molten center. Served with a scoop of vanilla bean ice cream.",
        "image_url": "https://www.cookingclassy.com/wp-content/uploads/2022/02/molten-lava-cake-17.jpg"
    }
]

# Extract unique categories dynamically for filtering
categories = sorted(list(set(item["category"] for item in menu_items)))

# Sidebar category selector
st.sidebar.header("Filter Options")
selected_category = st.sidebar.selectbox("Choose a Category", ["All Items"] + categories)

# Display items based on selected category filter
for item in menu_items:
    if selected_category != "All Items" and item["category"] != selected_category:
        continue
        
    # Split layout into 2 columns: Image on left, details on right
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Display food item image
        st.image(item["image_url"], use_container_width=True)
        
    with col2:
        # Display title, price, category tag, and explanation
        st.subheader(f"{item['name']}")
        st.write(f"**Price:** {item['price']}")
        st.caption(f"Category: {item['category']}")
        st.write(item["description"])
    
    # Visual divider between menu options
    st.divider()
