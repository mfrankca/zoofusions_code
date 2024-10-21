import streamlit as st
from PIL import Image
import os

# Sidebar image
###image_path = ".\Logo\ZooFusions_logo.png"
image_path = os.path.join(".", "Logo", "ZooFusions_logo.png")

if os.path.exists(image_path):
    st.sidebar.image(image_path, use_column_width=True)
else:
    st.sidebar.write("Logo not found")
    
# Display logo and business title
#st.image(logo, width=300)
st.sidebar.title("Zoo Fusions")
st.sidebar.subheader("Cat & Dog Products | Online Veterinary Consultations")

# Sidebar navigation
menu = ["Executive Summary", "Business Objectives", "Market Research", "Detailed Market Research for Zoo Fusions", 
        "Business Model", "Services and Products", "Operations Plan", 
        "Marketing Plan", "Financial Plan", "Risk Analysis", "Pitch"]
choice = st.sidebar.selectbox("Menu", menu)

# Load content based on menu choice
if choice == "Executive Summary":
    st.header("Executive Summary")
    st.write("""
    PetCare Online Canada aims to become the leading online platform in Canada for pet owners seeking convenient,
    expert veterinary consultations, grooming tutorials, and pet health tracking. 
    Alongside these services, we will offer an integrated e-commerce platform for pet supplies. 
    With the growing trend of pet ownership and demand for remote, accessible pet care services, 
    PetCare Online Canada will meet the evolving needs of modern pet owners.

    """)


elif choice == "Business Objectives":
    st.header("Business Objectives")
    st.write("""
    Short-term goals (Year 1): 
        Launch the platform in key Canadian cities (Toronto, Vancouver, Montreal).
        Achieve 10,000 registered users within the first year.
        Build partnerships with 100+ certified veterinarians and pet care professionals.
        Integrate an e-commerce store for essential pet supplies.

    - **Year 2-3**: 
    Expand services nationwide.
  - Increase registered users to 50,000.
  - Launch premium membership for unlimited veterinary consultations and discounts on pet supplies.

    - **Year 5**:  Establish PetCare Online as the go-to platform for pet care in Canada.
  - Expand into additional markets like the U.S. or the U.K.
  - Offer pet insurance services integrated with consultations.
    """)

# Repeat for other sections
elif choice == "Market Research":
    st.header("Market Research")
    st.write("""
             **Industry Overview**:  
The Canadian pet care industry is booming, with pet ownership on the rise. In 2023, the pet care market in Canada was estimated at CAD 9 billion, growing at 6% annually. The demand for digital pet care services surged during the COVID-19 pandemic, and this trend has continued as pet owners seek convenient, remote services.

**Target Audience**:  
- **Pet Owners**: Especially those in urban areas who value convenience and access to professional services online.
- **Pet Lovers with Busy Schedules**: Users who lack the time for frequent in-person vet visits or grooming services.
- **Millennials and Gen Z**: Tech-savvy, pet-loving individuals who prefer digital solutions.
- **Pet Breeders**: Small-scale breeders needing regular, remote consultations.

**Market Opportunities**:  
- **Untapped Regions**: Smaller Canadian cities and rural areas where access to quality veterinary care is limited.
- **Niche Markets**: Services for pets with specific needs (elderly pets, pets with chronic conditions) and specialty products (organic food, eco-friendly pet supplies).

             """)
elif choice == "Detailed Market Research for Zoo Fusions":
    st.header("Detailed Market Research for Zoo Fusions")
    st.write("""
             1. Global Pet Care Industry Overview:
The global pet care industry is experiencing rapid growth, driven by increased pet ownership, humanization of pets, and the trend toward online shopping for pet products and services. Here are the key statistics and insights:

Market Size: The global pet care market was valued at approximately $235 billion in 2023 and is projected to grow at a CAGR (Compound Annual Growth Rate) of 6.1% between 2023 and 2027, reaching an estimated $350 billion by 2027.
Pet Ownership Trends:
In North America, approximately 70% of households own at least one pet (around 90.5 million households in the U.S.). Canada also sees high rates of pet ownership, with about 58% of households having pets.
The increasing adoption of pets, especially dogs and cats, is driving demand for pet care services and products.
2. E-commerce and Online Veterinary Services:
E-commerce Growth in Pet Products: The global pet e-commerce market reached $30 billion in 2023, and it is expected to double to $60 billion by 2027, driven by the rise in online shopping convenience, curated product offerings, and subscription-based services.
U.S. E-commerce Sales: E-commerce sales for pet care in the U.S. accounted for 37% of all pet product purchases in 2023.
Online Veterinary Services: The global telemedicine market, including veterinary services, was valued at $1.3 billion in 2023, with a projected CAGR of 16.4% until 2028.
Veterinary Services Market Size: The veterinary services market was valued at $125 billion globally in 2023, with an increasing portion of that shifting to online and telemedicine-based services.
3. Target Audience for Zoo Fusions:
Demographics:
Pet Owners: Primarily millennials (aged 25-40) and Gen Z pet owners are driving the shift toward online services and products. Millennial pet owners spend 30% more on their pets than previous generations.
Income Brackets: Households earning $75,000 and above tend to spend significantly on premium products and services for pets, including health, wellness, and high-quality foods.
Geographic Target: Primary focus on North America (U.S. and Canada) with future expansion into the UK and Europe. The U.S. holds the largest share of the pet care market, at approximately 40% of the global market.
Key Customer Segments:
Busy Professionals: Looking for convenience in both pet health (tele-vet) and curated product offerings.
Health-Conscious Pet Owners: Concerned about the quality of pet food, supplements, and wellness products.
Tech-Savvy Millennials: Open to new technology-based services like telemedicine and app-based consultations for their pets.
4. Competitive Landscape:
Major Competitors (Online Pet Stores and Services):

Chewy.com: One of the largest online pet retailers, generating $9 billion in revenue in 2023. It offers auto-ship subscriptions for pet food, health products, and medications.
Petco: With both brick-and-mortar and online presence, Petco provides pet products, grooming services, and veterinary care.
Vetster: A growing platform offering tele-veterinary services. It raised $30 million in venture funding and is expanding its market reach.
Competitive Differentiation for Zoo Fusions:

Veterinary Services + E-commerce: A comprehensive platform combining personalized veterinary services with high-quality, curated products for cats and dogs.
Subscription Services: Offering both veterinary subscription packages (monthly or annual) and product subscriptions (for pet food and care essentials).
Niche Focus: Tailored product recommendations based on pets’ health needs, integrating data from consultations.
5. Pet Industry Product Segmentation (2023):
Food and Treats: $100 billion market size, with a 5.7% CAGR expected through 2027.
Pet Care Products: $20 billion market size, including grooming, health, and hygiene products.
Veterinary Care Services: $30 billion market size, projected to grow at a 7.2% CAGR.
Pet Toys and Accessories: $15 billion market size, with growing demand for eco-friendly and sustainable products.
6. Pricing Strategy Insights:
Veterinary Consultations Pricing:
Standard Consultation Fee: $40 - $100 (depending on consultation length and veterinarian expertise).
Subscription Plans:
Basic Plan: $20/month for two consultations.
Premium Plan: $50/month for unlimited consultations.
E-commerce Product Pricing:
Pet Food (Premium Brands): $30 - $80 per bag (5-10 kg).
Toys and Accessories: $10 - $50, with customizable options priced higher.
Grooming and Hygiene Products: $15 - $50.
7. Projected Market Share for Zoo Fusions:
Given the market trends, Zoo Fusions aims to capture a small but growing portion of the pet care and e-commerce market:

Year 1 Goal: Capture 0.05% of the global pet care e-commerce market ($30 million) and veterinary telemedicine market ($1.3 million).
Projected Revenue (Year 1):
Veterinary Services: $150,000 (through consultations and subscriptions).
E-commerce Sales: $350,000 (average order value $50, 7,000 customers).
Year 3 Goal: Expand to 0.1% market share, aiming for:
Veterinary Services: $400,000 revenue.
E-commerce Sales: $900,000 revenue.
8. Market Trends and Opportunities:
Humanization of Pets: Pet owners are treating their pets like family, driving demand for premium products and healthcare services.
Sustainability: There is a growing market for eco-friendly pet products (toys, grooming products, food packaging) as consumers become more environmentally conscious.
Pet Wellness: Supplements, natural food, and specialized diets (e.g., grain-free, organic) are increasingly popular.
Tech-Enabled Services: Pet owners are embracing tech-based solutions such as telemedicine, wearables for pets, and online health records, presenting opportunities for Zoo Fusions to integrate advanced health monitoring tools.
9. SWOT Analysis:
Strengths:

Comprehensive platform combining veterinary services and e-commerce.
Personalized pet health recommendations.
Low overhead with a focus on digital services.
Weaknesses:

High competition from established players like Chewy and Vetster.
Dependency on digital marketing for customer acquisition.
Opportunities:

Growing demand for tele-vet services and subscription-based products.
Ability to tap into international markets with minimal additional infrastructure.
Threats:

Regulatory challenges in the veterinary field (licensing for telemedicine across borders).
Rising shipping and product fulfillment costs.
10. Conclusions and Strategic Recommendations:
Focus on Customer Experience: Build trust with users by offering exceptional veterinary care and high-quality products. Create a community around Zoo Fusions with educational content and interactive features like live Q&A sessions with vets.
Leverage Data and AI: Use customer data from consultations to offer highly personalized product recommendations, which can increase sales and customer satisfaction.
Expand Product Offerings: Explore niche products like pet tech (GPS collars, activity monitors) and pet insurance to differentiate Zoo Fusions from competitors.
""")
elif choice == "Business Model":
    st.header("Business Model")
    st.write("""
             **Revenue Streams**:  
1. **Veterinary Consultations**:
   - **On-demand consultations**: Video calls with certified veterinarians for a flat fee (CAD 30 per consultation).
   - **Subscription Model**: Unlimited consultations for a monthly fee (CAD 50/month).
   
2. **Pet Health Tracking and Subscription Plans**:
   - Customized pet health tracking via a mobile app (CAD 5/month per pet).
   - Premium plans that include health tracking, nutritional advice, and regular vet check-ins (CAD 70/month).

3. **E-commerce Platform**:
   - **Pet supplies**: Selling essential pet care items (food, grooming tools, toys) via an online store.
   - **Affiliate commissions**: Partnering with pet brands to sell their products on the platform.
   - **Monthly subscription boxes**: Offering curated pet care boxes (CAD 30-50/month).

4. **Grooming Tutorials and Online Classes**:
   - **On-demand tutorials**: Videos on grooming, training, and general pet care (CAD 5 per class or CAD 25 for a package).
   - **Virtual grooming workshops**: Live sessions with pet care experts for a fee (CAD 50 per workshop).

5. **Advertisements and Sponsored Content**:
   - Monetizing the platform through pet-related advertisements (brands, products, services).
   - Sponsored content by pet care brands and services.
             """) 
elif choice == "Services and Products":
    st.header("Services and Products")
    st.write("""
              **Veterinary Consultations**:  
   - Available 24/7 with certified professionals for general pet health, emergencies, and second opinions.
   
- **Pet Grooming Tutorials**:  
   - Step-by-step tutorials on pet grooming (e.g., clipping nails, trimming fur, bathing).

- **Health Tracking**:  
   - An app that tracks vet appointments, vaccinations, medications, and overall pet health metrics.

- **Pet Supplies**:  
   - High-quality food, grooming kits, toys, and accessories available for purchase through the online store.

- **Subscription Boxes**:  
   - Monthly curated boxes with toys, treats, and care products tailored to different types of pets (dogs, cats, etc.).

 """)    
elif choice == "Operations Plan":
    st.header("Operations Plan")
    st.write("""
              **Platform Development**:  
- **Tech Stack**:  
  - Use cloud-based infrastructure for scalability (AWS or Azure).
  - Develop a responsive web platform and a mobile app (iOS/Android).
  - Secure payment gateways (Stripe, PayPal) for e-commerce transactions.
  
- **Staffing**:  
  - **Year 1**: 10 full-time employees (developers, customer support, marketing).
  - **Year 2-3**: Expand the team to 30, including veterinarians, tech support, and sales.
  
- **Veterinary Partnerships**:  
  - Work with registered veterinarians across Canada, offering them a commission-based model (e.g., 70/30 split).

- **Customer Support**:  
  - 24/7 customer support via chat and email, offering assistance for both pet care services and product inquiries.
 """)   
elif choice == "Marketing Plan":
    st.header("Marketing Plan")
    st.write("""
              **Customer Acquisition**:
- **Digital Marketing**:  
   - Google Ads, Facebook Ads, Instagram marketing targeting pet owners and pet-related interest groups.
  
- **SEO**:  
   - Invest in SEO for content related to pet health, grooming tips, and pet supplies.
  
- **Influencer Partnerships**:  
   - Collaborate with Canadian pet influencers on Instagram and YouTube for promotion and reviews.

- **Referral Program**:  
   - Offer discounts or free consultations for users who refer friends.

**Customer Retention**:
- **Loyalty Program**:  
   - Introduce a rewards system where frequent users earn points for consultations and purchases.
  
- **Content Marketing**:  
   - Blog posts, newsletters, and free webinars on pet health tips, training techniques, etc.

- **Social Media Presence**:  
   - Regular engagement with the pet community via Instagram, TikTok, and YouTube showcasing expert advice, user stories, and pet care tips.
""")         
elif choice == "Financial Plan":
    st.header("Financial Plan")
    st.write("""
              **Initial Investment**:  
- **Platform Development**: CAD 150,000.
- **Marketing and Advertising**: CAD 100,000 for digital campaigns.
- **Staffing Costs**: CAD 200,000 annually (developers, customer support, veterinarians).
- **Miscellaneous Costs**: CAD 50,000 (legal, licenses, initial inventory for e-commerce).

**Revenue Projections (Year 1)**:
- **Veterinary Consultations**: CAD 300,000 (10,000 consultations at CAD 30 each).
- **E-commerce Sales**: CAD 200,000 from pet supplies and subscription boxes.
- **Grooming Tutorials**: CAD 50,000.
- **Subscription Plans**: CAD 100,000 (2,000 users at CAD 50/month).

**Total Projected Revenue (Year 1)**: CAD 650,000.

**Break-Even Point**:  
- The business expects to break even within 18-24 months, depending on user growth and marketing efforts.

---""")
elif choice == "Exit Strategy":
    st.header("Exit Strategy")
    st.write("""
    - **IPO or Acquisition**:  
   - In the long-term, the company can be positioned for acquisition by a larger pet care or veterinary company, or it could pursue an IPO as the brand scales.
  """)
elif choice == "Risk Analysis":
    st.header("Risk Analysis")
    st.write("""
- **Regulatory Hurdles**:  
  - Ensuring compliance with veterinary licensing and telemedicine regulations in Canada.
  
- **User Adoption**:  
  - Convincing pet owners to switch to online consultations over traditional in-person vet visits.

- **Competition**:  
  - As the market matures, competition from large e-commerce players or other veterinary platforms could increase.

- **Technology Costs**:  
  - High initial costs for platform development and maintenance could be challenging, but offset by a strong user base and revenue growth.
""")   
    
elif choice == "Conclusion":
    st.header("Conclusion")
    st.write("""
             PetCare Online Canada aims to fill a growing need for convenient, accessible, and expert pet care services across Canada.
             By combining veterinary consultations, pet health tracking, grooming tutorials, and an e-commerce platform for pet supplies, this business is poised for success in the expanding pet care market.
             """)          
elif choice == "Pitch":
    st.header("Investor Pitch")
    st.write("""
           **Zoo Fusions Pitch**
             Introduction:
             At Zoo Fusions, we’re not just another pet store—we are the go-to online platform for veterinary consultations and premium pet products exclusively for cats and dogs.
             Pet owners today expect more convenience, personalized care, and quality. 
             Zoo Fusions delivers all that and more with a seamless blend of tele-veterinary services and curated e-commerce, making pet parenting easier, healthier, and more joyful.
    
Problem:

Pet owners are often faced with two major challenges:
Access to reliable, professional veterinary care without long waits or expensive in-person visits.
Finding high-quality, trusted pet products that match their pets' unique needs and health conditions.
Solution: Zoo Fusions solves both problems on a single platform:

Veterinary Telemedicine: Quick and easy access to licensed veterinarians for consultations from the comfort of home. Whether it’s for routine advice or more urgent issues, we offer flexible and affordable tele-vet services.
Curated E-Commerce Store: Our online store offers carefully selected premium products for cats and dogs, from food and supplements to toys and grooming essentials, all matched to pets’ health profiles based on their vet consultations.
Market Opportunity: The global pet care industry is valued at $235 billion, growing at 6.1% CAGR, with e-commerce in pet care expected to reach $60 billion by 2027. The demand for tele-veterinary services is booming, expected to grow at 16.4% CAGR over the next 5 years. Zoo Fusions is perfectly positioned to capitalize on this growth by combining both offerings into one trusted platform.

Why Zoo Fusions?

Personalized Care: Through tele-vet consultations, we collect valuable insights into pets’ health needs, allowing us to offer personalized product recommendations.
Convenience: Pet owners can consult a vet, get a diagnosis, and order the right products—all in one go. No more searching through endless options.
Subscription Services: Zoo Fusions offers custom subscription plans for regular veterinary check-ups and auto-ship products like food, ensuring pets never run out of essentials.
Expert Curated Products: Only the best, vet-recommended products make it to our store, ensuring pets get safe, high-quality nutrition, care, and playtime.
Revenue Model:

Veterinary Consultations: Pay-per-consultation or monthly/annual subscription plans for unlimited access.
E-Commerce Sales: High-margin premium products with opportunities for subscription-based recurring revenue.
Partnerships: Collaborations with pet product brands and vet clinics for co-branded offerings and exclusive deals.
Traction: We’re building momentum with a growing community of engaged pet owners who value expert advice, trusted products, and convenience. With a powerful e-commerce platform, a focus on customer loyalty, and a seamless telemedicine experience, we’re positioned for rapid growth.

Ask: We’re seeking $1.5 million in seed funding to:

Expand our tele-vet network across North America.
Invest in data-driven marketing to acquire more customers.
Build a robust logistics system to scale product delivery.
With your support, we’ll make Zoo Fusions the ultimate destination for modern pet care.

Conclusion: At Zoo Fusions, we believe pets deserve the best—and so do their owners. We’re redefining pet care by combining telemedicine and e-commerce to provide convenient, personalized solutions. Join us on our journey to transform the way pet owners care for their furry companions!
    """)
    if st.button("Download Pitch"):
        # Logic to generate and download the pitch as PDF
        st.write("Download initiated...")