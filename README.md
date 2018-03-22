# INFX547Proj
INFX 547 Social Media Data Mining Class Project

Group Members:
- Tiffany Chiu
- Pranavi Midathada
- Casey Pham

Report Visualization: https://navi1218.github.io/infx547finalproject/

## Project Proposal: Glossier

### Introduction

The internet-born startup Glossier began as a beauty and fashion blog, Into the Gloss. Its founder Emily Weiss successfully optimized social media marketing to use her site as a platform to launch Glossier. She was able to convert readers into followers and convert followers into brand evangelists, ultimately creating a cult community of minimalist makeup, facial, and skincare enthusiasts.

 Launched in 2014, Glossier has already raised over $35 million in funding, carries 22 products, boasts 805,000 Instagram and 46,000 Twitter followers, and has now expanded internationally as well as into the offline arena (Wischhover). It owes its success largely to three defining components: non-exclusive exclusive brand, fanatical following, and digital analytics.

Glossier's mission is to provide effortless, lit-from-within makeup that play up people's features rather than mask their flaws, riding on the no-makeup and natural makeup trend (Tiku). The company's goal is to make women proud of where they're at everyday, whether they're going to a coffee shop, attending a high-fashion social, or just lounging in the comfort of home. There is a heavy emphasis on accessible inclusivity, practicality, and simple coolness, playing to the idea that anyone can be a "cool girl" (Tiku). The democratic and encompassing yet still fashionable and alluring concept hooked thousands of customers, who regularly and inadvertently advertise for Glossier by posting to social media.

This loyal following generated Glossier's no-marketing marketing plan where customers willingly post Instagram-worthy pictures with Glossier's specially-packaged products, utilize existing and newly-formed hashtags, and spread additional followings by word-of-mouth and referral programs (Wischhover). Hashtags like #glossierpink have arisen to describe the company's iconic washed-out pink, as well as objects and sceneries elsewhere with similar colors, demonstrating the sweeping and contagious reach of Glossier. 

How has Glossier been able to see such tremendous growth for a cosmetics e-commerce site in just a few years? Emily Weiss attributes this success to her team's use of cross-domain analytics tools like Segment, employed to track user movements within and between different Glossier domains (Milnes). Tools like these allow the startup to understand user browsing behavior, measure browsing-to-purchase conversion patterns, and decipher segmented customer experience like those who merely perused versus those who actively provided feedback (Segment). These insights in turn allowed Glossier to better listen to and communicate with its followers and potential customers on its various social media accounts.

Our project team is interested in discovering how people feel regarding the Glossier brand and the products, in an effort to decipher whether their hype is more cult-based or product-based, which will ultimately answer our question of - what factors led to Glossier's success? Based on articles we read, it seems that many people buy into the lifestyle and vibe that the company has ingrained into its branding image, regardless of whether they actually enjoy using the cosmetics products. While there are also others who love the product because of the customer contributions that went into their development as well as the natural look they produce. We want to understand whether the Glossier lifestyle or products contribute more to its hype. This insight may help us identify impactful business and marketing strategies for other startups, e-commerce companies, and beauty retailers. 

As an offshoot of our main research topic, we want to identify the characteristics of the most popular products, which we will identify by looking at number of related posts as well as sentiment analysis of these posts. By determining what attracts customers the most in beauty products, we may help reveal customer preferences in the industry. We also want to know what hashtags are attributed to Glossier tweets by both the company itself and its followers, both company-created and based on folksonomy. This knowledge will not only help us answer our main research topic, but also reveal how people view the company versus how the company views itself. We might be able to discern whether the company vision has successfully conveyed itself and whether feelings for Glossier are constant or change with different products and marketing trends, among other insights.

### Data Collection

For our project, we are primarily collecting data using the Twitter API. We originally hoped to utilize Instagram API but as of early 2017, the platform enforced several stringent restrictions, including allowing only marketing and advertising sectors access (BrightPlanet). Additionally, the ability to obtain a user’s media, like posts and photos, is limited in both rate (#/hour) and number that can be accessed, though that number is not explicitly stated within the technical documentation (Instagram). However, it may still be worthwhile to explore the Instagram API, but significant time should not be spent if it is indeed limited in such a way where we cannot gain enough data for analysis.

Using the Twitter API, we would extract tweets from Glossier’s Twitter account from various time frames in each year it has been established. We are considering targeting the various stages of Glossier's startup, including when the company first started, after the first few and after consumer-contributed products rolled out, after major marketing campaigns, and after significant milestones (going international, Body Hero campaign, pop-up shops) in order to identify how Glossier rose to its success. The tweet elements we will analyze include text, hashtags, likes, comments, links, and retweets, among other items. We will collect both Glossier-created and user-created tweets, and analyze both the tweets themselves as well as the number and possibly content of user comments on these tweets. We will focus on words that convey Glossier's lifestyle, like "cool," "natural," "chic," and "bff," and compare the frequency of these vibe and lifestyle describing terms to words that relate more to the product, like "skincare," "makeup," "boybrow," and "perfume." These will help us determine whether people seem more hyped about the branding or the merchandise. 

### Data Analysis

The data we are most concerned with is text-based: post text content and user comments. Using Python’s Natural Language Toolkit (NLTK) package, we can perform sentiment analysis on posts and user comments. Posts can be organized by parsing the hashtags used. This will give us insight into user views towards not only Glossier, but also in relation to the hashtags used by Glossier and by the user. Additionally, as not all of Glossier’s posts have hashtags or abundant amounts of text, keyword filtering may be necessary to glean context from posts in order to make sense of user views towards Glossier and their posts. We plan to visualize our analyses with tools like Tableau and R, using word clouds and various charts.

### Limitations and Ethical Considerations

By limiting our API access to Twitter, we are missing out on the content-rich space of Instagram where Glossier and its followers post the majority of their pictures, and where the company's primary marketing takes place. The different usage of the Instagram versus Twitter platform stems from the intended usage of the two: picture-sharing versus text and text interaction, respectively.

Additionally, posts by Glossier may not always contain abundant, or any, text nor hashtags nor photos, since Twitter does not require users to post content with all elements present. For photos without textual clues, our analysis ability will be somewhat limited, as photo analysis is difficult and unreliable for non-standard photos without the appropriate metadata. If we are able to extract metadata elements for the posts, then that could serve as a workaround.

With ethical practices in mind, we will anonymize any revealing data components in consideration of the tweet creators and their privacy.  

### Works Cited

BrightPlanet. (2017, Jan 5). "Social Media Data - Instagram Pulls Back on API Access." Retrieved October 26, 2017, from https://brightplanet.com/2017/01/instagram-data/.

Del Russo, Maria. (2016, Jul 2). "The Minimalist's Guide to Makeup." Retrieved October 26, 2017, from
http://www.refinery29.com/minimalist-makeup-brand.

Forbes. (2017, Mar 29). "How Important Has Instagram Been For Glossier's Success?" Retrieved October 26, 2017, from https://www.forbes.com/sites/quora/2017/03/29/how-important-has-instagram-been-for-glossiers-success/amp/.

Gordon, Theo. (2017, Jun 6). "Introducing Cross-Domain Analytics: Unify Customer Profiles Across Your Brands." Retrieved October 26, 2017, from https://segment.com/blog/introducing-cross-domain-analytics-unify-customer-profiles-across-your-brands/.

Tiku, Nitasha. (2016, Aug 25). "Inside Glossier, The Beauty Startup That Just Happens to Sell Makeup." Retrieved October 26, 2017, from https://www.buzzfeed.com/nitashatiku/inside-glossier-the-beauty-startup-that-just-happens-to-sell?utm_term=.evp6M1A5V#.gwVNQdXw6.

Instagram. (2017). Instagram Developer Documentation. Retrieved October 26, 2017, from https://www.instagram.com/developer/.

Milnes, Hilary. (2017, Jun 13). "How Glossier Uses Data to Make Content and Commerce Work." Retrieved October 26, 2017, from https://digiday.com/marketing/glossier-uses-data-make-content-commerce-work/.

O'Connor, Clare. (2016, Nov 30). "Cult Beauty Brand Glossier Raises $24M Series B to Open Retail Stores, Go International." Retrieved October 26, 2017, from https://www.forbes.com/sites/clareoconnor/2016/11/30/cult-beauty-brand-glossier-raises-24m-series-b-to-open-retail-stores-go-international/#3b8aac5923fa.

Social Bearing. (n.d.). User Search and Analytics for "@glossier" Retrieved October 26, 2017, from https://socialbearing.com/search/user/glossier.

Wischhover, Cheryl. (2017, Jul 12). "Glossier is Going After New Customers With an Army of Reps." Retrieved October 26, 2017, from https://www.racked.com/2017/7/12/15949530/glossier-international-shipping-canada-uk.





