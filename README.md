# BOOK MY WEDDING WISH - Online Wedding Registry For Your Guests

Code Institute - Milestone Project 3 - Data Centric Development

BOOK MY WEDDING WISH helps you create your dream wedding registry for your friends and family.
Since it can be difficult, and often awkward, to communicate to your guests what you need or would like to receive,
Book My Wedding Wish allows you to create an online gift wishlist that you can share with your guests - for free.

The primary purpose of this web app is to help the soon-to-be married couple with informing their wedding attendees what they 
would prefer to receive as presents. Instead of talking to each guest separately, struggling with giving present suggestions 
that would fit a guest's budget, getting the same present twice or end up not liking a present at all - Book My Wedding Wish 
aims to help the happy couple by allowing them to create an online place where guests can choose among the presents the couple wishes
to receive.

As the guests also struggle with choosing a present for the newlyweds - which is often quite expensive - this online 
wedding gift wishlist helps them with deciding on what to buy while they can be sure the present will be greatly appreaciated. 
Therefore, the secondary purpose of this app is to provide a simple overview of desired wedding presents and an easy booking process.

![App Showcase](readme-files/images/img-showcase.png)

## UX

It is no secret wedding planning can be quite stressful and time-consuming. According to [Zola's survey](https://www.zola.com/blog/wedding-planning/science-wedding-planning-stressful/) 
on wedding planning, 96% of couples find wedding planning stressful. In fact, 86% of respondents suffered from up to three stress-induced symptoms, 
including skin breakouts, hair loss, insomnia, headaches, etc. On the other hand, 
[DailyMail](https://www.dailymail.co.uk/femail/article-2394473/Thats-ungrateful-82-PER-CENT-newlyweds-admit-selling-wedding-gifts-eBay.html) 
reports that "42% of guests admit they find buying wedding gifts stressful" while 10% of invited guests "declined invitation due to finding 
gift-buying process unpleasant." Despite the effort guests put into choosing a present, DailyMail's research has also shown that 20% of guests 
expect their gifts to be left unused, returned or sold while 82% of newlyweds actually do end up selling their presents on eBay and similar sites.

The psychology of giving wedding gifts is truly fascinating. In NPR's [interview with Shankar Vedantam](https://www.npr.org/2016/06/24/483426485/new-study-explores-psychology-of-giving-wedding-gifts?t=1599418748672), 
who did a research on this topic, Shankar says the tensions are produced from the fact that we want the gift to please the people getting married but 
at the same time, the gift should reflect well on us. One of the reasons why guests deviate from buying off the wedding registry is that it doesn't 
feel special enough. It is the close friends that normally deviate from the registry, saying that "they're doing it because they know what we really 
want more than we know ourselves." It doesn't seem like those 82% newlyweds who end up selling their wedding presents on eBay would agree.

### Conclusion of the Research

For a life event that is expected to be full of joy and harmony, the reasearch shows otherwise for majority of the participants - newlyweds and guests both.
The wedding planning is already stressful enough and the research shows the happy couple doesn't seem to be as happy with the presents despite the 
availability of wedding registries. This project follows the general UX of other online wedding registries such as [MyRegistry](https://www.myregistry.com/) 
and [Zola](https://www.zola.com/) with an important twist - a present is submitted with a personal note from the couple explaining why they want 
exactly this present. This might help the guests to realise the importance of the item on the list and encourage them to stick to the list.

![App Competitors](readme-files/images/img-competitors.png)

### Customer Goals

The primary customers for this app are the wshlist owners, however, since guests are interactng with the wishlist as well, they can be considered as 
the secondary customers.

As a wishlist owner...

* I need to communicate well to my guests which presents I'd like to receive so that I don't get something I don't want or need.
* I want to save my gift wishlist online so that I can easily share it with the guests.
* I want to be able to see which gifts will be bought so that I can add more if I have to.
* I want to have control over the presents I put on the wishlist so that I know the guests have the updated list.
* I want to be able to add a personal message to each present so the guests know why I want that particular present.
* I want to have a variety of presents on the wishlist so that everyone can pick something it fits their budget best.

As a wedding guest...

* I need help with deciding what to buy to the happy couple because the buying process is stressful for me.
* I need to be sure the couple will love the present I buy so that I don't feel like I've wasted my money.
* I want to know that other guests will not buy the same product so that the couple doesn't get the same present twice.
* I want to buy a present that I am also happy with so that I feel like I'm giving something unique or special.

### Business Goals

This project is mostly focusing on the end-user needs, such as wishlist owners and their wedding guests, since the main goal was to make sure the web app is 
suitable and useful for them. However, the business idea for this app could follow the affiliate business model most online weddng registries follow. 
The features related to business goals can be implemented in the future product releases.

As a business owner...

* I want to be able to analyse what users are buying so I can earn by selling data to 3rd parties.
* I want to see which brands people are buying from so that I could start brand partnership with them.
* I want the user to have an interface they will love because they will want to come back.
* I want the users to be able to connect to the product online so that the chances of buying itand earning from it's commision are higher.

## Features and App Sections

As this project relies on backend technologes more than my previous projects, my process for defining features and information architecture was different. 
I've started with listing the actions that the users should be able to do with this app - first wishlist owners and then their wedding guests. This also meant that 
dfferent types of users, owners and the guests, should have different page views. Finally, I didn't want this project to be accessble to only logged in or signed in 
website visitors because I've often felt discouraged to proceed to explore projects from the others that required me to give them my personal details like my email 
address or having to create passwords to remember how to access my account. Therefore, I had to be sure the features are grouped per user type and reflected well 
in the website structure as well as having an easy way to come back to the submitted information.

As a result, I prepared this short overview of what each website section should be able to do or provide, which was my main guide when working on the app. This is how 
the MVP was created.

![Feature and Information Architecture Overview](readme-files/images/img-feature-overview.png)

### App Sections

1. **Navigation on the top** - fixed navigation on the top which differs to different user type so that the users have shortcuts to the main functions of the particular 
page view (edit present, edt wishlist, delete wishlist, etc.) and are able to navigate themselves back to the homepage if needed.
1. **Header** - introduction to the website or to the wishlist - different to different user type with the appropriate information in the header.
1. **Homepage USP section** - a quick overview of the steps how the app works.
1. **Hmepage about section** - rather than speaking about the project itself, this small textual section addresses users' pain points and introduces Book My Wedding Wish as a solution to their problems.
1. **Owner view** - a set of pages where the wishlist owners can add presents to their list, update and delete the wishlist and the products and link to the guest view.
1. **Guest view** - a set of pages where the first time guest visitor can submit their username to book and unbook the presents they want to buy.
1. **Footer** - gives users the option to stay up to date with the app via links to social media profiles.

### Features

The features are split into owner related features and guest related features.

Owner features:

1. **Unique wishlist creation** - a feature that allows users to create their wishlists by submitting a unique wishlist name. The app validates the submitted name and encourages a new 
one if needed. It is important the name is unique because it appears in the link to the wishlist. The name cannot be edited afterwards - thought he owner has the possibility to delete 
the whole wishlist and create a new one if neeeded.
1. **Additional wishlist information** - a feature that let's the wishlist owners customize their wishlist preview by adding wishlist description, header image, wedding details and customize 
the header colour of the wishlist (i.e. choosing the wishlist theme).
1. **Add presents to the list** - a feature that let's the owners add presents to the list. The older presents appear at the top of the page.
1. **Edit presents** - a feature that allows the owners to edit a submitted present's details.
1. **Delete presents** - a feature that allows the owners delete the presents they don't want to have on the list.
1. **Edit wishlist** - a feature that allows the owners to edit wishlist information. The wishlist name and the theme are not editable. Name can't be edited to preserve the uniqueness 
of the shareable link. Wishlist theme editing has been explained in the future features below.
1. **Delete wishlist** - a feature that allows the owners delete the wishlist.

Guest features:

1. **Submit username** - a feature that let's the user register to the wishlist with their name. An important step to be able to reserve the presents.
1. **Book a present** - a feature that allows registered guests to reserve the presents.
1. **Unbook a present** - allows registered guests to unbook the presents they have previously reserved.

