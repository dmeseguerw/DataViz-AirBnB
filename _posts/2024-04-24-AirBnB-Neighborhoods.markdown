---
layout: post
author: Shah, Daniel & Dan
title: "AirBnBs in Copenhagen"
date: 2024-04-24 12:30:14
subtitle: "A small story on the company's status in Denmark's capital"
background: "/images/nyhavn.jpg"
---

### About AirBnB
20 years ago, the hospitality industry consisted on booking only hotel or motel rooms, making it sometimes difficult to travel to cities with low offerings, or prices being ridiculously high. In 2007, the company AirBnB was founded in San Francisco, as a hospitality service that connects people who want to rent out their properties with people who are looking for accomodations. Ever since, AirBnB has grown to over 5 million hosts, with more than 1.5 billion guests, in almost every country in the world. The idea was simple but effective: creating a safe platform for people to show their places on rent and earn some income, and also for visitors to rent places that felt like "home" [^airbnb]. 

AirBnB's business model relies on a "sharing economy", by taking a cut everytime someone books a stay. One good aspect of this service is that it doesn't require hosts to pay to list their properties. Hosts can always list what they want and also set the price accordingly [^investopedia]. Also, moving on to the safety side, AirBnB provides some regulations on how both hosts and users should communicate, ensuring that everyone feels safe and there are no threats, which could result in booking cancellations or even blocking users. 


### Introduction to Dataset

In this post, we'll be exploring AirBnB's data in Copenhagen at the moment of September 2023. This dataset includes an ample set of data ranging from hosts information and ratings, to accomodations information, type, ratings, and location. We'll perform a deep analysis to find interesting patterns, and provide external data to support our findings. A lot of questions can be asked and we'll try to answer some of them: why does certain neighborhoods have lower rentals than others? What are the pricest neighborhoods to rent in Copenhagen? What type of accomodations are usually offered? What is the relationship with pricing and ratings? What can we know about hosts in Copenhagen?

### Neighborhood analysis

As a starter, we present a choropleth map that covers the distribution of rentals per neighborhood in Copenhagen, starting from green as the lowest up to red as the highest number.

<iframe src="{{ site.baseurl }}/data_htmls/choropleth_map_landmarks.html" height="500" width="100%"></iframe>



##### Trending neighborhoods

At a first glance, notice how 3 neighborhoods stand out as the ones with the highest number of rentals: Norrebro, Vesterbro-Kongens Enghave, and Indre By. According to Sølver REF, these 3 neighborhoods, along with Frederiksberg, are the best in Copenhagen. They all offer a lot of entertainment, restaurants, bakeries, shops, and sightseeing. For instance, Norrebro is recognized for its authentic and local Copenhagen atmosphere, with several Danish bakeries and local designer shops, while Indre By is renowned for its list of sightseeing attractions, which can actually be seen on the map with the red markers REF.


##### Harder to get to neighborhoods

On the other hand, notice the 4 neighborhoods with the least amount of rentals: Bispebjerg, Bronshoj-Husum, Vanlose, and Valby. An interesting question might jump from this: why are all these neighborhoods on the west part of the city? Although these neighborhoods also offer a lot, REF ..., there is a small issue in their location that probably makes people resist from renting their places: less access to public transportation. 

If we observe the public transportation map of Copenhagen, we can immediately notice something about the metro and the trains: most of the routes are located on the east part of the city. This is something interesting to note if you are planning on visiting Copenhagen; there could be price differences but access to public transport is essential to many people. However, don't be afraid and hold back; a few metro lines and train rails are currently under planning or construction, connecting more of the west side of the city to the whole transport network. REF


#### Short break! 

Now we want to take a break from all this interesting stories. Feel free to play around with the following map containing markers for all AirBnB rentals in Copenhagen! You can filter out by neighborhoods, and zoom in to find interesting patterns, or even find if there are any rentals near your place. Maybe you'll decide to rent your place if you live in an area with a lack of rentals 😊

<iframe src="{{ site.baseurl }}/data_htmls/airbnbs_marker.html" height="500" width="100%"></iframe>


#### References

[^investopedia]: Folger, J. (2023). How Airbnb Works—for Hosts, Guests, and the Company Itself. From a single air mattress in 2007 to an S&P 500 listing today. Retrieved from [https://www.investopedia.com/articles/personal-finance/032814/pros-and-cons-using-airbnb.asp](https://www.investopedia.com/articles/personal-finance/032814/pros-and-cons-using-airbnb.asp)

[^airbnb]: AirBnB (2023). About us. Retrieved from [https://news.airbnb.com/about-us/](https://news.airbnb.com/about-us/)
[^Winter]: "Why Do Drug Overdoses Increase in Winter?" _The Right Step Rehab Hill Country_. Retrieved from [https://www.rightsteprehabhillcountry.com/addiction-blog/why-do-drug-overdoses-increase-in-winter/](https://www.rightsteprehabhillcountry.com/addiction-blog/why-do-drug-overdoses-increase-in-winter/)
[^UNODC]: United Nations Office on Drugs and Crime. (2007). Strategy for the period 2008-2011 for the United Nations Office on Drugs and Crime. E/CN.7/2007/14–E/CN.15/2007/5. UNODC.
