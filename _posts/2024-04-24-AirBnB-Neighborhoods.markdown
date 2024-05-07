---
layout: post
author: Shah, Daniel & Dan
title: "AirBnBs in Copenhagen"
date: 2024-04-24 12:30:14
subtitle: "A small story on the company's status in Denmark's capital"
background: "/images/nyhavn.jpg"
---

### About AirBnB 🏨🏠

20 years ago, if you wanted to travel to another city and stay there for a while, the only options you had were either to find a hotel or motel room. Hotels held a monopoly over the lodging industry, which allowed them to charge exorbitant amounts for relatively short duration of stays, simply because people didn't have any other choice. In 2007, the company AirBnB was founded in San Francisco, as a hospitality service that connects people who want to rent out their properties with people who are looking for accomodations. Since then, AirBnB has grown to over 5 million hosts, with more than 1.5 billion guests, in almost every country in the world. The idea is simple but effective: creating a safe platform for people to show the places they wanted to rent so they could earn some income, and also for visitors to rent places that felt like "home" [^airbnb].

AirBnB's business model relies on a "sharing economy", by taking a cut everytime someone books a stay. One good aspect of this service is that it doesn't require hosts to pay to list their properties. Hosts can always list what they want and also set the price accordingly [^investopedia]. Also, moving on to the safety side, AirBnB provides some regulations on how both hosts and users should communicate, ensuring that everyone feels safe and there are no threats, which could result in booking cancellations or even blocking users.

In this article we are going to walk you through the current scene of AirBnB rentals in the beautiful city of Copenhagen. Whether you are thinking of visiting the city and are curious to know all the facts and figures about rentals in the city, or if you are thinking of investing in the listing your own property on the platform, this article is going to answer some of your most important questions. First we present some facts and figures and try to analyze some trends that might not be visible on the surface. Once you have gotten a lay of the land, so to speak, you can explore the data by yourself! Using the interactive map we have provided in this article. Lets begin!

### Introduction to Dataset ⚙️

First of all we want to introduce a little bit our source of all these wonderful charts and information. In this post, we'll be exploring a dataset known as [Inside AirBnB](https://insideairbnb.com/). The Copenhagen dataset contains information about all the properties that are listed on AirBnB's platform, as of September 2023. The dataset includes information for over 18,000 properties listed as AirBnB rentals in Copenhagen city. We'll be taking a deep dive into this data to find interesting patterns, to try and answer some of your burning questions, such as, why do listings in certain neighborhoods have lower rent per night than others? What are the pricest neighborhoods to rent in Copenhagen? What type of accomodations are usually offered? What is the relationship with pricing and ratings? What can we know about hosts in Copenhagen? 🤔

### Price Analysis

Let us try and answer the 3.8 Billion DKK questions[^CPHimpact] (the total revenue AirBnB has earned in Denmark since 2009). The plot below gives us the first take a look at the density of rental units based on their price in different parts of the city. Indre By (which translates to "inner city"), also known as Copenhagen K or Downtown Copenhagen, has the highest average price of rental units available across the city. BnB listings in this area are going to cost you upwards of DKK 1600 for a stay. Indre By lies at the heart of the city so this is kind of unsurprising, but we still provide some plausible reasons behind the unsually high pricing.

<img src="{{ site.baseurl }}/images/price_density_neighborhood.png" style="width: 100%; height: auto;">

### Room type analysis

The provided bar charts offer a detailed breakdown of various aspects of rental properties in Copenhagen, ranging from bedroom and bed distribution to bath facilities and room types. The majority of listings feature one bedroom, indicating a prevalence of smaller accommodations suitable for solo travelers or couples. Similarly, the bed distribution chart shows a dominance of properties with one bed, aligning with the bedroom data. The bath distribution highlights that most properties provide one bathroom, enhancing convenience for guests. Additionally, the room type distribution chart reveals that a vast majority of properties are entire homes or apartments, suggesting a preference among travelers for privacy and full amenities, with only a small percentage opting for private or shared rooms. These visuals collectively paint a comprehensive picture of the rental options available, showcasing preferences and trends within the Copenhagen housing market.

<iframe src="{{ site.baseurl }}/data_htmls/distribution.html" height="550" width="100%" style="border:none;"></iframe>

In this elegant visualization, we delve into the pricing and rating landscapes of rental properties, captured through meticulously plotted histograms and a revealing scatter plot. The majority of properties boast near-perfect ratings, reflecting a market where excellence predominates and guest satisfaction is high. Turning to the price distribution, it’s a tale of affordability with most properties priced below 1,000 DKK, hinting at a diverse array of lodging options suitable for various budgets.

<img src="{{ site.baseurl }}/images/price.png" style="width: 100%; height: auto;">

### Neighborhood analysis

As a starter, we present a choropleth map that covers the distribution of rentals per neighborhood in Copenhagen, starting from green as the lowest up to red as the highest number.

<iframe src="{{ site.baseurl }}/data_htmls/choropleth_map_landmarks.html" height="500" width="100%"></iframe>

We introduce a choropleth map that vividly illustrates the distribution of rental properties across Copenhagen neighborhoods. The color gradient starts with green, representing areas with the fewest rentals, and progresses to red, indicating neighborhoods with the highest concentration of rentals. This visual tool offers a straightforward depiction of rental density across the city.

<iframe src="{{ site.baseurl }}/data_htmls/hexagon_layer.html" height="500" width="100%"></iframe>

##### Trending neighborhoods

At a first glance, notice how 3 neighborhoods stand out as the ones with the highest number of rentals: **Nørrebro, Vesterbro-Kongens Enghave, and Indre By**. According to _Sølver_ [^nghbs], these 3 neighborhoods, along with Frederiksberg, are the best in Copenhagen. They all offer a lot of entertainment, restaurants, bakeries, shops, and sightseeing. For instance, Nørrebro is recognized for its authentic and local Copenhagen atmosphere, with several Danish bakeries 🥐 and local designer shops 👗, while Indre By is renowned for its list of sightseeing attractions 🧳🏛️, which can actually be seen on the map with the red markers ❗ [^landmarks].

In the realm of rental availability, over half of the landlords typically offer their properties just one month in advance. However, in our analysis, when filtering out listings available for fewer than 180 days, **Indre By** dramatically leads over **Nørrebro and Vesterbro-Kongens Enghave** in listing percentages. As Copenhagen's quintessential tourist heartland, **Indre By** is dense with must-see attractions and is ripe with properties designed for the traveler in mind. Here, savvy landlords prefer longer lease periods, capitalizing on the constant flow of tourists, unlike their counterparts in quieter residential areas. This trend underlines a clever strategy by Indre By property owners who are keen to optimize earnings all year round from the ever-present tourist buzz.

<img src="{{ site.baseurl }}/images/filter_available.png" style="width: 100%; height: auto;">

##### Harder to get to neighborhoods

On the other hand, notice the 4 neighborhoods with the least amount of rentals: **Bispebjerg, Brønshøj-Husum, Vanløse, and Valby**. An interesting question might jump from this: why are all these neighborhoods on the west part of the city? Although these neighborhoods also offer a lot, there is a small issue in their location that probably makes people resist from renting their places: **less access to public transportation**.

<img src="{{ site.baseurl }}/images/transport.png" style="max-width: 80%; height: auto; display: block; margin: 0 auto;">

<!-- ![Copenhagen metro and railway system]("{{ site.baseurl }}/images/transport.jpg") -->

If we observe the public transportation map of Copenhagen 🚄[^transport], we can immediately notice something about the metro and the trains: most of the routes are located on the east part of the city. This is something interesting to note if you are planning on visiting Copenhagen. Even though there are a lot of bus routes and services offered in these neighborhoods, train and metro services are lacking, with most of them only having a couple of stops.

#### Short break!

Now we want to take a break from all this interesting stories. Feel free to play around with the following map containing markers for all AirBnB rentals in Copenhagen! You can filter out by neighborhoods, and zoom in to find interesting patterns, or even find if there are any rentals near your place. Maybe you'll decide to rent your place if you live in an area with a lack of rentals 😊

<iframe src="{{ site.baseurl }}/data_htmls/airbnbs_marker.html" height="500" width="100%"></iframe>

#### References

[^CPHimpact]: AirBnB's impact in Copenhagen. [Report published by AirBnB](https://news.airbnb.com/wp-content/uploads/sites/4/2019/06/Report-Airbnb%E2%80%99s-Impact-in-Copenhagen.pdf)
[^investopedia]: Folger, J. (2023). How Airbnb Works—for Hosts, Guests, and the Company Itself. From a single air mattress in 2007 to an S&P 500 listing today. Retrieved from [https://www.investopedia.com/articles/personal-finance/032814/pros-and-cons-using-airbnb.asp](https://www.investopedia.com/articles/personal-finance/032814/pros-and-cons-using-airbnb.asp)
[^nghbs]: Sølver, C. (2022). The best neighborhoods in Copenhagen to find your hygge. Retrieved from [https://www.lonelyplanet.com/articles/best-neighborhoods-in-copenhagen](https://www.lonelyplanet.com/articles/best-neighborhoods-in-copenhagen)
[^landmarks]: Visit Copenhagen (2024). Top attractions in Copenhagen. Retrieved from [https://www.visitcopenhagen.com/copenhagen/activities/top-attractions-copenhagen](https://www.visitcopenhagen.com/copenhagen/activities/top-attractions-copenhagen)
[^airbnb]: AirBnB. (2023). About us. Retrieved from [https://news.airbnb.com/about-us/](https://news.airbnb.com/about-us/)
[^transport]: Kristofer Torbjørn, K. & Omelekhin, P (2023). A New Rapid Transit Map of Copenhagen. Retrieved from [https://cphtransitmap.dk/en/] (https://cphtransitmap.dk/en/)
